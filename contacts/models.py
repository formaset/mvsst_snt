from urllib.parse import urlparse

from django.core.exceptions import ValidationError
from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.models import Page


class ContactsPage(Page):
    template = "contacts/contacts_page.html"

    phone = models.CharField(max_length=50, blank=True, verbose_name="Телефон")
    email = models.EmailField(blank=True, verbose_name="Email")
    legal_address = models.CharField(max_length=255, blank=True, verbose_name="Юридический адрес")
    actual_address = models.CharField(max_length=255, blank=True, verbose_name="Фактический адрес")
    work_hours = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="График работы",
        default="ПН–ЧТ 08:00–17:00, ПТ 08:00–16:00, перерыв 12:00–13:00",
    )
    full_name = models.CharField(max_length=255, blank=True, verbose_name="Полное наименование")
    short_name = models.CharField(max_length=255, blank=True, verbose_name="Сокращенное наименование")
    yandex_map_embed = models.TextField(
        blank=True,
        verbose_name="Yandex Maps embed URL или iframe",
        help_text="Вставьте URL или iframe с Яндекс.Карт.",
    )

    content_panels = Page.content_panels + [
        FieldPanel("phone"),
        FieldPanel("email"),
        FieldPanel("legal_address"),
        FieldPanel("actual_address"),
        FieldPanel("work_hours"),
        FieldPanel("full_name"),
        FieldPanel("short_name"),
        FieldPanel("yandex_map_embed"),
    ]

    class Meta:
        verbose_name = "Контакты"

    def clean(self):
        super().clean()
        if not self.yandex_map_embed:
            return
        url = self.extract_yandex_url()
        if not url:
            raise ValidationError({"yandex_map_embed": "Укажите корректный URL или iframe Яндекс.Карт."})
        parsed = urlparse(url)
        if not parsed.netloc.endswith("yandex.ru") and not parsed.netloc.endswith("yandex.com"):
            raise ValidationError({"yandex_map_embed": "Разрешены только ссылки Яндекс.Карт."})

    def extract_yandex_url(self):
        value = self.yandex_map_embed.strip()
        if value.startswith("<iframe"):
            start = value.find("src=")
            if start == -1:
                return ""
            quote = value[start + 4]
            if quote not in {'"', "'"}:
                return ""
            end = value.find(quote, start + 5)
            return value[start + 5 : end]
        return value

    def yandex_embed_src(self):
        return self.extract_yandex_url()
