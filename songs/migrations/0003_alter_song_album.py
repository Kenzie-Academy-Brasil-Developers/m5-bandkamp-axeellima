# Generated by Django 4.0.7 on 2022-12-18 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0003_alter_album_user'),
        ('songs', '0002_alter_song_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='album',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='songs', to='albums.album'),
        ),
    ]
