# Generated by Django 2.1.4 on 2019-01-11 11:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('latitude', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('longitude', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('my_description', models.CharField(blank=True, default=None, max_length=1024, null=True)),
                ('twitter_handle', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('facebook_handle', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('instagram_handle', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('paypal_email', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('device_token', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('onetime_token', models.CharField(blank=True, default=None, max_length=255, null=True, unique=True)),
                ('avatar', models.FileField(blank=True, default=None, null=True, upload_to='avatars')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'hs_user_profile',
            },
        ),
        migrations.CreateModel(
            name='Timezones',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('county_code', models.CharField(blank=True, default=None, max_length=2, null=True)),
                ('lat_long', models.CharField(blank=True, default=None, max_length=12, null=True)),
                ('tz_name', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('country_portion', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('status', models.CharField(blank=True, default=None, max_length=10, null=True)),
                ('utc_offset', models.CharField(blank=True, default=None, max_length=6, null=True)),
                ('utc_dst_offset', models.CharField(blank=True, default=None, max_length=6, null=True)),
                ('notes', models.TextField(blank=True, default=None, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'hs_timezones',
            },
        ),
        migrations.AddField(
            model_name='profile',
            name='timezone',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Timezones'),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]