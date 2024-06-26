# Generated by Django 5.0.4 on 2024-05-07 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicantsReg', '0007_addmitted_student_submission_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='addmitted_student',
            name='addmission_approval',
            field=models.CharField(choices=[('Approved', 'Approved'), ('Rejected', 'Rejected')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='addmitted_student',
            name='addmission_reject_reason',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='reffered_by',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
