# Generated by Django 2.1.7 on 2019-05-05 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbms', '0002_auto_20190409_2105'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='permission',
            field=models.CharField(default=1, max_length=1),
            preserve_default=False,
        ),
    ]
