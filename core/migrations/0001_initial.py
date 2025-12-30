from django.db import migrations, models
import wagtail.fields
from wagtail import blocks as wagtail_blocks

import core.blocks


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("wagtailcore", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="HomePage",
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
                (
                    "body",
                    wagtail.fields.StreamField(
                        [
                            ("hero", core.blocks.HeroBlock()),
                            ("cards", core.blocks.CardGridBlock()),
                            ("rich_text", core.blocks.RichTextSection()),
                            ("values", core.blocks.ValuesBlock()),
                            ("directions", core.blocks.DirectionsBlock()),
                            ("selected_news", core.blocks.SelectedNewsBlock()),
                            ("latest_news", core.blocks.LatestNewsBlock()),
                        ],
                        blank=True,
                        use_json_field=True,
                        verbose_name="Контент",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="AboutPage",
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
                (
                    "intro",
                    models.TextField(
                        blank=True,
                        default=(
                            "Организация основана 1 октября 2024 года единственным учредителем — "
                            "ГУП «Мосводосток». Мы — строительный трест, работающий на благо столицы. "
                            "Наша деятельность охватывает благоустройство улиц и сезонной инфраструктуры, "
                            "капитальный ремонт многоквартирных домов и объектов образования, "
                            "строительство производственных баз, а также выполнение специализированных задач "
                            "учредителя. В АНО «МосводостокСтройТрест» трудоустроено около 4000 работников."
                        ),
                        verbose_name="О компании",
                    ),
                ),
                (
                    "mission",
                    models.TextField(
                        blank=True,
                        default=(
                            "Создавать комфортную и безопасную городскую среду, "
                            "объединяя традиции столичного строительства с современными "
                            "технологиями благоустройства для миллионов жителей Москвы."
                        ),
                        verbose_name="Миссия",
                    ),
                ),
                (
                    "values",
                    wagtail.fields.StreamField(
                        [
                            (
                                "value",
                                wagtail_blocks.StructBlock(
                                    [
                                        ("title", wagtail_blocks.CharBlock(label="Название")),
                                        ("text", wagtail_blocks.TextBlock(label="Описание")),
                                    ]
                                ),
                            )
                        ],
                        blank=True,
                        use_json_field=True,
                        verbose_name="Ценности",
                    ),
                ),
                (
                    "directions",
                    wagtail.fields.StreamField(
                        [("direction", wagtail_blocks.CharBlock(label="Направление"))],
                        blank=True,
                        use_json_field=True,
                        verbose_name="Направления деятельности",
                    ),
                ),
                (
                    "body",
                    wagtail.fields.StreamField(
                        [
                            ("hero", core.blocks.HeroBlock()),
                            ("cards", core.blocks.CardGridBlock()),
                            ("rich_text", core.blocks.RichTextSection()),
                            ("values", core.blocks.ValuesBlock()),
                            ("directions", core.blocks.DirectionsBlock()),
                        ],
                        blank=True,
                        use_json_field=True,
                        verbose_name="Дополнительные блоки",
                    ),
                ),
            ],
            options={
                "abstract": False,
                "verbose_name": "Об организации",
            },
            bases=("wagtailcore.page",),
        ),
    ]
