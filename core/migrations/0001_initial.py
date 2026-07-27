from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grievance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('live_image', models.ImageField(upload_to='complaints/')),
                ('latitude', models.DecimalField(decimal_places=15, max_digits=20)),
                ('longitude', models.DecimalField(decimal_places=15, max_digits=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
