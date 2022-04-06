# Generated by Django 3.2.4 on 2021-06-09 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210609_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='rate',
            field=models.IntegerField(default=0, verbose_name=range(0, 5)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='reply_comment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.comment'),
        ),
    ]
