# Generated by Django 3.2.8 on 2021-11-30 10:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('scholarship', '0002_auto_20211111_1411'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.IntegerField(default=0)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('scholarship', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='scholarship.scholarship')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
