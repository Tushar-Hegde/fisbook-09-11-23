# Generated by Django 2.1 on 2023-09-11 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0005_auto_20230911_2332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forum',
            name='pic',
            field=models.ImageField(default='media/forums/Dragonfruit2.jpg', upload_to='forums'),
        ),
    ]
