from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.images import get_image_model_string
from wagtail.models import Page
from wagtail.snippets.models import register_snippet


@register_snippet
class Person(models.Model):
    name = models.CharField(max_length=255, verbose_name="ФИО")
    position = models.CharField(max_length=255, verbose_name="Должность")
    photo = models.ForeignKey(
        get_image_model_string(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="people_photos",
        verbose_name="Фото",
    )

    panels = [FieldPanel("name"), FieldPanel("position"), FieldPanel("photo")]

    class Meta:
        verbose_name = "Руководитель"
        verbose_name_plural = "Руководство"

    def __str__(self):
        return self.name


class LeadershipPage(Page):
    template = "people/leadership_page.html"

    intro = models.TextField(blank=True, verbose_name="Вводный текст")

    content_panels = Page.content_panels + [FieldPanel("intro")]

    class Meta:
        verbose_name = "Руководство"

    def get_context(self, request):
        context = super().get_context(request)
        context["leaders"] = Person.objects.all()
        return context
