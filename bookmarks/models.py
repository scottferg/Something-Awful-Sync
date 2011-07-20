from django.db import models
from django.contrib.auth.models import User

class Bookmark(models.Model):
    user    = models.ForeignKey(User)
    post_id = models.CharField(max_length = 50)

    def export_to_dict(self):
        return {
            'post_id': self.post_id,
        }

    class Meta:
        unique_together = (
            'user',
            'post_id'
        )
