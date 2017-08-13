# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bb_post', '0002_auto_20150415_1227'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField()),
                ('post', models.ForeignKey(to='bb_post.Post')),
            ],
            options={
                'db_table': 'comment',
            },
            bases=(models.Model,),
        ),
    ]
