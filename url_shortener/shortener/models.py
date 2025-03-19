from django.db import models
import shortuuid
from django.contrib.auth.models import User

class ShortenedURL(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    original_url = models.URLField()
    short_code = models.CharField(max_length=30, unique=True, default=shortuuid.uuid)
    visit_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.short_code

