# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('article_tittle', models.CharField(max_length=200)),
                ('article_date', models.DateTimeField()),
                ('article_text', models.TextField()),
                ('article_likes', models.IntegerField()),
            ],
            options={
                'db_table': 'article',
            },
        ),
    ]
