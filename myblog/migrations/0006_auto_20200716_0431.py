# Generated by Django 3.0.7 on 2020-07-16 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0005_auto_20200716_0430'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='author',
            field=models.ManyToManyField(to='myblog.Author'),
        ),
    ]