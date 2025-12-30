from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.images import get_image_model_string
from wagtail.models import Page
from wagtail.snippets.models import register_snippet


@register_snippet
class Award(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(blank=True, verbose_name="Описание")
    image = models.ForeignKey(
        get_image_model_string(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="award_images",
        verbose_name="Изображение",
    )

    panels = [FieldPanel("title"), FieldPanel("description"), FieldPanel("image")]

    class Meta:
        verbose_name = "Награда"
        verbose_name_plural = "Награды"

    def __str__(self):
        return self.title


class EvaluationPage(Page):
    template = "awards/evaluation_page.html"

    intro = models.TextField(blank=True, verbose_name="Вводный текст")

    content_panels = Page.content_panels + [FieldPanel("intro")]

    class Meta:
        verbose_name = "Оценка деятельности"

    def get_context(self, request):
        context = super().get_context(request)
        context["awards"] = Award.objects.all()
        return context
