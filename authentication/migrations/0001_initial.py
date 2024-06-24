# Generated by Django 5.0.6 on 2024-06-24 06:03

import django.contrib.auth.models
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='DistrictModel',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('Pid', models.IntegerField()),
                ('LocationType', models.CharField(max_length=100)),
                ('districtname', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='RegisterMedicals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Medical_name', models.CharField(max_length=50)),
                ('dl_number1', models.CharField(max_length=30)),
                ('dl_number2', models.CharField(max_length=30)),
                ('UniqueId', models.CharField(max_length=30, null=True)),
                ('medical_timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='StateModel',
            fields=[
                ('Pid', models.IntegerField(primary_key=True, serialize=False)),
                ('LocationType', models.CharField(max_length=100)),
                ('Pname', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(max_length=150, unique=True, verbose_name='Username')),
                ('phone_num', models.CharField(blank=True, max_length=15, unique=True, verbose_name='Phone Number')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('pin', models.PositiveIntegerField(blank=True, null=True, verbose_name='PIN')),
                ('store_type', models.CharField(blank=True, choices=[('retailer', 'Retailer'), ('manufacturer', 'Manufacturer'), ('pharmacy', 'Pharmacy'), ('medical', 'Medical'), ('others', 'Others')], max_length=50, null=True, verbose_name='Store Type')),
                ('other_value', models.CharField(blank=True, max_length=50, null=True, verbose_name='Other Value')),
                ('position', models.CharField(blank=True, choices=[('Admin', 'Admin'), ('Senior', 'Senior'), ('Member', 'Member'), ('NewUser', 'NewUser')], default='Admin', max_length=20, null=True, verbose_name='Position')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='customuser_set', to='auth.group', verbose_name='Groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='customuser_set', to='auth.permission', verbose_name='User Permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='ConnectMedicals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_read', models.BooleanField(default=False)),
                ('accept_status', models.BooleanField(default=True)),
                ('request_message', models.TextField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('request_receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='request_receiver', to=settings.AUTH_USER_MODEL)),
                ('request_sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='request_sender', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MedicalShopName', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('ProprietaryName', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('ProprietaryNumber', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('ProprietaryContact', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('DrugLiceneseNumber2', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('DrugLiceneseNumber1', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('City', models.CharField(blank=True, max_length=100, null=True)),
                ('Pincode', models.CharField(blank=True, max_length=100, null=True)),
                ('StreetNumber', models.CharField(blank=True, max_length=100, null=True)),
                ('DoorNumber', models.CharField(blank=True, max_length=100, null=True)),
                ('PharmacistName', models.CharField(blank=True, max_length=100, null=True)),
                ('RegisteredNumber', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('ContactNumber', models.CharField(blank=True, max_length=15, null=True)),
                ('PharmacistEmail', models.EmailField(blank=True, max_length=254, null=True)),
                ('UniqueId', models.CharField(blank=True, max_length=100, null=True)),
                ('temporaryNo', models.CharField(blank=True, max_length=50, null=True)),
                ('district', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='authentication.districtmodel')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('state', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='authentication.statemodel')),
            ],
        ),
        migrations.AddField(
            model_name='districtmodel',
            name='state',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='authentication.statemodel'),
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('message', models.TextField(default='Notification')),
                ('is_read', models.BooleanField(default=False)),
                ('request_status', models.BooleanField(default=True)),
                ('position', models.CharField(max_length=20, null=True)),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_notifications', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_notifications', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('sender', 'receiver')},
            },
        ),
    ]
