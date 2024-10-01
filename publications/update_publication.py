from .models import Publication
from scholarly import scholarly

GOOGLE_SCHOLAR_ID = 'vcb7qp4AAAAJ'

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
            print(f"Create new publication: {newPublication}")
except Exception as e:
    print(f"Error retrieving publications:")
        