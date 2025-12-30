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
            name="Award",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=255, verbose_name="Название")),
                ("description", models.TextField(blank=True, verbose_name="Описание")),
                (
                    "image",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="award_images",
                        to="wagtailimages.image",
                        verbose_name="Изображение",
                    ),
                ),
            ],
            options={
                "verbose_name": "Награда",
                "verbose_name_plural": "Награды",
            },
        ),
        migrations.CreateModel(
            name="EvaluationPage",
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
                "verbose_name": "Оценка деятельности",
            },
            bases=("wagtailcore.page",),
        ),
    ]
