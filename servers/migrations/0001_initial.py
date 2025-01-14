# Generated by Django 3.1.4 on 2020-12-30 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hosts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(blank=True, null=True)),
                ('code', models.CharField(max_length=180)),
                ('name', models.CharField(max_length=180)),
                ('version', models.CharField(blank=True, max_length=255, null=True)),
                ('uptime', models.CharField(blank=True, max_length=255, null=True)),
                ('sessions', models.CharField(blank=True, max_length=255, null=True)),
                ('processes', models.CharField(blank=True, max_length=255, null=True)),
                ('processes_array', models.TextField(blank=True, null=True)),
                ('file_handles', models.CharField(blank=True, max_length=255, null=True)),
                ('file_handles_limit', models.CharField(blank=True, max_length=255, null=True)),
                ('os_kernel', models.CharField(blank=True, max_length=255, null=True)),
                ('os_name', models.CharField(blank=True, max_length=255, null=True)),
                ('os_arch', models.CharField(blank=True, max_length=255, null=True)),
                ('cpu_name', models.CharField(blank=True, max_length=255, null=True)),
                ('cpu_cores', models.CharField(blank=True, max_length=255, null=True)),
                ('cpu_freq', models.CharField(blank=True, max_length=255, null=True)),
                ('ram_total', models.CharField(blank=True, max_length=255, null=True)),
                ('ram_usage', models.CharField(blank=True, max_length=255, null=True)),
                ('swap_total', models.CharField(blank=True, max_length=255, null=True)),
                ('swap_usage', models.CharField(blank=True, max_length=255, null=True)),
                ('disk_array', models.TextField(blank=True, null=True)),
                ('disk_total', models.CharField(blank=True, max_length=255, null=True)),
                ('disk_usage', models.CharField(blank=True, max_length=255, null=True)),
                ('connections', models.CharField(blank=True, max_length=255, null=True)),
                ('nic', models.CharField(blank=True, max_length=255, null=True)),
                ('ipv_4', models.CharField(blank=True, max_length=255, null=True)),
                ('ipv_6', models.CharField(blank=True, max_length=255, null=True)),
                ('rx', models.CharField(blank=True, max_length=255, null=True)),
                ('tx', models.CharField(blank=True, max_length=255, null=True)),
                ('rx_gap', models.CharField(blank=True, max_length=255, null=True)),
                ('tx_gap', models.CharField(blank=True, max_length=255, null=True)),
                ('loads', models.CharField(blank=True, max_length=255, null=True)),
                ('load_cpu', models.CharField(blank=True, max_length=255, null=True)),
                ('load_io', models.CharField(blank=True, max_length=255, null=True)),
                ('ping_eu', models.CharField(blank=True, max_length=255, null=True)),
                ('ping_us', models.CharField(blank=True, max_length=255, null=True)),
                ('ping_as', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'hosts',
                'managed': False,
                'default_permissions': (),
            },
        ),
    ]
