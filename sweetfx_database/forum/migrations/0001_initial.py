# Generated by Django 2.2.6 on 2019-10-10 19:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import sweetfx_database.gamedb.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Forum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('updated', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('sorting', models.PositiveIntegerField(db_index=True, default=100)),
                ('threads', models.PositiveIntegerField(default=0)),
                ('slug', models.SlugField()),
            ],
            options={
                'ordering': ['-sorting'],
            },
            bases=(sweetfx_database.gamedb.models.RenderMixin, models.Model),
        ),
        migrations.CreateModel(
            name='ForumPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('ip', models.CharField(blank=True, max_length=200)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ForumThread',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('posts', models.PositiveIntegerField(default=0)),
                ('sorting', models.PositiveIntegerField(db_index=True, default=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('forum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.Forum')),
                ('last_post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='forum.ForumPost')),
            ],
            options={
                'ordering': ['-sorting', '-updated'],
            },
            bases=(sweetfx_database.gamedb.models.RenderMixin, models.Model),
        ),
        migrations.AddField(
            model_name='forumpost',
            name='thread',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.ForumThread'),
        ),
        migrations.AddField(
            model_name='forum',
            name='last_thread',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='forum2', to='forum.ForumThread'),
        ),
        migrations.AddField(
            model_name='forum',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='forum.Forum'),
        ),
    ]
