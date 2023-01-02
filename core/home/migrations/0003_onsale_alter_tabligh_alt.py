# Generated by Django 4.1.3 on 2023-01-02 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_tabligh_alt_tabligh_text2'),
    ]

    operations = [
        migrations.CreateModel(
            name='OnSale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('text', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('alt', models.CharField(max_length=50)),
                ('date', models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name='tabligh',
            name='alt',
            field=models.CharField(max_length=50),
        ),
    ]
