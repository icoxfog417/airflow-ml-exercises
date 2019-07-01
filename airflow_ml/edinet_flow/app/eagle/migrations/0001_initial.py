# Generated by Django 2.2.2 on 2019-07-01 05:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('local_name', models.TextField()),
                ('global_name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period_start', models.DateField(null=True)),
                ('period_end', models.DateField(null=True)),
                ('submitted_date', models.DateTimeField()),
                ('lang', models.CharField(max_length=2)),
                ('path', models.TextField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='eagle.Company')),
            ],
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit', models.CharField(max_length=3)),
                ('ground', models.TextField()),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='eagle.Document')),
            ],
        ),
        migrations.CreateModel(
            name='DummyFeature',
            fields=[
                ('feature_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='eagle.Feature')),
                ('value', models.IntegerField()),
            ],
            bases=('eagle.feature',),
        ),
        migrations.CreateModel(
            name='EDINETCompany',
            fields=[
                ('company_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='eagle.Company')),
                ('jcn', models.CharField(max_length=13)),
                ('edinet_code', models.CharField(max_length=6)),
                ('sec_code', models.CharField(max_length=5, null=True)),
                ('fund_code', models.CharField(max_length=6, null=True)),
            ],
            bases=('eagle.company',),
        ),
        migrations.CreateModel(
            name='NumberOfExecutives',
            fields=[
                ('feature_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='eagle.Feature')),
                ('value', models.IntegerField()),
            ],
            bases=('eagle.feature',),
        ),
        migrations.CreateModel(
            name='EDINETDocument',
            fields=[
                ('document_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='eagle.Document')),
                ('xbrl_path', models.TextField()),
                ('pdf_path', models.TextField()),
                ('edinet_document_id', models.CharField(max_length=8)),
                ('edinet_document_type', models.CharField(max_length=3)),
                ('title', models.TextField()),
                ('ordinance_code', models.CharField(max_length=3)),
                ('form_code', models.CharField(max_length=6)),
                ('issuer_edinet_code', models.CharField(max_length=6, null=True)),
                ('subject_edinet_code', models.CharField(max_length=6, null=True)),
                ('subsidiary_edinet_code', models.CharField(max_length=6, null=True)),
                ('submit_reason', models.TextField(null=True)),
                ('operated_date', models.DateTimeField(null=True)),
                ('withdraw_status', models.CharField(max_length=1)),
                ('operation_status', models.CharField(max_length=1)),
                ('disclosure_status', models.CharField(max_length=1)),
                ('has_attachment', models.BooleanField()),
                ('has_xbrl', models.BooleanField()),
                ('has_pdf', models.BooleanField()),
                ('has_english_doc', models.BooleanField()),
                ('parent_document_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='eagle.EDINETDocument')),
            ],
            bases=('eagle.document',),
        ),
        migrations.CreateModel(
            name='CompanyData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_month', models.DateField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='eagle.Company')),
                ('number_of_executives', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='eagle.NumberOfExecutives')),
            ],
            options={
                'unique_together': {('company', 'year_month')},
            },
        ),
    ]
