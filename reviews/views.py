import json
from django.views.decorators.csrf import ensure_csrf_cookie
from django.shortcuts import  HttpResponse
from reviews.models import Review
from reviews.serializers import ReviewSerializer
from rest_framework import generics, permissions
from rest_framework import permissions


class SafeMethodsOnlyPermission(permissions.BasePermission):
    """Only can access non-destructive methods (like GET and HEAD)"""
    def has_permission(self, request, view):
        return self.has_object_permission(request, view)

    def has_object_permission(self, request, view, obj=None):
        return request.method in permissions.SAFE_METHODS


class PostAuthorCanEditPermission(SafeMethodsOnlyPermission):
    """Allow everyone to list or view, but only the other can modify existing instances"""
    def has_object_permission(self, request, view, obj=None):
        if obj is None:
            # Either a list or a create, so no author
            can_edit = True
        else:
            can_edit = request.user == obj.author
        return can_edit or super(PostAuthorCanEditPermission, self).has_object_permission(request, view, obj)

@ensure_csrf_cookie
def create_review(request):
    if request.method == 'POST':
        post_data = json.loads(request.body)
        author = post_data.get('author', False)
        review = post_data.get('review', False)
        rate = post_data.get('rate', False)
        #author = request.POST['username']
        #review = request.POST['text']
        #rate = request.POST['rate']
        is_moderate = False
        object_id = post_data.get('object_id', None)
        content_type_id = post_data.get('content_type_id', None)
        review = Review(author=author, review=review, rate=rate, is_moderate=is_moderate, object_id=object_id, content_type_id=content_type_id)
        review.save()
        return HttpResponse('')


class ReviewList(generics.ListCreateAPIView):
    print '11111111111111111111111'
    serializer_class = ReviewSerializer
    permission_classes = [
        PostAuthorCanEditPermission
    ]
    queryset = Review.objects.all()

