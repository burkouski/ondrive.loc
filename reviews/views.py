import json
from django.views.decorators.csrf import ensure_csrf_cookie
from django.shortcuts import  HttpResponse
from reviews.models import Review

@ensure_csrf_cookie
def create_review(request):
    if request.method == 'POST':
        post_data = json.loads(request.body)
        author = post_data.get('username', False)
        review = post_data.get('text', False)
        rate = post_data.get('rate', False)
        #author = request.POST['username']
        #review = request.POST['text']
        #rate = request.POST['rate']
        is_moderate = False
        object_id = post_data.get('obj_id', None)
        content_type_id = post_data.get('relate', None)
        review = Review(author=author, review=review, rate=rate, is_moderate=is_moderate, object_id=object_id, content_type_id=content_type_id)
        review.save()
        return HttpResponse('')

