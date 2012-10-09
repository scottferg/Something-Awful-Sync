from piston.handler import BaseHandler
from piston.utils import rc, validate

from models import *
from forms import *

class UserHandler(BaseHandler):
    allowed_methods = ('POST',)

    @validate(CreateUserForm, 'POST')
    def create(self, request):
        User.objects.create_user(request.form.cleaned_data['email'],
                request.form.cleaned_data['email'],
                request.form.cleaned_data['password'])

        return rc.CREATED
        
class SyncV1Handler(BaseHandler):
    allowed_methods = ('GET', 'POST',)
    model = Bookmark

    def read(self, request):
        return [bookmark.export_to_dict() for bookmark in Bookmark.objects.filter(user__pk = request.user.pk)]

    @validate(CreateBookmarkForm, 'POST')
    def create(self, request):
        Bookmark(
            user    = request.user,
            post_id = request.form.cleaned_data['post_id'],
            thread_title = request.form.cleaned_data['thread_title'],
        ).save()

        return rc.CREATED

class SyncByIdV1Handler(BaseHandler):
    allowed_methods = ('GET', 'DELETE',)
    model = Bookmark

    def read(self, request, bookmark_id):
        try:
            return Bookmark.objects.get(pk = bookmark_id).export_to_dict()
        except Bookmark.DoesNotExist:
            return rc.NOT_FOUND

    def delete(self, request, bookmark_id):
        try:
            b = Bookmark.objects.get(pk = bookmark_id).export_to_dict()
            b.delete()

            return rc.DELETED
        except Bookmark.DoesNotExist:
            return rc.NOT_FOUND
