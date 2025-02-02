# Generated by Django 5.1.4 on 2025-01-25 11:21

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veggiecart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserWallet',
            fields=[
                ('w_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('w_balance', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('w_points', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('w_commission', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('w_status', models.CharField(choices=[('ACTIVE', 'ACTIVE'), ('INACTIVE', 'INACTIVE'), ('BANNED', 'BANNED')], default='ACTIVE', max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
