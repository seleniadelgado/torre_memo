from django.db import models
import uuid
# Create your models here.

class ConnectionMemos(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    connection_id = models.CharField(max_length=9, null=False)
    user_id = models.CharField(max_length=9, null=False)
    memo = models.CharField(max_length=200, null=True, blank=True)
