# Generated by Django 3.2 on 2022-01-19 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Songs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Track_Name', models.CharField(max_length=100)),
                ('Artist_Name', models.CharField(max_length=50)),
                ('Genre', models.CharField(max_length=50)),
                ('Beats_Per_Minute', models.IntegerField()),
                ('Energy', models.IntegerField()),
                ('Danceability', models.IntegerField()),
                ('Loudness', models.IntegerField()),
                ('Liveness', models.IntegerField()),
                ('Valence', models.IntegerField()),
                ('Length', models.IntegerField()),
                ('Acousticness', models.IntegerField()),
                ('Speechiness', models.IntegerField()),
                ('Popularity', models.IntegerField()),
            ],
        ),
    ]
