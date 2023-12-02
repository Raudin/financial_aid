from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    BACKGROUND_CHOICES = [
        ('Orphan', 'Orphan'),
        ('Non-Orphan', 'Non-Orphan'),
        ('Single-orphan', 'Single-orphan'),
    ]
    
    COUNTY_CHOICES = [
    ('Mombasa', 'Mombasa'),
    ('Kwale', 'Kwale'),
    ('Kilifi', 'Kilifi'),
    ('Tana River', 'Tana River'),
    ('Lamu', 'Lamu'),
    ('Taita-Taveta', 'Taita-Taveta'),
    ('Garissa', 'Garissa'),
    ('Wajir', 'Wajir'),
    ('Mandera', 'Mandera'),
    ('Marsabit', 'Marsabit'),
    ('Isiolo', 'Isiolo'),
    ('Meru', 'Meru'),
    ('Tharaka-Nithi', 'Tharaka-Nithi'),
    ('Embu', 'Embu'),
    ('Kitui', 'Kitui'),
    ('Machakos', 'Machakos'),
    ('Makueni', 'Makueni'),
    ('Nyandarua', 'Nyandarua'),
    ('Nyeri', 'Nyeri'),
    ('Kirinyaga', 'Kirinyaga'),
    ('Murang\'a', 'Murang\'a'),
    ('Kiambu', 'Kiambu'),
    ('Turkana', 'Turkana'),
    ('West Pokot', 'West Pokot'),
    ('Samburu', 'Samburu'),
    ('Trans-Nzoia', 'Trans-Nzoia'),
    ('Uasin Gishu', 'Uasin Gishu'),
    ('Elgeyo-Marakwet', 'Elgeyo-Marakwet'),
    ('Nandi', 'Nandi'),
    ('Baringo', 'Baringo'),
    ('Laikipia', 'Laikipia'),
    ('Nakuru', 'Nakuru'),
    ('Narok', 'Narok'),
    ('Kajiado', 'Kajiado'),
    ('Kericho', 'Kericho'),
    ('Bomet', 'Bomet'),
    ('Kakamega', 'Kakamega'),
    ('Vihiga', 'Vihiga'),
    ('Bungoma', 'Bungoma'),
    ('Busia', 'Busia'),
    ('Siaya', 'Siaya'),
    ('Kisumu', 'Kisumu'),
    ('Homa Bay', 'Homa Bay'),
    ('Migori', 'Migori'),
    ('Kisii', 'Kisii'),
    ('Nyamira', 'Nyamira'),
    ('Nairobi.', 'Nairobi.'),
]


    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField('default.jpg', upload_to='profile_pics', null =True, blank = True)
    gender = models.CharField(max_length=15, choices=GENDER_CHOICES)
    number = models.CharField(max_length=100, null=True, blank=True)
    
    #Used fir Classification
    background = models.CharField(max_length=15, choices=BACKGROUND_CHOICES)
    sponsor = models.BooleanField(default=False)
    disabled = models.BooleanField(default=False)
    refugee_or_immigrant = models.BooleanField(default=False)
    kcse = models.CharField(max_length=5)
    kcpe = models.CharField(max_length=5)
    county = models.CharField(max_length=30, choices=COUNTY_CHOICES)
    extra_curricular = models.BooleanField(default=False)
    leadership = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.user.username} Profile'
