# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commets',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comments_text', models.TextField()),
            ],
            options={
                'db_table': 'comments',
            },
        ),
        migrations.AlterField(
            model_name='article',
            name='article_likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='commets',
            name='comments_article',
            field=models.ForeignKey(to='article.Article'),
        ),
    ]
