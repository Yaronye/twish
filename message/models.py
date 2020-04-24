import uuid
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Secret(models.Model):
    content = models.TextField()                                    # textfield for unrestricted text
    password = models.CharField(max_length=50)
    maxviews = models.IntegerField(default=1)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)     # uuid for a unique url
