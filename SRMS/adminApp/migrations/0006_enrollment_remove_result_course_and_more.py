# Generated by Django 4.2.6 on 2023-11-04 05:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminApp', '0005_result_course_type_result_exam_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminApp.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminApp.student')),
            ],
        ),
        migrations.RemoveField(
            model_name='result',
            name='course',
        ),
        migrations.RemoveField(
            model_name='result',
            name='course_type',
        ),
        migrations.RemoveField(
            model_name='result',
            name='exam_type',
        ),
        migrations.RemoveField(
            model_name='result',
            name='student',
        ),
        migrations.RemoveField(
            model_name='result',
            name='total_marks',
        ),
        migrations.AlterField(
            model_name='result',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterModelTable(
            name='result',
            table=None,
        ),
        migrations.DeleteModel(
            name='Marks',
        ),
        migrations.AddField(
            model_name='result',
            name='enrollment',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='adminApp.enrollment'),
        ),
    ]
