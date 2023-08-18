# Generated by Django 4.1.7 on 2023-08-18 10:57

import django.core.validators
from django.db import migrations, models
import django_jalali.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentMethodeDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PaymentDetails', models.CharField(choices=[('1', 'پرداخت توسط فیش بانکی'), ('2', 'زرین پال')], default=1, max_length=20, verbose_name='روش ارسال')),
                ('isTermsAndRules', models.BooleanField(default=False, verbose_name=' پذیرفتن شرایط ')),
                ('peymentCode', models.CharField(blank=True, max_length=150, null=True, validators=[django.core.validators.RegexValidator(regex='^\\d{25}$')], verbose_name=' کد پرداخت ')),
            ],
            options={
                'verbose_name': 'جزئیات پرداخت',
                'verbose_name_plural': 'جرئیات پرداخت',
            },
        ),
        migrations.CreateModel(
            name='PostAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=150, verbose_name='نام')),
                ('lastName', models.CharField(max_length=150, verbose_name='نام خانوادگی')),
                ('country', models.CharField(choices=[('iran', 'ایران')], default='iran', max_length=20, verbose_name='کشور')),
                ('city', models.CharField(max_length=150, verbose_name='شهر')),
                ('address', models.TextField(verbose_name='آدرس')),
                ('phone_number', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '0999999999'. Up to 15 digits allowed.", regex='^\\0?1?\\d{9,15}$')], verbose_name='تلفن ثابت')),
                ('mobile_phone_number', models.CharField(max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '0999999999'. Up to 15 digits allowed.", regex='^\\0?1?\\d{9,15}$')], verbose_name='تلفن همراه')),
                ('post_code', models.CharField(max_length=20, verbose_name='کد پستی')),
                ('isCorrect_mobile_phone_number', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'اطلاعات پست',
                'verbose_name_plural': 'اطلاعات پست',
            },
        ),
        migrations.CreateModel(
            name='PostAddressDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carrierDetails', models.CharField(choices=[('1', 'پست'), ('2', 'تیپاکس'), ('3', 'باربری')], default=1, max_length=20, verbose_name='روش ارسال')),
                ('isResive', models.BooleanField(default=False)),
                ('carried', django_jalali.db.models.jDateTimeField(blank=True, null=True, verbose_name='تاریخ حمل شده')),
                ('sentToShippingUnit', django_jalali.db.models.jDateTimeField(blank=True, null=True, verbose_name='تاریخ ارسال شده به واحد حمل')),
                ('collected', django_jalali.db.models.jDateTimeField(blank=True, null=True, verbose_name='تاریخ جمع آوری شده')),
                ('collecting', django_jalali.db.models.jDateTimeField(blank=True, null=True, verbose_name='تاریخ در حال جمع اوری')),
                ('Ongoing', django_jalali.db.models.jDateTimeField(blank=True, null=True, verbose_name='تاریخ در دست اقدام')),
                ('processing', django_jalali.db.models.jDateTimeField(blank=True, null=True, verbose_name='تاریخ در حال پردازش')),
                ('confirmedPayment', django_jalali.db.models.jDateTimeField(blank=True, null=True, verbose_name='تاریخ پرداخت تایید شده')),
            ],
            options={
                'verbose_name': 'اطلاعات آدرس انتخابی',
                'verbose_name_plural': 'اطلاعات آدرس',
            },
        ),
        migrations.CreateModel(
            name='PostPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='هزینه ارسال ')),
                ('price', models.IntegerField(verbose_name='هزینه ی پست')),
            ],
            options={
                'verbose_name': 'پست',
                'verbose_name_plural': 'هزینه ارسال',
            },
        ),
    ]