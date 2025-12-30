from news.models import NewsIndexPage
from core.models import AboutPage
from people.models import LeadershipPage
from awards.models import EvaluationPage
from contacts.models import ContactsPage


def site_pages(request):
    return {
        "about_page": AboutPage.objects.live().first(),
        "leadership_page": LeadershipPage.objects.live().first(),
        "evaluation_page": EvaluationPage.objects.live().first(),
        "news_index_page": NewsIndexPage.objects.live().first(),
        "contacts_page": ContactsPage.objects.live().first(),
    }
