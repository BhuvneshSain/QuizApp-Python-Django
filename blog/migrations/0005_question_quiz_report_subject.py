# Generated by Django 3.0.5 on 2020-04-06 11:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0004_auto_20200406_1519'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quiz_name', models.CharField(max_length=250)),
                ('score', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(default='NA', max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='taken_quizzes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('code', models.CharField(max_length=12)),
                ('description', models.TextField()),
                ('time_limit', models.PositiveIntegerField(help_text='In Minuts')),
                ('total_questions', models.PositiveIntegerField(help_text='Must be less than 10')),
                ('passing_marks', models.PositiveIntegerField(help_text='Must be less than 100')),
                ('marks_per_question', models.PositiveIntegerField()),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quizzes', to='blog.Subject')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('option_A', models.CharField(max_length=200)),
                ('option_B', models.CharField(max_length=200)),
                ('option_C', models.CharField(max_length=200)),
                ('option_D', models.CharField(max_length=200)),
                ('Answer', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=1, null=True)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='blog.Subject')),
            ],
        ),
    ]
