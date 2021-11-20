# Generated by Django 3.2.9 on 2021-11-15 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('image', models.FileField(upload_to='post_images/')),
                ('likes', models.IntegerField(default=0)),
            ],
        ),
    ]
