# Generated by Django 5.0.6 on 2024-05-16 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Privacy_Policy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('privacy_policy_pdf_file', models.FileField(blank=True, null=True, upload_to='static/assets/pdfs/')),
            ],
        ),
        migrations.CreateModel(
            name='Terms_of_Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('terms_of_service_pdf_file', models.FileField(blank=True, null=True, upload_to='static/assets/pdfs/')),
            ],
        ),
    ]
