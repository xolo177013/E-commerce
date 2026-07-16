from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=120, unique=True)
    parent = models.ForeignKey(
        'self',
        on_delete = models.CASCADE, #If you delete a parent category, all its children
        null=True,
        blank=True,
        related_name='children'
    )

    class Meta:
        verbose_name_plural='Categories'

    def __str__(self):
        return self.name
    
