from django.db import models
from django.contrib.auth.models import User

# Create your models here.

GENDER_CHOICES = (
    ('male', 'Male'),
    ('female', 'Female'),
    ('third_gender', 'Third Gender'),
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=12, choices=GENDER_CHOICES, null=True)
    image = models.ImageField(default='uploads/default.png', upload_to='uploads/profile_pics')
    date_of_birth = models.DateField(editable=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False, )
    updated_at = models.DateTimeField(auto_now=True, editable=False, )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.user.username} Profile'
