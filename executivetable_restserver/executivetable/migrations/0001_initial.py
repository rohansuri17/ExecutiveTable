# Generated by Django 3.0.6 on 2020-05-20 23:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Connection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Startup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=45)),
                ('last_name', models.CharField(max_length=45)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('password_digest', models.CharField(max_length=255)),
                ('startup_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='executivetable.Startup')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True)),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='executivetable.User')),
            ],
        ),
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=45)),
                ('description', models.TextField(blank=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(null=True)),
                ('user_profile_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='executivetable.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='StartupRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=45)),
                ('description', models.TextField()),
                ('is_startup_owner', models.BooleanField(default=False)),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='executivetable.User')),
            ],
        ),
        migrations.CreateModel(
            name='StartupProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True)),
                ('startup_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='executivetable.Startup')),
            ],
        ),
        migrations.CreateModel(
            name='PrivateMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('connection_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='executivetable.Connection')),
                ('startup_receiver_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='startup_receiver_id', to='executivetable.Startup')),
                ('startup_sender_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='startup_sender_id', to='executivetable.Startup')),
                ('user_receiver_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_receiver_id', to='executivetable.User')),
                ('user_sender_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_sender_id', to='executivetable.User')),
            ],
        ),
        migrations.CreateModel(
            name='MessageBoard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('user_message_board_id', models.ManyToManyField(to='executivetable.User')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution', models.CharField(max_length=255)),
                ('education_level', models.CharField(blank=True, max_length=255)),
                ('major', models.CharField(blank=True, max_length=255)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(null=True)),
                ('user_profile_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='executivetable.UserProfile')),
            ],
        ),
        migrations.AddField(
            model_name='connection',
            name='action_user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='action_user_id', to='executivetable.User'),
        ),
        migrations.AddField(
            model_name='connection',
            name='user1_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_1', to='executivetable.User'),
        ),
        migrations.AddField(
            model_name='connection',
            name='user2_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_2', to='executivetable.User'),
        ),
    ]
