# Generated by Django 4.2.1 on 2023-05-16 10:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0003_alter_empresa_options_alter_empresa_table'),
        ('departamentos', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('funcionarios', '0002_rename_funconario_funcionario'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcionario',
            name='departamentos',
            field=models.ManyToManyField(to='departamentos.departamento'),
        ),
        migrations.AddField(
            model_name='funcionario',
            name='empresa',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='empresas.empresa'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='funcionario',
            name='user',
            field=models.OneToOneField(default=16052023, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
