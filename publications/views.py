from django.shortcuts import render
from scholarly import scholarly
from django.core.cache import cache

GOOGLE_SCHOLAR_ID = 'vcb7qp4AAAAJ'

def get_publications(google_scholar_id):
    publications_cache = cache.get('publications_data')
    if not publications_cache:
        try:
            publications = scholarly.fill(scholarly.search_author_id(GOOGLE_SCHOLAR_ID), sections=['publications'])['publications']
            publications_cache = []
            for publication in publications:
                pub = scholarly.fill(publication)
                bib = pub['bib']
                url = pub['pub_url']
                bib['pub_url'] = url
                publications_cache.append(bib)
            cache.set('publications_data', publications_cache, timeout=3600) 
        except Exception as e:
                print(f"Error retrieving publications:")
                publications_cache = []  
    return publications_cache


# Create your views here.
def index(request):
    publication_data = get_publications('vcb7qp4AAAAJ')

    context = {
        'publications': publication_data
    }

    return render(request, "publications/index.html", context)