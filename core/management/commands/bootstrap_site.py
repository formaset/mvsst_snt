from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand
from django.db import transaction
from wagtail.models import Collection, GroupCollectionPermission, GroupPagePermission, Page, Site

from awards.models import Award, EvaluationPage
from contacts.models import ContactsPage
from core.models import AboutPage, HomePage
from news.models import NewsIndexPage, NewsPage
from people.models import LeadershipPage, Person


class Command(BaseCommand):
    help = "Создаёт базовую структуру сайта и демонстрационный контент."

    @transaction.atomic
    def handle(self, *args, **options):
        root = Page.get_first_root_node()
        home = HomePage.objects.child_of(root).first()

        if not home:
            home = HomePage(title="Главная", slug="home")
            root.add_child(instance=home)
            home.save_revision().publish()

        Site.objects.update_or_create(
            hostname="localhost",
            defaults={"root_page": home, "is_default_site": True},
        )

        about_page = AboutPage.objects.child_of(home).first()
        if not about_page:
            about_page = AboutPage(title="Об организации", slug="about")
            about_page.values = [
                {
                    "type": "value",
                    "value": {
                        "title": "Качество",
                        "text": "Строим на совесть, соблюдаем технологии и ГОСТы. Отвечаем за результат своим именем.",
                    },
                },
                {
                    "type": "value",
                    "value": {
                        "title": "Сроки",
                        "text": "Ценим ритм мегаполиса и выполняем задачи без простоев и срывов графика.",
                    },
                },
                {
                    "type": "value",
                    "value": {
                        "title": "Безопасность",
                        "text": "Жизнь людей — безусловный приоритет и строгие стандарты охраны труда.",
                    },
                },
                {
                    "type": "value",
                    "value": {
                        "title": "Команда",
                        "text": "Мы — единый механизм, основанный на взаимном уважении и ответственности.",
                    },
                },
            ]
            about_page.directions = [
                {"type": "direction", "value": "Благоустройство улиц и городской инфраструктуры."},
                {"type": "direction", "value": "Сезонные работы и спецпроекты."},
                {"type": "direction", "value": "Капитальный ремонт МКД и объектов образования."},
                {"type": "direction", "value": "Строительство производственных баз."},
            ]
            home.add_child(instance=about_page)
            about_page.save_revision().publish()

        leadership_page = LeadershipPage.objects.child_of(home).first()
        if not leadership_page:
            leadership_page = LeadershipPage(title="Руководство", slug="leadership")
            home.add_child(instance=leadership_page)
            leadership_page.save_revision().publish()

        evaluation_page = EvaluationPage.objects.child_of(home).first()
        if not evaluation_page:
            evaluation_page = EvaluationPage(title="Оценка деятельности организации", slug="evaluation")
            home.add_child(instance=evaluation_page)
            evaluation_page.save_revision().publish()

        news_index = NewsIndexPage.objects.child_of(home).first()
        if not news_index:
            news_index = NewsIndexPage(title="Новости", slug="news")
            home.add_child(instance=news_index)
            news_index.save_revision().publish()

        contacts_page = ContactsPage.objects.child_of(home).first()
        if not contacts_page:
            contacts_page = ContactsPage(
                title="Контакты",
                slug="contacts",
                phone="+7 (495) 000-00-00",
                email="info@mosvodostokstroy.ru",
                legal_address="Москва, ул. Примерная, 1",
                actual_address="Москва, ул. Примерная, 1",
                full_name="АНО по развитию городской среды «МосводостокСтройТрест»",
                short_name="АНО «МосводостокСтройТрест»",
            )
            home.add_child(instance=contacts_page)
            contacts_page.save_revision().publish()

        if not NewsPage.objects.child_of(news_index).exists():
            news_page = NewsPage(
                title="Старт работ по благоустройству квартала",
                slug="start-project",
                lead="Команда «МосводостокСтройТрест» приступила к реализации пилотного проекта в центре Москвы.",
            )
            news_page.body = [
                {
                    "type": "paragraph",
                    "value": {
                        "text": "<p>Проект объединяет модернизацию инженерной инфраструктуры и создание комфортных общественных пространств.</p>",
                    },
                },
                {
                    "type": "quote",
                    "value": {
                        "text": "Работаем в тесном взаимодействии с жителями и городскими службами.",
                        "author": "Пресс-служба",
                    },
                },
                {
                    "type": "key_figure",
                    "value": {"number": "18 га", "caption": "площадь благоустройства"},
                },
            ]
            news_index.add_child(instance=news_page)
            news_page.save_revision().publish()

        if not Person.objects.exists():
            Person.objects.create(
                name="Иванов Иван Иванович",
                position="Генеральный директор",
            )

        if not Award.objects.exists():
            Award.objects.create(
                title="Благодарность за вклад в развитие города",
                description="Отмечаем вклад организации в реализацию городских программ.",
            )

        self.stdout.write(self.style.SUCCESS("Структура сайта и демо-данные созданы."))

        self._ensure_news_editors_group(news_index)

    def _ensure_news_editors_group(self, news_index):
        group, _ = Group.objects.get_or_create(name="Редактор новостей")

        for permission_type in ["add", "edit", "publish"]:
            GroupPagePermission.objects.get_or_create(
                group=group,
                page=news_index,
                permission_type=permission_type,
            )

        root_collection = Collection.get_first_root_node()
        for codename in ["add_image", "change_image", "add_document", "change_document"]:
            perm = Permission.objects.get(codename=codename)
            GroupCollectionPermission.objects.get_or_create(
                group=group,
                collection=root_collection,
                permission=perm,
            )
