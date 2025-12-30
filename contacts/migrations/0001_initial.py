from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("wagtailcore", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ContactsPage",
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
                ("phone", models.CharField(blank=True, max_length=50, verbose_name="Телефон")),
                ("email", models.EmailField(blank=True, max_length=254, verbose_name="Email")),
                ("legal_address", models.CharField(blank=True, max_length=255, verbose_name="Юридический адрес")),
                ("actual_address", models.CharField(blank=True, max_length=255, verbose_name="Фактический адрес")),
                (
                    "work_hours",
                    models.CharField(
                        blank=True,
                        default="ПН–ЧТ 08:00–17:00, ПТ 08:00–16:00, перерыв 12:00–13:00",
                        max_length=255,
                        verbose_name="График работы",
                    ),
                ),
                ("full_name", models.CharField(blank=True, max_length=255, verbose_name="Полное наименование")),
                ("short_name", models.CharField(blank=True, max_length=255, verbose_name="Сокращенное наименование")),
                (
                    "yandex_map_embed",
                    models.TextField(
                        blank=True,
                        help_text="Вставьте URL или iframe с Яндекс.Карт.",
                        verbose_name="Yandex Maps embed URL или iframe",
                    ),
                ),
            ],
            options={
                "abstract": False,
                "verbose_name": "Контакты",
            },
            bases=("wagtailcore.page",),
        ),
    ]
