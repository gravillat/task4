# Generated by Django 4.0.5 on 2022-10-19 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='imgpath',
            field=models.ImageField(upload_to='media/images/'),
        ),
        migrations.AlterField(
            model_name='course',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='app.category'),
        ),
        migrations.AlterField(
            model_name='course',
            name='logo',
            field=models.ImageField(upload_to='media/images/'),
        ),
    ]