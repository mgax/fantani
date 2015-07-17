# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 17, 15, 16, 30, 653285, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
