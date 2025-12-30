from django.db import models
from django.utils import timezone
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField
from wagtail.models import Page
from wagtail.search import index

from .blocks import (
    CalloutBlock,
    DividerBlock,
    GalleryBlock,
    HeadingBlock,
    ImageBlock,
    KeyFigureBlock,
    ParagraphBlock,
    QuoteBlock,
    VideoBlock,
)


class NewsIndexPage(Page):
    template = "news/news_index_page.html"
    subpage_types = ["news.NewsPage"]

    intro = models.TextField(blank=True, verbose_name="Вводный текст")

    content_panels = Page.content_panels + [FieldPanel("intro")]

    class Meta:
        verbose_name = "Раздел новостей"

    def get_context(self, request):
        context = super().get_context(request)
        news_items = NewsPage.objects.child_of(self).live().order_by("-publish_date")
        page = int(request.GET.get("page", 1))
        per_page = 6
        start = (page - 1) * per_page
        end = start + per_page
        context["news_items"] = news_items[start:end]
        context["page"] = page
        context["has_prev"] = page > 1
        context["has_next"] = news_items.count() > end
        return context


class NewsPage(Page):
    template = "news/news_page.html"
    parent_page_types = ["news.NewsIndexPage"]

    lead = models.TextField(blank=True, verbose_name="Лид")
    publish_date = models.DateField(default=timezone.now, verbose_name="Дата публикации")
    cover_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="news_cover",
        verbose_name="Обложка",
    )
    body = StreamField(
        [
            ("heading", HeadingBlock()),
            ("paragraph", ParagraphBlock()),
            ("image", ImageBlock()),
            ("video", VideoBlock()),
            ("quote", QuoteBlock()),
            ("callout", CalloutBlock()),
            ("divider", DividerBlock()),
            ("key_figure", KeyFigureBlock()),
            ("gallery", GalleryBlock()),
        ],
        use_json_field=True,
        blank=True,
        verbose_name="Контент",
    )

    search_fields = Page.search_fields + [
        index.SearchField("lead"),
        index.SearchField("body"),
    ]

    content_panels = Page.content_panels + [
        FieldPanel("publish_date"),
        FieldPanel("lead"),
        FieldPanel("cover_image"),
        FieldPanel("body"),
    ]

    class Meta:
        verbose_name = "Новость"
