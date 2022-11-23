from PIL import Image
from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):
    user_follower = models.ForeignKey('Profile', related_name='rel_follower_set', on_delete=models.CASCADE)
    user_followed = models.ForeignKey('Profile', related_name='rel_followed_set', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self) -> str:
        return f'{self.user_follower} follows {self.user_followed}'


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='photo3.jpg', upload_to='profiles/')
    phone = models.CharField(max_length=20, verbose_name='phone number', unique=True, null=True, blank=True)
    following = models.ManyToManyField('self', through=Contact, related_name='followers', symmetrical=False, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        image = Image.open(self.image.path)
        if image.width > 250 or image.height > 250:
            output_size = (250, 250)
            image.thumbnail(output_size)
            image.save(self.image.path)