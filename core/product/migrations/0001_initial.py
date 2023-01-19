# Generated by Django 4.1.3 on 2023-01-19 11:00

import ckeditor.fields
import colorfield.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='نام دسته بندی')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='')),
                ('alt', models.CharField(max_length=100)),
                ('image_2', models.ImageField(blank=True, null=True, upload_to='')),
                ('alt_2', models.CharField(blank=True, max_length=100, null=True)),
                ('price', models.IntegerField(verbose_name='قیمت اصلی')),
                ('product_count', models.PositiveBigIntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='تعداد محصول')),
                ('instock', models.BooleanField(null=True)),
                ('info', ckeditor.fields.RichTextField()),
                ('discount', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)], verbose_name='درصد تخفیف')),
                ('orgin_color', colorfield.fields.ColorField(default='#FFFFFF', image_field=None, max_length=18, samples=[('#FFFFFF', 'white'), ('#000000', 'black')])),
                ('orgin_size', models.CharField(max_length=20)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.category')),
            ],
        ),
        migrations.CreateModel(
            name='TagProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=20, verbose_name='سایز')),
                ('Ekhtelaf', models.IntegerField(default=0, verbose_name='اختلاف قیمت')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.product')),
            ],
            options={
                'verbose_name': 'سایز های بیشتر کیف',
                'verbose_name_plural': 'سایز های بیشتر کیف',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='tag',
            field=models.ManyToManyField(to='product.tagproduct'),
        ),
        migrations.CreateModel(
            name='GalleryImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(unique=True, upload_to='', verbose_name='عکس محصول')),
                ('alt', models.CharField(max_length=150, verbose_name='توضیحات عکس')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.product')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('body', models.TextField()),
                ('point', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=1)),
                ('created', models.DateTimeField(auto_now=True)),
                ('is_show', models.BooleanField(default=False)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
            options={
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', colorfield.fields.ColorField(default='#FFFFFF', image_field=None, max_length=18, samples=[('#FFFFFF', 'white'), ('#000000', 'black')])),
                ('Ekhtelaf', models.IntegerField(default=0, verbose_name='اختلاف قیمت')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.product')),
            ],
            options={
                'verbose_name': 'رنگ های بیشتر',
                'verbose_name_plural': 'رنگ های بیشتر',
            },
        ),
    ]
