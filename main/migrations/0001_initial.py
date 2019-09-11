# Generated by Django 2.2.4 on 2019-09-11 04:56

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
                ('ticker', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('sector', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Summary',
            fields=[
                ('ticker_date', models.CharField(max_length=13, primary_key=True, serialize=False)),
                ('date', models.DateTimeField(verbose_name='Date Scraped')),
                ('market_cap', models.BigIntegerField()),
                ('risk', models.DecimalField(decimal_places=2, max_digits=5)),
                ('debt_equity_index', models.DecimalField(decimal_places=2, max_digits=5)),
                ('net_dividend_yield_index', models.DecimalField(decimal_places=2, max_digits=5)),
                ('sharpe_ratio_index', models.DecimalField(decimal_places=2, max_digits=5)),
                ('return_on_equity_index', models.DecimalField(decimal_places=2, max_digits=5)),
                ('score', models.SmallIntegerField()),
                ('ticker', models.ForeignKey(db_column='ticker', on_delete=django.db.models.deletion.CASCADE, to='main.Company')),
            ],
        ),
        migrations.CreateModel(
            name='Ratios',
            fields=[
                ('ticker_date', models.CharField(max_length=13, primary_key=True, serialize=False)),
                ('date', models.DateTimeField(verbose_name='Date Scraped')),
                ('ePS', models.FloatField()),
                ('nTA', models.FloatField()),
                ('net_DPS', models.FloatField()),
                ('gross_DPS', models.FloatField()),
                ('beta_Value', models.FloatField()),
                ('price_NTA', models.FloatField()),
                ('net_Yield', models.FloatField()),
                ('gross_Yield', models.FloatField()),
                ('sharpe', models.FloatField()),
                ('debt_Equity', models.FloatField()),
                ('return_On_Equity', models.FloatField()),
                ('ticker', models.ForeignKey(db_column='ticker', on_delete=django.db.models.deletion.CASCADE, to='main.Company')),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('date', models.DateTimeField(verbose_name='Date Scraped')),
                ('ticker_date', models.CharField(max_length=13, primary_key=True, serialize=False)),
                ('price', models.FloatField()),
                ('capital_adjusted', models.FloatField()),
                ('volume_traded', models.FloatField()),
                ('value_traded', models.FloatField()),
                ('number_of_trades', models.FloatField()),
                ('price_change', models.FloatField()),
                ('ticker', models.ForeignKey(db_column='ticker', on_delete=django.db.models.deletion.CASCADE, to='main.Company')),
            ],
        ),
        migrations.CreateModel(
            name='Liabilities',
            fields=[
                ('year', models.DateTimeField(verbose_name='Date Scraped')),
                ('ticker_year', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('payables', models.FloatField()),
                ('current_debt', models.FloatField()),
                ('current_liabilities', models.FloatField()),
                ('long_term_debt', models.FloatField()),
                ('deferred_tax_liabilities', models.FloatField()),
                ('other_NC_liabilities', models.FloatField()),
                ('NC_liability', models.FloatField()),
                ('total_liability', models.FloatField()),
                ('ticker', models.ForeignKey(db_column='ticker', on_delete=django.db.models.deletion.CASCADE, to='main.Company')),
            ],
        ),
        migrations.CreateModel(
            name='IncomeStatement',
            fields=[
                ('year', models.DateTimeField(verbose_name='Date Scraped')),
                ('ticker_year', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('sales_revenue', models.FloatField()),
                ('investment_revenue', models.FloatField()),
                ('total_core_revenue', models.FloatField()),
                ('EB17DA', models.FloatField()),
                ('depreciation', models.FloatField()),
                ('EBIT', models.FloatField()),
                ('interest_expense', models.FloatField()),
                ('PBT', models.FloatField()),
                ('income_tax_expense', models.FloatField()),
                ('continuing_operations', models.FloatField()),
                ('MIE', models.FloatField()),
                ('net_income', models.FloatField()),
                ('basic_eps', models.FloatField()),
                ('diluted_eps', models.FloatField()),
                ('ticker', models.ForeignKey(db_column='ticker', on_delete=django.db.models.deletion.CASCADE, to='main.Company')),
            ],
        ),
        migrations.CreateModel(
            name='Equity',
            fields=[
                ('year', models.DateTimeField(verbose_name='Date Scraped')),
                ('ticker_year', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('paid_in_capital', models.FloatField()),
                ('reatained_earnings', models.FloatField()),
                ('minority_interest', models.FloatField()),
                ('other_equity', models.FloatField()),
                ('total_equity', models.FloatField()),
                ('ticker', models.ForeignKey(db_column='ticker', on_delete=django.db.models.deletion.CASCADE, to='main.Company')),
            ],
        ),
        migrations.CreateModel(
            name='Dividends',
            fields=[
                ('ticker_date', models.CharField(max_length=13, primary_key=True, serialize=False)),
                ('date', models.DateTimeField(verbose_name='Date Scraped')),
                ('dividends', models.FloatField()),
                ('ticker', models.ForeignKey(db_column='ticker', on_delete=django.db.models.deletion.CASCADE, to='main.Company')),
            ],
        ),
        migrations.CreateModel(
            name='Directors',
            fields=[
                ('date', models.DateTimeField(verbose_name='Date Scraped')),
                ('name_date', models.CharField(max_length=99, primary_key=True, serialize=False)),
                ('director_name', models.CharField(max_length=100)),
                ('director_role', models.CharField(max_length=100)),
                ('ticker', models.ForeignKey(db_column='ticker', on_delete=django.db.models.deletion.CASCADE, to='main.Company')),
            ],
        ),
        migrations.CreateModel(
            name='CompanyProfile',
            fields=[
                ('date', models.DateTimeField(verbose_name='Date Scraped')),
                ('ticker_date', models.CharField(max_length=13, primary_key=True, serialize=False)),
                ('overview', models.TextField()),
                ('performance', models.TextField()),
                ('outlook', models.TextField()),
                ('description', models.TextField()),
                ('ticker', models.ForeignKey(db_column='ticker', on_delete=django.db.models.deletion.CASCADE, to='main.Company')),
            ],
        ),
        migrations.CreateModel(
            name='CashTable',
            fields=[
                ('year', models.DateTimeField(verbose_name='Date Scraped')),
                ('ticker_year', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('operating', models.FloatField()),
                ('investing', models.FloatField()),
                ('finance', models.FloatField()),
                ('net_change', models.FloatField()),
                ('ticker', models.ForeignKey(db_column='ticker', on_delete=django.db.models.deletion.CASCADE, to='main.Company')),
            ],
        ),
        migrations.CreateModel(
            name='Assets',
            fields=[
                ('year', models.DateTimeField(verbose_name='Date Scraped')),
                ('ticker_year', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('cash_equity', models.FloatField()),
                ('NTR', models.FloatField()),
                ('current_inventory', models.FloatField()),
                ('other_CA', models.FloatField()),
                ('PPE', models.FloatField()),
                ('intangible_assests', models.FloatField()),
                ('LT_investments', models.FloatField()),
                ('LT_deferred_assets', models.FloatField()),
                ('other_NCA', models.FloatField()),
                ('current_assets', models.FloatField()),
                ('NC_assets', models.FloatField()),
                ('total_assets', models.FloatField()),
                ('ticker', models.ForeignKey(db_column='ticker', on_delete=django.db.models.deletion.CASCADE, to='main.Company')),
            ],
        ),
    ]
