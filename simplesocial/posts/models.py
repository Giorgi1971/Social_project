from django.db import models
# Create your models here.
from django.urls import reverse
from django.conf import settings

# import misaka

from groups.models import Group

from django.contrib.auth import get_user_model 
User = get_user_model()

class Post(models.Model):
    user = models.ForeignKey(User, related_name='posts', on_delete=any)
    created_at = models.DateTimeField(auto_now=True)
    message = models.TextField()
    message_html = models.TextField(editable=False)
    group = models.ForeignKey(Group,related_name='posts', null=True, blank=True, on_delete=any)

    def __str__(self) -> str:
        return self.message

    def save(self, *args, **kwargs):
        self.message_html = "misaka_slung_message"
        # misaka.html(self.message)


    def get_absolute_url(self):
        return reverse('posts:single', kwargs={'username':self.user.username, 'pk':self.user.pk})

    class Meta:
        ordering = ['-created_at']
        unique_together = ['user','message']

