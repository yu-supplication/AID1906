# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-08-05 02:58
from __future__ import unicode_literals

import deploy.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deploy', '0003_auto_20190805_0957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moduleattchment',
            name='attchment',
            field=models.FileField(blank=True, null=True, storage=deploy.storage.FileStorage(), upload_to='salt/module/758UWJ7cGTkHPQqv7qlhJrTLjbwruaJMtygH3UqCGjDMapJLJHxk6spaFV59CmmxubLQryE4Abf8LLk5', verbose_name='\u6a21\u5757\u4e0a\u4f20'),
        ),
    ]