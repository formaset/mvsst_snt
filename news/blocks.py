from wagtail import blocks
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.images.blocks import ImageChooserBlock


class HeadingBlock(blocks.StructBlock):
    text = blocks.CharBlock(label="Заголовок")

    class Meta:
        icon = "title"
        label = "Заголовок"
        template = "news/blocks/heading.html"


class ParagraphBlock(blocks.StructBlock):
    text = blocks.RichTextBlock(label="Текст")

    class Meta:
        icon = "doc-full"
        label = "Абзац"
        template = "news/blocks/paragraph.html"


class ImageBlock(blocks.StructBlock):
    image = ImageChooserBlock(label="Изображение")
    caption = blocks.CharBlock(label="Подпись", required=False)

    class Meta:
        icon = "image"
        label = "Изображение"
        template = "news/blocks/image.html"


class VideoBlock(blocks.StructBlock):
    video = DocumentChooserBlock(label="Видео файл")
    caption = blocks.CharBlock(label="Подпись", required=False)

    class Meta:
        icon = "media"
        label = "Видео"
        template = "news/blocks/video.html"


class QuoteBlock(blocks.StructBlock):
    text = blocks.TextBlock(label="Цитата")
    author = blocks.CharBlock(label="Автор", required=False)

    class Meta:
        icon = "openquote"
        label = "Цитата"
        template = "news/blocks/quote.html"


class CalloutBlock(blocks.StructBlock):
    text = blocks.TextBlock(label="Выделение")

    class Meta:
        icon = "warning"
        label = "Выделение"
        template = "news/blocks/callout.html"


class DividerBlock(blocks.StructBlock):
    class Meta:
        icon = "horizontalrule"
        label = "Разделитель"
        template = "news/blocks/divider.html"


class KeyFigureBlock(blocks.StructBlock):
    number = blocks.CharBlock(label="Число")
    caption = blocks.CharBlock(label="Подпись")

    class Meta:
        icon = "placeholder"
        label = "Ключевая цифра"
        template = "news/blocks/key_figure.html"


class GalleryBlock(blocks.StructBlock):
    images = blocks.ListBlock(ImageChooserBlock(label="Изображение"), label="Галерея")

    class Meta:
        icon = "image"
        label = "Галерея"
        template = "news/blocks/gallery.html"
