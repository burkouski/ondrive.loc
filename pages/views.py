from django.shortcuts import get_object_or_404,get_list_or_404, render
from pages.models import Page

def get_page(request, page_alias):
    page = get_object_or_404(Page, alias=page_alias)
    args = {'page': page}
    return render(request, 'pages/page_view.html', args)

