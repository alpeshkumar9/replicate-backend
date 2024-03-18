# Generated by Django 5.0.3 on 2024-03-18 19:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_alter_tags_options_remove_books_descriptiom_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_date', models.DateField(auto_now_add=True, verbose_name='Issue Date')),
                ('due_date', models.DateField(verbose_name='Due Date')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loans', to='books.books')),
                ('reader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_loans', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Book Loan',
                'verbose_name_plural': 'Book Loans',
            },
        ),
    ]