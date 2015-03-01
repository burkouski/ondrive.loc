import json
from django.views.decorators.csrf import ensure_csrf_cookie
from django.shortcuts import  HttpResponse
from reviews.models import Review

@ensure_csrf_cookie
def create_review(request):
    author = request.POST['username']
    review = request.POST['text']
    rate = request.POST['rate']
    is_moderate = False
    object_id = request.POST['obj_id']
    content_type_id = request.POST['relate']
    review = Review(author=author, review=review, rate=rate, is_moderate=is_moderate, object_id=object_id, content_type_id=content_type_id)
    review.save()


    if request.method == 'POST':
        return HttpResponse('')

