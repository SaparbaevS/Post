# Generated by Django 4.2.3 on 2023-07-14 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=30)),
                ('head', models.TextField()),
                ('text', models.CharField(max_length=30)),
                ('page_layk', models.IntegerField()),
            ],
        ),
    ]
