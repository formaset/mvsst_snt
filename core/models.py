from django.db import models
from wagtail import blocks
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField
from wagtail.models import Page

from .blocks import (
    HeroBlock,
    CardGridBlock,
    DirectionsBlock,
    LatestNewsBlock,
    RichTextSection,
    SelectedNewsBlock,
    ValuesBlock,
)


class HomePage(Page):
    template = "core/home_page.html"

    body = StreamField(
        [
            ("hero", HeroBlock()),
            ("cards", CardGridBlock()),
            ("rich_text", RichTextSection()),
            ("values", ValuesBlock()),
            ("directions", DirectionsBlock()),
            ("selected_news", SelectedNewsBlock()),
            ("latest_news", LatestNewsBlock()),
        ],
        use_json_field=True,
        blank=True,
        verbose_name="Контент",
    )

    content_panels = Page.content_panels + [FieldPanel("body")]

    def get_context(self, request):
        from news.models import NewsPage

        context = super().get_context(request)
        context["latest_news"] = NewsPage.objects.live().order_by("-publish_date")[:6]
        return context


class AboutPage(Page):
    template = "core/about_page.html"

    intro = models.TextField(
        verbose_name="О компании",
        blank=True,
        default=(
            "Организация основана 1 октября 2024 года единственным учредителем — "
            "ГУП «Мосводосток». Мы — строительный трест, работающий на благо столицы. "
            "Наша деятельность охватывает благоустройство улиц и сезонной инфраструктуры, "
            "капитальный ремонт многоквартирных домов и объектов образования, "
            "строительство производственных баз, а также выполнение специализированных задач "
            "учредителя. В АНО «МосводостокСтройТрест» трудоустроено около 4000 работников."
        ),
    )
    mission = models.TextField(
        verbose_name="Миссия",
        blank=True,
        default=(
            "Создавать комфортную и безопасную городскую среду, "
            "объединяя традиции столичного строительства с современными "
            "технологиями благоустройства для миллионов жителей Москвы."
        ),
    )

    values = StreamField(
        [
            (
                "value",
                blocks.StructBlock(
                    [
                        ("title", blocks.CharBlock(label="Название")),
                        ("text", blocks.TextBlock(label="Описание")),
                    ]
                ),
            )
        ],
        use_json_field=True,
        blank=True,
        verbose_name="Ценности",
    )

    directions = StreamField(
        [("direction", blocks.CharBlock(label="Направление"))],
        use_json_field=True,
        blank=True,
        verbose_name="Направления деятельности",
    )

    body = StreamField(
        [
            ("hero", HeroBlock()),
            ("cards", CardGridBlock()),
            ("rich_text", RichTextSection()),
            ("values", ValuesBlock()),
            ("directions", DirectionsBlock()),
        ],
        use_json_field=True,
        blank=True,
        verbose_name="Дополнительные блоки",
    )

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
        FieldPanel("mission"),
        FieldPanel("values"),
        FieldPanel("directions"),
        FieldPanel("body"),
    ]

    class Meta:
        verbose_name = "Об организации"

    def get_context(self, request):
        from news.models import NewsPage

        context = super().get_context(request)
        context["latest_news"] = NewsPage.objects.live().order_by("-publish_date")[:6]
        return context
