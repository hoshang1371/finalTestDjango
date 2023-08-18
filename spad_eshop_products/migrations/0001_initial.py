# Generated by Django 4.1.7 on 2023-08-18 10:57

from django.db import migrations, models
import django.db.models.deletion
import spad_eshop_products.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('spad_eshop_products_category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='عنوان')),
                ('code', models.CharField(max_length=150, verbose_name='کد')),
                ('place', models.CharField(blank=True, max_length=150, null=True, verbose_name='مکان کالا')),
                ('number', models.CharField(blank=True, max_length=150, null=True, verbose_name='تعداد')),
                ('brand', models.CharField(blank=True, max_length=150, null=True, verbose_name='برند')),
                ('description', models.TextField(verbose_name='توضیحات')),
                ('smallDescription', models.TextField(max_length=150, verbose_name='کوتاه توضیحات')),
                ('price', models.IntegerField(verbose_name='قیمت')),
                ('priceOff', models.IntegerField(blank=True, null=True, verbose_name='قیمت تخفیف')),
                ('image', models.ImageField(blank=True, null=True, upload_to=spad_eshop_products.models.upload_image_path, verbose_name='تصویر')),
                ('image_tumpnail', models.ImageField(blank=True, null=True, upload_to=spad_eshop_products.models.upload_image_tumpnail_path, verbose_name='تصویر_بند_انگشتی')),
                ('active', models.BooleanField(default=False, verbose_name='فعال / غیرفعال')),
                ('visit_count', models.IntegerField(default=0, verbose_name='تعداد بازدید ها')),
                ('vige', models.BooleanField(default=False, verbose_name='ویژه / غیرویژه')),
                ('categories', models.ManyToManyField(blank=True, to='spad_eshop_products_category.productcategory', verbose_name='دسته بندی ها')),
            ],
            options={
                'verbose_name': 'محصول',
                'verbose_name_plural': 'محصولات',
            },
        ),
        migrations.CreateModel(
            name='ProductGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='عنوان')),
                ('image', models.ImageField(upload_to=spad_eshop_products.models.upload_gallery_image_path, verbose_name='تصویر')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spad_eshop_products.product', verbose_name='محصول')),
            ],
            options={
                'verbose_name': 'تصویر',
                'verbose_name_plural': 'تصاویر',
            },
        ),
    ]
