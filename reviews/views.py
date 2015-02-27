import json
from django.views.decorators.csrf import ensure_csrf_cookie

@ensure_csrf_cookie
def send_review(request):
    services = AutoService.objects.all()
    obj = {}
    for key in request.POST:
        obj[key[:-2]] = request.POST.getlist(key)

    for key, val in obj.items():
        for x in val:
            services = services.filter(**{key: x})
    services = services.annotate(sort=Avg('reviews__rate')).order_by('-sort')
    services = json.dumps(
        {
        'info': [{
                            'name': o.name,
                            'longitude': o.longitude,
                            'latitude': o.latitude,
                            'logo': o.logo.url,
                            'teaser': o.teaser,
                            'address': o.address,
                            'rating': o.reviews.all().aggregate(Avg('rate'))['rate__avg'],
                            'sort': o.sort,
                            'url': o.get_absolute_url()} for o in services],
        'meta': services.count()
        }),

    if request.method == 'POST':
        return HttpResponse(services)

    return render(request, 'service/list_view.html')
