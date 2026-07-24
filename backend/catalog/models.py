from django.db import models
from accounts.models import CustomUser

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
    


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products')
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True)
    description = models.TextField(blank = True)
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ProductVariant(models.Model):
    SIZE_CHOICES = [
        ('XS', 'Extra Small'),
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
        ('XXL', 'Double Extra Large'),
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='variants')
    size = models.CharField(max_length=5, choices=SIZE_CHOICES)
    color = models.CharField(max_length=50)
    sku = models.CharField(max_length=50, unique=True)
    price_override = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    stock_quantity = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ('product', 'size', 'color')

    def __str__(self):
        return f"{self.product.name} - {self.size} / {self.color}"
    

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products/')
    alt_text = models.CharField(max_length=150, blank=True)
    is_primary = models.BooleanField(default=False)

    def __str__(self):
        return f"Image of {self.product.name}"
    
# class ProductReview(models.Model):
#     RATING_CHOICES = [
#         (1, "*"),
#         (2, "* *"),
#         (3, "* * *"),
#         (4, "* * * *"),
#         (5, "* * * * *"),
#     ]

#     user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name='reviews')
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
#     text = models.TextField(blank=False)
#     rating =models.PositiveSmallIntegerField(choices=RATING_CHOICES)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         constraints = [
#             models.UniqueConstraint(
#                 fields=["user", "product"],
#                 name="unique_review"
#             )
#         ]

#     def __str__(self):
#         user = self.user.username if self.user else "Deleted User"
#         return f"{user} - {self.product.name} ({self.rating}/5)"
    
# class ReviewImage(models.Model):

#     review = models.ForeignKey(ProductReview, on_delete=models.CASCADE, related_name='images')
#     image = models.ImageField(upload_to='reviews/')

# class ReviewReply(models.Model):
#     user = models.ForeignKey(
#         CustomUser,
#         on_delete=models.SET_NULL,
#         null=True
#     )
#     review = models.ForeignKey(ProductReview, on_delete=models.SET_NULL, null=True, blank=True, related_name='replies')
#     text = models.TextField()
#     image = models.ImageField(upload_to='reviews/', blank=True, null=True)

#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
