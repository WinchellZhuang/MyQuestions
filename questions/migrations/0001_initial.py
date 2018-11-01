# Generated by Django 2.1.2 on 2018-10-29 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_title', models.CharField(blank=True, max_length=100, null=True)),
                ('c_happen_date', models.DateTimeField(auto_now_add=True)),
                ('c_resolvent', models.TextField(null=True)),
                ('c_resolvent_date', models.DateTimeField(null=True)),
                ('isDelete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='QuestionSolve',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_solve', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='QuestionSource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q_source', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SubjectInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_create_datetime', models.DateTimeField(auto_now_add=True)),
                ('u_real_name', models.CharField(blank=True, max_length=20, null=True)),
                ('u_login_name', models.CharField(max_length=20)),
                ('u_pwd', models.CharField(max_length=20)),
                ('u_last_login_datetime', models.DateTimeField(auto_now=True)),
                ('u_last_login_ip', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='questioncomment',
            name='c_qst_source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.QuestionSource'),
        ),
        migrations.AddField(
            model_name='questioncomment',
            name='c_solve',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.QuestionSolve'),
        ),
        migrations.AddField(
            model_name='questioncomment',
            name='c_subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='questions.SubjectInfo'),
        ),
        migrations.AddField(
            model_name='questioncomment',
            name='c_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.UserInfo'),
        ),
    ]
