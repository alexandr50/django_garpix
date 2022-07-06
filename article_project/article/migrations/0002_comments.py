# Generated by Django 3.2.6 on 2022-07-06 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=50)),
                ('text', models.TextField(max_length=1000)),
                ('name_art', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='name_article', to='article.article', verbose_name='Имя статьи')),
            ],
        ),
    ]
