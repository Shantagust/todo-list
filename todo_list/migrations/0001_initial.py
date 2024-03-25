# Generated by Django 4.2.11 on 2024-03-25 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('deadline_date', models.DateField(blank=True, null=True)),
                ('is_done', models.BooleanField(default=False)),
                ('tag', models.ManyToManyField(related_name='tasks', to='todo_list.tag')),
            ],
        ),
    ]
