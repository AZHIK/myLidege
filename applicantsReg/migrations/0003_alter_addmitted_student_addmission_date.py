# Generated by Django 5.0.4 on 2024-05-01 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicantsReg', '0002_rename_next_of_kin_relatioship_applicants_guardian_details_next_of_kin_relationship'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addmitted_student',
            name='addmission_date',
            field=models.DateField(null=True),
        ),
    ]
