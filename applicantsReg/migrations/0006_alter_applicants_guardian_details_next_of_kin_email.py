# Generated by Django 5.0.4 on 2024-05-02 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicantsReg', '0005_alter_applicant_other_qualifications_training_or_workshop1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicants_guardian_details',
            name='next_of_kin_email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
