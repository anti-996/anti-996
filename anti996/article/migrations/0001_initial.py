# Generated by Django 2.1.7 on 2019-03-30 14:55

from django.db import migrations, models
import django.db.models.deletion
import utils.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024)),
                ('slug', models.SlugField(max_length=2048)),
                ('tags', models.CharField(max_length=1024)),
                ('content', models.TextField()),
                ('status', models.IntegerField(choices=[(-1, 'deleted'), (0, 'draft'), (1, 'published'), (2, 'rejected')])),
            ],
            bases=(models.Model, utils.models.AuditMixin),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            bases=(models.Model, utils.models.AuditMixin),
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='article.Category'),
        ),
    ]
