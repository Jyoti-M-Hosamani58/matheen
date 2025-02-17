# Generated by Django 3.0 on 2024-12-09 19:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('consign_app', '0012_auto_20241210_0058'),
    ]

    operations = [
        migrations.AddField(
            model_name='fullload',
            name='haltAmt',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='balance',
            name='full_load',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='balances', to='consign_app.Fullload'),
        ),
    ]
