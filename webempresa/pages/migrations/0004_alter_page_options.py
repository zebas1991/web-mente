# Generated by Django 5.0.6 on 2024-07-25 19:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_alter_page_options_alter_page_content'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='page',
            options={'ordering': ['order', 'title'], 'verbose_name': 'Página', 'verbose_name_plural': 'Páginas'},
        ),
    ]