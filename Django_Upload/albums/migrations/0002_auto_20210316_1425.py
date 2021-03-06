# Generated by Django 3.1.7 on 2021-03-16 10:25

import albums.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.FileField(upload_to=albums.models.upload_location)),
            ],
            options={
                'verbose_name': 'FileUpload',
                'verbose_name_plural': 'FildUploads',
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='album',
            name='file',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='albums', to='albums.fileupload', verbose_name='FileUpload'),
        ),
    ]
