import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_nyt', '0003_subscription'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='subscription',
            field=models.ForeignKey(
                to_field='id',
                to='django_nyt.Subscription',
                blank=True,
                on_delete=django.db.models.deletion.SET_NULL,
                null=True),
            preserve_default=True,
        ),
    ]
