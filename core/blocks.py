from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock


class HeroBlock(blocks.StructBlock):
    title = blocks.CharBlock(label="Заголовок", required=True)
    text = blocks.TextBlock(label="Текст", required=False)
    image = ImageChooserBlock(label="Изображение", required=False)

    class Meta:
        icon = "image"
        label = "Hero"
        template = "core/blocks/hero.html"


class CardBlock(blocks.StructBlock):
    title = blocks.CharBlock(label="Заголовок")
    text = blocks.TextBlock(label="Описание", required=False)
    image = ImageChooserBlock(label="Изображение", required=False)


class CardGridBlock(blocks.StructBlock):
    heading = blocks.CharBlock(label="Заголовок блока", required=False)
    cards = blocks.ListBlock(CardBlock(), label="Карточки")

    class Meta:
        icon = "doc-full"
        label = "Карточки"
        template = "core/blocks/card_grid.html"


class ValueItemBlock(blocks.StructBlock):
    title = blocks.CharBlock(label="Название")
    text = blocks.TextBlock(label="Описание")


class ValuesBlock(blocks.StructBlock):
    heading = blocks.CharBlock(label="Заголовок блока", required=False)
    items = blocks.ListBlock(ValueItemBlock(), label="Ценности")

    class Meta:
        icon = "list-ul"
        label = "Ценности"
        template = "core/blocks/values.html"


class DirectionsBlock(blocks.StructBlock):
    heading = blocks.CharBlock(label="Заголовок блока", required=False)
    items = blocks.ListBlock(blocks.CharBlock(label="Направление"), label="Направления")

    class Meta:
        icon = "list-ol"
        label = "Направления деятельности"
        template = "core/blocks/directions.html"


class SelectedNewsBlock(blocks.StructBlock):
    heading = blocks.CharBlock(label="Заголовок блока", required=False)
    news = blocks.ListBlock(
        blocks.PageChooserBlock(page_type=["news.NewsPage"], label="Новость"),
        label="Выбранные новости",
    )

    class Meta:
        icon = "doc-full"
        label = "Выбранные новости"
        template = "core/blocks/selected_news.html"


class LatestNewsBlock(blocks.StructBlock):
    heading = blocks.CharBlock(label="Заголовок блока", required=False)
    limit = blocks.IntegerBlock(label="Сколько новостей показать", default=3)

    class Meta:
        icon = "date"
        label = "Последние новости"
        template = "core/blocks/latest_news.html"


class RichTextSection(blocks.StructBlock):
    heading = blocks.CharBlock(label="Заголовок", required=False)
    body = blocks.RichTextBlock(label="Текст")

    class Meta:
        icon = "doc-full-inverse"
        label = "Rich text"
        template = "core/blocks/rich_text_section.html"
