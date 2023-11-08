# Generated by Django 4.2.6 on 2023-11-04 20:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminApp', '0009_alter_student_courses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='courses',
            field=models.ManyToManyField(default=[], related_name='students', to='adminApp.course'),
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_marks', models.DecimalField(decimal_places=2, max_digits=5)),
                ('percentage', models.DecimalField(decimal_places=2, max_digits=5)),
                ('grade', models.CharField(max_length=2)),
                ('result_source', models.CharField(choices=[('internal', 'Internal'), ('external', 'External')], default='internal', max_length=10)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminApp.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminApp.student')),
            ],
            options={
                'unique_together': {('student', 'course')},
            },
        ),
        migrations.CreateModel(
            name='Marks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marks_obtained', models.DecimalField(decimal_places=2, max_digits=5)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminApp.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminApp.student')),
            ],
            options={
                'unique_together': {('student', 'course')},
            },
        ),
    ]