# Generated by Django 5.2 on 2025-04-23 11:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_department_alter_employee_department"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employee",
            name="department",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="employees",
                to="core.department",
            ),
        ),
    ]
