from django.db import migrations, models
from django.utils import timezone
import django.db.models.deletion
import wagtail.fields

import news.blocks


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("wagtailcore", "0001_initial"),
        ("wagtailimages", "0001_initial"),
        ("wagtaildocs", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="NewsIndexPage",
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
                "verbose_name": "Раздел новостей",
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="NewsPage",
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
                ("lead", models.TextField(blank=True, verbose_name="Лид")),
                (
                    "publish_date",
                    models.DateField(default=timezone.now, verbose_name="Дата публикации"),
                ),
                (
                    "cover_image",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="news_cover",
                        to="wagtailimages.image",
                        verbose_name="Обложка",
                    ),
                ),
                (
                    "body",
                    wagtail.fields.StreamField(
                        [
                            ("heading", news.blocks.HeadingBlock()),
                            ("paragraph", news.blocks.ParagraphBlock()),
                            ("image", news.blocks.ImageBlock()),
                            ("video", news.blocks.VideoBlock()),
                            ("quote", news.blocks.QuoteBlock()),
                            ("callout", news.blocks.CalloutBlock()),
                            ("divider", news.blocks.DividerBlock()),
                            ("key_figure", news.blocks.KeyFigureBlock()),
                            ("gallery", news.blocks.GalleryBlock()),
                        ],
                        blank=True,
                        use_json_field=True,
                        verbose_name="Контент",
                    ),
                ),
            ],
            options={
                "abstract": False,
                "verbose_name": "Новость",
            },
            bases=("wagtailcore.page",),
        ),
    ]
