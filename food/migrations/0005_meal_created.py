# Generated by Django 3.0.8 on 2020-07-10 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0004_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]