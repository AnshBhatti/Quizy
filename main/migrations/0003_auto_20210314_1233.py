# Generated by Django 3.0.6 on 2021-03-14 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210314_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='img',
            field=models.FileField(default='/assets/logo.png', upload_to=''),
        ),
        migrations.AlterField(
            model_name='questions',
            name='img1',
            field=models.FileField(default='/assets/logo.png', upload_to=''),
        ),
        migrations.AlterField(
            model_name='questions',
            name='img2',
            field=models.FileField(default='/assets/logo.png', upload_to=''),
        ),
        migrations.AlterField(
            model_name='questions',
            name='img3',
            field=models.FileField(default='/assets/logo.png', upload_to=''),
        ),
    ]