# Generated by Django 5.1.5 on 2025-02-27 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scanpipe', '0068_rename_discovered_dependencies_attribute'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='purl',
            field=models.CharField(blank=True, help_text="Package URL (PURL) for the project, required for pushing the project's scan result to FederatedCode. For example, if the input is an input URL like https://registry.npmjs.org/lodash/-/lodash-4.17.21.tgz, the corresponding PURL would be pkg:npm/lodash@4.17.21.", max_length=2048),
        ),
    ]
