# Generated by Django 3.0.3 on 2020-07-11 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryUrlsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_cat', models.CharField(choices=[('TPS', 'Top Stories'), ('TCH', 'Technology'), ('SPR', 'Sports'), ('BSN', 'Business'), ('ENT', 'Entertainment')], max_length=3, unique=True)),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-updated'],
            },
        ),
        migrations.CreateModel(
            name='NewsSourceModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('code', models.CharField(max_length=3, unique=True)),
                ('top_stories_url', models.URLField()),
                ('sports_url', models.URLField()),
                ('entertainment_url', models.URLField()),
                ('business_url', models.URLField()),
                ('tech_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='UrlModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('keywords', models.TextField(blank=True, null=True)),
                ('summary', models.TextField(blank=True, null=True)),
                ('title', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('news_source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.NewsSourceModel')),
            ],
            options={
                'ordering': ['-updated'],
            },
        ),
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.DeleteModel(
            name='Feed',
        ),
        migrations.AddField(
            model_name='categoryurlsmodel',
            name='urls',
            field=models.ManyToManyField(to='news.UrlModel'),
        ),
    ]