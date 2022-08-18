# Generated by Django 3.2.7 on 2021-09-07 15:31

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('portal', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('co_introduction', models.TextField()),
                ('logo', models.ImageField(default='default.png', upload_to='co-logo')),
                ('link', models.CharField(max_length=80)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.category')),
                ('employer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('location', models.CharField(max_length=80)),
                ('created_date', models.DateTimeField(blank=True, default=datetime.datetime(2021, 9, 7, 20, 1, 19, 446506))),
                ('experience', models.CharField(choices=[('no-matter', 'مهم نیست'), ('1-3', 'یک تا ۳ سال'), ('3-6', 'سه تا ۶ سال'), ('+6', 'بیشتر از ۶ سال')], max_length=80)),
                ('salary', models.CharField(choices=[('agreement ', 'توافقی'), ('from 3', 'از ۳ میلیون'), ('from 5', 'از ۵ میلیون'), ('from 8', 'از ۸ میلیون'), ('from 10', 'از ۱۰ میلیون'), ('from 12', 'از ۱۲ میلیون'), ('from 15', 'از ۱۵ میلیون')], max_length=80)),
                ('cooperation_type', models.CharField(choices=[('full-time', 'تمام وقت'), ('part-time', 'پاره وقت'), ('remote', 'دور کاری'), ('internship', 'کار آموزی')], max_length=80)),
                ('job_description', models.TextField()),
                ('skills_required', models.CharField(max_length=80)),
                ('military_service', models.CharField(choices=[('no-matter', 'مهم نیست'), ('end', 'پایان خدمت')], max_length=80)),
                ('degree', models.CharField(choices=[('no-matter', 'مهم نیست'), ('diploma', 'دیپلم'), ('bachelor', 'لیسانس')], max_length=80)),
                ('gender', models.CharField(choices=[('Male', 'مرد'), ('Female', 'زن'), ('not-matter', 'مهم نیست')], max_length=10)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.category')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='employer.company')),
            ],
        ),
        migrations.CreateModel(
            name='JobRequests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume_url', models.CharField(max_length=100)),
                ('accepted', models.BooleanField(default=False)),
                ('hired', models.BooleanField(default=False)),
                ('viewed', models.BooleanField(default=False)),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employer.company')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employer.job')),
                ('jobseeker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]