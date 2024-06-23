# Generated by Django 4.2.5 on 2024-06-23 06:06

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
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('pin_code', models.IntegerField()),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('category_image', models.ImageField(upload_to='category_images/')),
            ],
        ),
        migrations.CreateModel(
            name='RentRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rent_type', models.CharField(choices=[('one_day', 'One Day'), ('one_week', 'One Week'), ('one_month', 'One Month'), ('one_year', 'One Year'), ('direct_buy', 'Direct Buy')], max_length=10)),
                ('pay_per_duration', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='RentPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('post_image', models.ImageField(upload_to='post_images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('whatsapp_number', models.CharField(max_length=15)),
                ('phone_number', models.CharField(max_length=15)),
                ('term_and_condition', models.TextField()),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rent_now.address')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rent_now.category')),
                ('rent_request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rent_now.rentrequest')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RentOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('requested', 'Requested'), ('accepeted', 'Accepted'), ('completed', 'Completed')], default='requested', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user_phone_number', models.CharField(max_length=15)),
                ('user_whatsapp_number', models.CharField(max_length=15)),
                ('rent_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rent_now.rentpost')),
                ('rent_request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rent_now.rentrequest')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rent_now.address')),
            ],
        ),
    ]