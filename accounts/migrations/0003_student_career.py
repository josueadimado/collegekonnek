# Generated by Django 3.0.3 on 2020-04-02 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='career',
            field=models.CharField(max_length=20, null=True),
        ),
    ]