# Generated by Django 2.2.5 on 2019-10-21 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catApp', '0003_cat'),
    ]

    operations = [
        migrations.CreateModel(
            name='CatRace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('racers', models.ManyToManyField(related_name='races', to='catApp.Cat')),
                ('winner', models.ForeignKey(null=True, on_delete='CASCADE', related_name='wins', to='catApp.Cat')),
            ],
        ),
    ]
