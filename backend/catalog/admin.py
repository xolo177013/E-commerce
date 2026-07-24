from django.contrib import admin
from .models import Category, Product, ProductVariant, ProductImage
class ProductVariantInline(admin.TabularInline):
    model = ProductVariant
    extra = 1

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra =1

# class ProductReviewInline(admin.TabularInline):
#     model = ProductReview
#     extra =1


# class ReviewImageInline(admin.TabularInline):
#     model = ReviewImage
#     extra = 1

# class ReviewReplyInline(admin.TabularInline):
#     model = ReviewReply
#     extra = 1


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductVariantInline, ProductImageInline]

# class ProductReviewAdmin(admin.ModelAdmin):
#     inlines = [ ReviewImageInline, ReviewReplyInline]

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
# admin.site.register(ProductReview, ProductReviewAdmin)