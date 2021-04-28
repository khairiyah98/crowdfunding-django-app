from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length = 100)
    amt_sought = models.DecimalField(max_digits=8, decimal_places=2,verbose_name='Amount needed for project (SGD)', default = 0)
    amt_raised = models.DecimalField(max_digits=8, decimal_places=2,verbose_name='Amount raised so far (SGD)', default=0)
    post_status = models.CharField(max_length = 70, default = 'Funding needed')
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk': self.pk})