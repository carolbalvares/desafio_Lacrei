# Generated by Django 5.1.1 on 2024-09-08 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('question', models.TextField(max_length=400)),
                ('priority', models.CharField(choices=[('H', 'high'), ('M', 'medium'), ('L', 'low')], max_length=1)),
            ],
            options={
                'verbose_name': 'The Question',
                'verbose_name_plural': 'Peoples Questions',
            },
        ),
    ]
