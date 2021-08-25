# Generated by Django 3.2.6 on 2021-08-21 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0003_food_type_food'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='type_food',
            field=models.CharField(choices=[('breakfast', 'صبحانه'), ('drinks', 'نوشیدنی'), ('dinner', 'شام'), ('lunch', 'ناهار')], default='drinks', max_length=10, verbose_name='نوع غذا'),
        ),
    ]
