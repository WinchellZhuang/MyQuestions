# Generated by Django 2.1.2 on 2018-10-30 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='u_last_login_datetime',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='u_last_login_ip',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
