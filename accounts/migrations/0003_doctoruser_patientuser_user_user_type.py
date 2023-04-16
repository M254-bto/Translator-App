# Generated by Django 4.1.7 on 2023-04-15 17:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        (
            "accounts",
            "0002_delete_message_remove_user_county_remove_user_gender_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="DoctorUser",
            fields=[
                (
                    "user_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"abstract": False,},
            bases=("accounts.user",),
        ),
        migrations.CreateModel(
            name="PatientUser",
            fields=[
                (
                    "user_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"abstract": False,},
            bases=("accounts.user",),
        ),
        migrations.AddField(
            model_name="user",
            name="user_type",
            field=models.CharField(
                choices=[("patient", "Patient"), ("doctor", "Doctor")],
                default="patient",
                max_length=20,
            ),
        ),
    ]