# Generated by Django 2.1.7 on 2019-04-09 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
