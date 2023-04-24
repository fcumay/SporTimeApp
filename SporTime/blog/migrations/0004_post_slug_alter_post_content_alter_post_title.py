# Generated by Django 4.1.7 on 2023-03-28 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(blank=True, help_text='Не более 5000 символов', max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(help_text='Не более 200 символов', max_length=200),
        ),
    ]