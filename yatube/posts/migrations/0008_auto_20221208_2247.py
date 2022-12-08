# Generated by Django 2.2.16 on 2022-12-08 15:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_auto_20221208_1615'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='follow',
            options={'ordering': ('-author',), 'verbose_name': 'Лента автора', 'verbose_name_plural': 'Лента авторов'},
        ),
        migrations.RemoveConstraint(
            model_name='follow',
            name='unique_follows',
        ),
        migrations.RemoveConstraint(
            model_name='follow',
            name='you cannot follow yourself',
        ),
        migrations.AlterField(
            model_name='follow',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following', to=settings.AUTH_USER_MODEL, verbose_name='Автор поста'),
        ),
        migrations.AlterField(
            model_name='follow',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follower', to=settings.AUTH_USER_MODEL, verbose_name='Подписчик'),
        ),
    ]