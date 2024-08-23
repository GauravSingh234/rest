# Generated by Django 5.0.6 on 2024-08-23 12:40

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('locationid', models.AutoField(primary_key=True, serialize=False)),
                ('locationname', models.CharField(max_length=25)),
                ('CreatedAt', models.DateField(default=django.utils.timezone.now)),
                ('UpdatedAt', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='ThingsToCarry',
            fields=[
                ('ThinksToCarryid', models.AutoField(primary_key=True, serialize=False)),
                ('Description', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Trekcategory',
            fields=[
                ('Trekcategoryid', models.AutoField(primary_key=True, serialize=False)),
                ('TrekCategory', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TrekHeroImages',
            fields=[
                ('TrekHeroImagesid', models.AutoField(primary_key=True, serialize=False)),
                ('Location', models.CharField(choices=[('top', 'Top'), ('left', 'Left'), ('right', 'Right'), ('bottom', 'Bottom')], default='top', max_length=6)),
                ('TrekHeroImagesUrl', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TrekPlan',
            fields=[
                ('TrekPlanID', models.AutoField(primary_key=True, serialize=False)),
                ('Trekid', models.CharField(max_length=100)),
                ('TrekDay', models.CharField(max_length=100)),
                ('TrekPlanTitle', models.CharField(max_length=100)),
                ('TrekplanDescription', models.CharField(max_length=600)),
            ],
        ),
        migrations.CreateModel(
            name='Trek',
            fields=[
                ('Trekid', models.AutoField(primary_key=True, serialize=False)),
                ('RegularPrice', models.DecimalField(decimal_places=2, max_digits=10)),
                ('DicountedPrice', models.DecimalField(decimal_places=2, max_digits=10)),
                ('TotalDuration', models.DecimalField(decimal_places=2, max_digits=10)),
                ('TotalDay', models.IntegerField()),
                ('TotalNight', models.IntegerField()),
                ('TrekHeight', models.DecimalField(decimal_places=2, max_digits=10)),
                ('TrekDistance', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Pickupfrom', models.CharField(max_length=100)),
                ('DropTo', models.CharField(max_length=100)),
                ('Overview', models.CharField(max_length=100, null=True)),
                ('Highlights', models.CharField(max_length=1000)),
                ('TrekGallery', models.ImageField(upload_to='')),
                ('MeetingPoint', models.CharField(max_length=200)),
                ('LocationTag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Location', to='app.location')),
                ('ThingsToCarryid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ThingsToCarry', to='app.thingstocarry')),
                ('Trek_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Trekcategory', to='app.trekcategory')),
                ('TrekHeroImage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='TrekHeroImages', to='app.trekheroimages')),
            ],
        ),
    ]
