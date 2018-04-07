# Generated by Django 2.0.3 on 2018-04-06 09:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profileprojects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Booking_Modified_Date', models.DateTimeField(auto_now=True)),
                ('Booking_Created_Date', models.DateTimeField(auto_now_add=True)),
                ('Booking_Status', models.CharField(max_length=100)),
                ('Booking_Charges_After_Negotiable', models.CharField(max_length=100)),
                ('Booking_From_Date', models.DateField()),
                ('Booting_Till_Date', models.DateField()),
                ('Booking_Project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Booking', to='profileprojects.ProfileProject')),
                ('Booking_User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creator_bookings', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Booking_Comment', models.CharField(max_length=150)),
                ('Booking_Comment_Author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booking_comment', to=settings.AUTH_USER_MODEL)),
                ('Comment_Booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Comment_Bookingnew', to='bookings.Booking')),
            ],
        ),
    ]