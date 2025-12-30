from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("wagtailcore", "0001_initial"),
        ("wagtailimages", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Person",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=255, verbose_name="ФИО")),
                ("position", models.CharField(max_length=255, verbose_name="Должность")),
                (
                    "photo",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="people_photos",
                        to="wagtailimages.image",
                        verbose_name="Фото",
                    ),
                ),
            ],
            options={
                "verbose_name": "Руководитель",
                "verbose_name_plural": "Руководство",
            },
        ),
        migrations.CreateModel(
            name="LeadershipPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=models.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                ("intro", models.TextField(blank=True, verbose_name="Вводный текст")),
            ],
            options={
                "abstract": False,
                "verbose_name": "Руководство",
            },
            bases=("wagtailcore.page",),
        ),
    ]
