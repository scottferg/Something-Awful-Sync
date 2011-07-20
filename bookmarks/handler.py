from piston.handler import BaseHandler
from piston.utils import rc, validate

from models import *
from forms import *

class SyncV1Handler(BaseHandler):
    allowed_methods = ('GET', 'POST', 'DELETE',)
    model = Bookmark

    def read(self, request, bookmark_id):
        try:
            return Bookmark.objects.get(pk = bookmark_id).export_to_dict()
        except Bookmark.DoesNotExist:
            return rc.NOT_FOUND

    def read(self, request):
        return [bookmark.export_to_dict() for bookmark in Bookmark.objects.filter(user__pk = request.user.pk)]

    @validate(CreateBookmarkForm, 'POST')
    def create(self, request):
        Bookmark(
            user    = request.user,
            post_id = request.form.cleaned_data['post_id'],
        ).save()

        return rc.CREATED
