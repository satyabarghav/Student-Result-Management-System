# Generated by Django 4.2.6 on 2023-11-04 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminApp', '0008_remove_result_enrollment_delete_enrollment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='courses',
            field=models.ManyToManyField(related_name='students', to='adminApp.course'),
        ),
    ]
