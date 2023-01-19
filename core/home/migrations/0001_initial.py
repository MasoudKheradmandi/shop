# Generated by Django 4.1.3 on 2023-01-19 11:00

import colorfield.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
        ('product', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='FooterOne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='NavOne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='نام نوبار')),
                ('link', models.CharField(max_length=100, verbose_name='لینک نوبار')),
            ],
        ),
        migrations.CreateModel(
            name='SiteSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.FileField(null=True, upload_to='', verbose_name='لوگو')),
                ('alt', models.CharField(max_length=100, null=True, verbose_name='توضیحات لوگو')),
                ('favicon', models.FileField(null=True, upload_to='', verbose_name='آیکون')),
                ('alt2', models.CharField(max_length=100, null=True, verbose_name='توضیحات icon')),
                ('telephon', models.CharField(max_length=30, null=True, verbose_name='تلفن')),
                ('footer_text', models.CharField(max_length=300, null=True, verbose_name='متن فوتر')),
                ('email', models.EmailField(max_length=100, null=True, verbose_name='ایمیل')),
                ('address', models.CharField(max_length=200, null=True, verbose_name='ادرس')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=False, verbose_name='تنظیمات فعال؟')),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text1', models.CharField(max_length=300, null=True, verbose_name='متن یک')),
                ('text2', models.CharField(max_length=300, null=True, verbose_name='متن دو')),
                ('text3', models.CharField(max_length=300, null=True, verbose_name='متن سه')),
                ('image', models.ImageField(upload_to='', verbose_name='عکس سلایدر')),
                ('alt', models.CharField(max_length=100, verbose_name='توضیح عکس')),
                ('name_button', models.CharField(max_length=100, null=True, verbose_name='متن دکمه')),
                ('link', models.CharField(max_length=100, null=True, verbose_name='ادرس دکمه')),
            ],
        ),
        migrations.CreateModel(
            name='Tabligh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('alt', models.CharField(max_length=50)),
                ('text', models.CharField(max_length=100, null=True, verbose_name='متن')),
                ('text2', models.CharField(max_length=100, null=True, verbose_name='2متن')),
                ('diraction', models.CharField(choices=[('right', 'راست'), ('left', 'چپ'), ('right2', 'راست (کنار محصولات)')], max_length=100, verbose_name='مکان تبلیغ')),
                ('link', models.CharField(max_length=400, null=True, verbose_name='لینک تبلیغ')),
            ],
        ),
        migrations.CreateModel(
            name='WishList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', colorfield.fields.ColorField(blank=True, default=None, image_field=None, max_length=18, null=True, samples=None)),
                ('size', models.CharField(max_length=20, null=True, verbose_name='سایز')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.profile')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
        migrations.CreateModel(
            name='OnSale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('text', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('alt', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('is_show', models.BooleanField(default=True)),
                ('products', models.ManyToManyField(to='product.product')),
            ],
        ),
        migrations.CreateModel(
            name='NavTwo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='نام نوبار')),
                ('link', models.CharField(max_length=100, verbose_name='لینک نوبار')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home.navone')),
            ],
        ),
        migrations.CreateModel(
            name='FooterTwo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='نام')),
                ('link', models.CharField(max_length=100, null=True, verbose_name='لینک صفحه')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home.footerone')),
            ],
        ),
    ]
