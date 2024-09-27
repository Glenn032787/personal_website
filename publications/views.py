from django.shortcuts import render, redirect
from scholarly import scholarly
from django.core.cache import cache
from django.contrib.auth.decorators import user_passes_test
from .models import Publication

GOOGLE_SCHOLAR_ID = 'vcb7qp4AAAAJ'

# Create your views here.
def index(request):
    publications = Publication.objects.all()
    context = {'publications': publications}
    return render(request, "publications/index.html", context)

def is_admin(user):
    return user.is_superuser

@user_passes_test(is_admin)
def update_database(request):
    try:
        publications = scholarly.fill(scholarly.search_author_id(GOOGLE_SCHOLAR_ID), sections=['publications'])['publications']
        for publication in publications:
            if not Publication.objects.filter(google_scholar_id=publication['author_pub_id']).exists():
                pub = scholarly.fill(publication)
                new_Publication = Publication(
                    title=pub['bib']['title'],
                    abstract=pub['bib']['abstract'],
                    pub_url=pub['pub_url'],
                    pub_year=pub['bib']['pub_year'],
                    citation=pub['bib']['citation'],
                    author=pub['bib']['author'],
                    google_scholar_id=pub['author_pub_id']
                )
                new_Publication.save()
        return redirect('research')
    except Exception as e:
        print(f"Error retrieving publications:")
        return redirect('research')
            