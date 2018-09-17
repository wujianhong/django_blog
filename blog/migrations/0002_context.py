# Generated by Django 2.1.1 on 2018-09-17 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Context',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('context', models.CharField(max_length=1000)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_context', to='blog.Blog')),
            ],
            options={
                'verbose_name_plural': 'Context',
            },
        ),
    ]
