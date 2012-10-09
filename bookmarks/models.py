from django.db import models
from django.contrib.auth.models import User

class Bookmark(models.Model):
    user         = models.ForeignKey(User)
    post_id      = models.CharField(max_length = 50)
    thread_title = models.CharField(max_length = 500)

    def export_to_dict(self):
        return {
            'id': self.pk,
            'post_id': self.post_id,
            'thread_title': self.thread_title,
        }

    class Meta:
        unique_together = (
            'user',
            'post_id'
        )
