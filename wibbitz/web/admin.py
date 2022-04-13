from django.contrib import admin
from web.models import Subscribe, Customer, Feature, Testimonial, MarketingFeature, Product,Blog, Contact, Review

admin.site.register(Subscribe)
admin.site.register(Customer)

class FeatureAdmin(admin.ModelAdmin):
    list_display = ["id","title","testimonial_author","author_designation"]
admin.site.register(Feature,FeatureAdmin)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ["id", "title" ]

admin.site.register(Review, ReviewAdmin)

class TestimonialAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "role", "company_name", "is_featured"]

admin.site.register(Testimonial,TestimonialAdmin)

class MarketingFeatureAdmin(admin.ModelAdmin):
    list_display = ["id", "image", "title", "description"]

admin.site.register(MarketingFeature,MarketingFeatureAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "description", "image", "logo"]

admin.site.register(Product, ProductAdmin)

class BlogAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "content_type", "image"]

admin.site.register(Blog,BlogAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ["id", "first_name", "last_name", "company", "job_role", "country"]

admin.site.register(Contact, ContactAdmin)
