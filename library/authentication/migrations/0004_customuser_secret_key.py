# Generated by Django 4.1 on 2024-03-14 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_customuser_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='secret_key',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
    ]