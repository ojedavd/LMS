# Generated by Django 3.0.5 on 2020-04-28 04:49

import core.courses.models
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teachers', '0001_initial'),
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('slug', models.SlugField(max_length=150)),
                ('code', models.CharField(blank=True, default='08FB7F', max_length=6, verbose_name='Code')),
                ('description', models.TextField()),
                ('students', models.ManyToManyField(to='students.Student')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='teachers.Teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('order', models.PositiveIntegerField(default=1)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('order', models.PositiveIntegerField(default=1)),
                ('type', models.SmallIntegerField(choices=[(1, 'General'), (2, 'Homework'), (2, 'Quiz')], default=1, verbose_name='Type')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Section')),
            ],
        ),
        migrations.CreateModel(
            name='Resources',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resource', models.FileField(upload_to=core.courses.models.get_resource_file_path, verbose_name='File')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Topic')),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('slug', models.SlugField(max_length=150)),
                ('code', models.CharField(max_length=10)),
                ('courses', models.ManyToManyField(to='courses.Course')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Package')),
            ],
        ),
    ]
