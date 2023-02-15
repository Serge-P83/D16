# Generated by Django 4.0.5 on 2022-09-05 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal_news', '0003_rename_date_post_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='text_comment',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='select_choices',
            field=models.CharField(choices=[('AR', 'Статья'), ('NE', 'Новость')], max_length=2),
        ),
    ]