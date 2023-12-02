from django.urls import path
from . import views

app_name = "aid"

urlpatterns = [
    path('', views.index, name='scholarship-categories'),
    path('category/<int:category_id>', views.scholarships,
         name='scholarship-categories-items'),
    path('category/<int:category_id>/item/<int:item_id>',
         views.item, name='scholarship-item'),
    path('applications', views.applications, name='scholarship-applications'),
    path('applications/classify', views.classify,
         name='scholarship-applications-classify'),
    path('send-message/', views.sendMessage, name='send_message'),
]
