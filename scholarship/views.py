from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied
from .logistic_regression import classify as lr
from .message import send_sms
from django.http import JsonResponse
from users.models import Profile

# third-party import
import csv

# local imports
from .models import Category, Scholarship, Application
# Create your views here.


@login_required
def index(request):
    context = {
        'categories': Category.objects.all()
    }
    return render(request, 'scholarship/index.html', context)


def homepage(request):
    return render(request, 'scholarship/base.html')


@login_required
def scholarships(request, category_id):
    context = {
        'category': Category.objects.get(id=category_id),
        'scholarships': Scholarship.objects.filter(category=category_id)
    }
    return render(request, 'scholarship/scholarships.html', context)


@login_required
def item(request, category_id, item_id):
    scholarship = Scholarship.objects.get(id=item_id)
    applications = scholarship.application_set.filter(user=request.user)

    if request.method == 'POST':
        if applications.count():
            applications.delete()
            application = None
        else:
            application = Application(
                user=request.user, scholarship=scholarship)
            application.save()
    else:
        application = applications.first

    context = {
        'scholarship': scholarship,
        'application': application
    }
    return render(request, 'scholarship/item.html', context)


@login_required
def applications(request):
    accepted = Application.objects.filter(accepted=True)
    rejected = Application.objects.filter(accepted=False)
    pending = Application.objects.filter(accepted__isnull=True)

    if not request.user.is_staff:
        accepted = accepted.filter(user=request.user)
        rejected = rejected.filter(user=request.user)
        pending = pending.filter(user=request.user)

    context = {
        'accepted': accepted,
        'rejected': rejected,
        'pending': pending,
    }
    return render(request, 'scholarship/applications.html', context)


@login_required
def classify(request):
    if not request.user.is_staff:
        raise PermissionDenied

    if request.method == 'POST':
        # header = ['id', 'first_name', 'last_name', 'email',
        #           'gender', 'sponsor', 'background', 'aid']
        
        header =  ['id','sponsor','disabled','refugee_or_immigrant','family_background','KCSE','KCPE','aid','county', 'extra-curricular','leadership']
        
        
        data = []

        pending = Application.objects.filter(accepted__isnull=True)

        for application in pending:
            data.append(
                [application.id,
                 application.user.profile.sponsor,
                 application.user.profile.disabled,
                 application.user.profile.refugee_or_immigrant,
                 application.user.profile.background, 
                 application.user.profile.kcse,
                 application.user.profile.kcpe,
                 application.scholarship.category.title,
                 application.user.profile.county,
                 application.user.profile.extra_curricular,
                 application.user.profile.leadership,
                 ]
            )

        with open(f'{settings.MEDIA_ROOT}/data/pending.csv', 'w', encoding='UTF8') as f:
            writer = csv.writer(f)

            # write the header
            writer.writerow(header)

            # write the data
            writer.writerows(data)

        lr(f'{settings.MEDIA_ROOT}/data/')

        with open(f'{settings.MEDIA_ROOT}/data/outputs.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # print(row['id'], row['accepted'])
                application = Application.objects.get(id=row['id'])
                if row['accepted'] == '1':
                    application.accepted = True
                else:
                    application.accepted = False
                application.save()

    return redirect('aid:scholarship-applications')


def sendMessage(request):
    if request.method == 'POST':
        profile_id = request.POST.get('profile_id')
        profile = Profile.objects.get(id=profile_id)
        # Call the send_message function
        name = profile.user.username  # Replace with actual field name
        number = profile.number  # Replace with actual field name

        application_id = request.POST.get('application_id')
        application = Application.objects.get(id=application_id)
        application_type = application.scholarship.title

        if application.accepted == True:
            message = f"Hi {name} this is financial aid. Your Application for {application_type} has been approved and the funds will be dispersed."
            send_sms.sending(number, name, message)
        else:
            message = f"Hi {name} this is financial aid. Your Application for {application_type} has been declined."
            send_sms.sending(number, name, message)

        # Return a JSON response with the message
        return JsonResponse({'message': 'message sent'})

    return JsonResponse({'error': 'Invalid request method'})
