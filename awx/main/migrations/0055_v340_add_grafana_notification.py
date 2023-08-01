# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-01-20 12:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('main', '0054_v340_workflow_convergence'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='notification_type',
            field=models.CharField(
                choices=[
                    ('email', 'Email'),
                    ('slack', 'Slack'),
                    ('twilio', 'Twilio'),
                    ('pagerduty', 'Pagerduty'),
                    ('grafana', 'Grafana'),
                    ('hipchat', 'HipChat'),
                    ('webhook', 'Webhook'),
                    ('mattermost', 'Mattermost'),
                    ('rocketchat', 'Rocket.Chat'),
                    ('irc', 'IRC'),
                ],
                max_length=32,
            ),
        ),
        migrations.AlterField(
            model_name='notificationtemplate',
            name='notification_type',
            field=models.CharField(
                choices=[
                    ('email', 'Email'),
                    ('slack', 'Slack'),
                    ('twilio', 'Twilio'),
                    ('pagerduty', 'Pagerduty'),
                    ('grafana', 'Grafana'),
                    ('hipchat', 'HipChat'),
                    ('webhook', 'Webhook'),
                    ('mattermost', 'Mattermost'),
                    ('rocketchat', 'Rocket.Chat'),
                    ('irc', 'IRC'),
                ],
                max_length=32,
            ),
        ),
    ]
