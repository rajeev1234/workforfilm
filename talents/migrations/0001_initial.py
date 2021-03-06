# Generated by Django 2.0.3 on 2018-04-06 07:10

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
            name='Talent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Talent_Actor', models.BooleanField(default=False)),
                ('Talent_Child_Artist', models.BooleanField(default=False)),
                ('Talent_Dancer', models.BooleanField(default=False)),
                ('Talent_Mimicry_Artist', models.BooleanField(default=False)),
                ('Talent_Models', models.BooleanField(default=False)),
                ('Talent_Musician', models.BooleanField(default=False)),
                ('Talent_Singer', models.BooleanField(default=False)),
                ('Talent_Special_Art', models.BooleanField(default=False)),
                ('Talent_Theater_Artist', models.BooleanField(default=False)),
                ('Talent_Voice_Over_Artist', models.BooleanField(default=False)),
                ('Talent_User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Talent', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
