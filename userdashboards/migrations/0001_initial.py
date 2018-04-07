# Generated by Django 2.0.3 on 2018-04-06 09:48

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
            name='UserDashBoard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserDashBoard_Talent', models.BooleanField(default=False)),
                ('UserDashBoard_Crew', models.BooleanField(default=False)),
                ('UserDashBoard_Producer', models.BooleanField(default=False)),
                ('UserDashBoard_Service_Provider', models.BooleanField(default=False)),
                ('UserDashBoard_User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='UserDashBoard', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
