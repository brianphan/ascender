# Generated by Django 4.2.3 on 2023-08-04 20:50

import django.core.validators
from django.db import migrations, models
from django.conf import settings


def automatically_peer_from_control_plane(apps, schema_editor):
    if settings.IS_K8S:
        Instance = apps.get_model('main', 'Instance')
        Instance.objects.filter(node_type='execution').update(peers_from_control_nodes=True)
        Instance.objects.filter(node_type='control').update(listener_port=None)


class Migration(migrations.Migration):
    dependencies = [
        ('main', '0186a_disable_NEXT_UI'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='instancelink',
            options={'ordering': ('id',)},
        ),
        migrations.AddField(
            model_name='instance',
            name='peers_from_control_nodes',
            field=models.BooleanField(default=False, help_text='If True, control plane cluster nodes should automatically peer to it.'),
        ),
        migrations.AlterField(
            model_name='instance',
            name='ip_address',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='instance',
            name='listener_port',
            field=models.PositiveIntegerField(
                blank=True,
                default=None,
                help_text='Port that Receptor will listen for incoming connections on.',
                null=True,
                validators=[django.core.validators.MinValueValidator(1024), django.core.validators.MaxValueValidator(65535)],
            ),
        ),
        migrations.AlterField(
            model_name='instance',
            name='peers',
            field=models.ManyToManyField(related_name='peers_from', through='main.InstanceLink', to='main.instance'),
        ),
        migrations.AlterField(
            model_name='instancelink',
            name='link_state',
            field=models.CharField(
                choices=[('adding', 'Adding'), ('established', 'Established'), ('removing', 'Removing')],
                default='adding',
                help_text='Indicates the current life cycle stage of this peer link.',
                max_length=16,
            ),
        ),
        migrations.AddConstraint(
            model_name='instance',
            constraint=models.UniqueConstraint(
                condition=models.Q(('ip_address', ''), _negated=True),
                fields=('ip_address',),
                name='unique_ip_address_not_empty',
                violation_error_message='Field ip_address must be unique.',
            ),
        ),
        migrations.AddConstraint(
            model_name='instancelink',
            constraint=models.CheckConstraint(check=models.Q(('source', models.F('target')), _negated=True), name='source_and_target_can_not_be_equal'),
        ),
        migrations.RunPython(automatically_peer_from_control_plane),
    ]
