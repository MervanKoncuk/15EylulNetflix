# Generated by Django 4.1.3 on 2022-11-22 17:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0005_profile_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='olusturan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='olusturan', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profile',
            name='slug',
            field=models.SlugField(blank=True, editable=False, null=True),
        ),
        migrations.CreateModel(
            name='Hesap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resim', models.FileField(upload_to='hesaplar/')),
                ('tel', models.IntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]