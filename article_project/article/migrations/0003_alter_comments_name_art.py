# Generated by Django 3.2.6 on 2022-07-06 15:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='name_art',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='name_article', to='article.article', verbose_name='Имя статьи'),
        ),
    ]
