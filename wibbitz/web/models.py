from django.db import models
from django.db.models.base import Model
from os import name

CONTENT_TYPE = (
    ("blog_post","Blog Post"),
    ("webinar","WebInar"),
    ("report","Report")
)
COMPANY_SIZE = (
    ("1","1-10"),
    ("2","11-50"),
    ("3","51-200"),
    ("4","201-500")
)
INDUSTRY = (
    ("1","Agriculture"),
    ("2","Banking & Finance"),
    ("3","Business Services & Software"),
)
JOB_ROLE = (
    ("1","C-Suite"),
    ("2","VP"),
)
COUNTRY = (
    ("us","United States"),
    ("albania","Albania"),
)

class Testimonial(models.Model):
    name=models.CharField(max_length=255)
    designation=models.CharField(max_length=255)
    description=models.TextField()
    logo=models.FileField(upload_to="testimonial/icons/", blank=True)
    company_name=models.CharField(max_length=255)
    image=models.ImageField(upload_to="testimonial/images/")
    is_featured=models.BooleanField(default=False)

    class Meta:
        db_table = "testimonial"
        ordering = ["-id"]

    def _str_(self):
        return self.name

class Customer(models.Model):
    product = models.ForeignKey("web.Product", on_delete=models.CASCADE)
    image = models.FileField(upload_to="customers")
    white_image = models.FileField(upload_to="customers",blank=True,null=True)

    def _str_(self):
        return str (self.id)

class Subscribe(models.Model):
    email = models.EmailField()

    def _str_(self):
        return self.email

class Feature(models.Model):
    image=models.ImageField(upload_to="feature/image/")
    icon= models.FileField(upload_to="feature/icons/")
    icon_background= models.CharField(max_length=25)
    title=models.CharField(max_length=225)
    description=models.TextField(max_length=255)
    testimonial_description=models.TextField(max_length=255)
    testimonial_author=models.CharField(max_length=128)
    author_designation=models.CharField(max_length=128)
    testimonial_logo = models.ImageField(upload_to="features/logos/")

    def _str_(self):
        return self.testimonial_author

class Review(models.Model):
    title = models.CharField(max_length=155)
    image = models.FileField(upload_to="reviews")
    play = models.FileField(upload_to="reviews")
    logo = models.FileField(upload_to="reviews/logo")

    def __str__(self):
        return str(self.id)

class MarketingFeature(models.Model):
    image=models.ImageField(upload_to="Marketingfeature/image/")
    title=models.CharField(max_length=128)
    description=models.TextField()

    class Meta:
        ordering =["id"]

    def _str_(self):
        return str(self.title)

class Blog(models.Model):
    image=models.ImageField(upload_to="Blog/image/")
    title=models.CharField(max_length=128)
    content_type=models.CharField(max_length=128,choices=CONTENT_TYPE)
    next = models.CharField(max_length=125, default="Read blog")

    class Meta:
        ordering =["id"]

    def _str_(self):
        return self.title

class Testimonial(models.Model):
    image = models.ImageField(upload_to="testimonials")
    logo = models.FileField(upload_to="testimonials\logo",blank=True,null=True)
    description = models.TextField(max_length=255)
    name = models.CharField(max_length=125)
    role = models.CharField(max_length=125)
    company_name = models.CharField(max_length=125)
    is_featured = models.BooleanField()

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ["id"]


class Product(models.Model):
    image = models.FileField(upload_to="product")
    hero_image = models.FileField(upload_to="product/hero")
    title = models.CharField(max_length=155)
    name = models.CharField(max_length=155)
    logo = models.FileField(upload_to="product/logo")
    description = models.TextField(max_length=255)
    bg_color = models.CharField(max_length=10, default="#fff")
    button_bg_color = models.CharField(max_length=10, default="#fff")

    class Meta:
        ordering = ["id"]

    def _str_(self):
        return self.title

class Contact(models.Model):
    email=models.EmailField()
    first_name=models.CharField(max_length=128)
    last_name=models.CharField(max_length=128)
    company=models.CharField(max_length=128)
    company_size=models.CharField(max_length=128,choices=COMPANY_SIZE)
    industry=models.CharField(max_length=128,choices=INDUSTRY)
    job_role=models.CharField(max_length=128,choices=JOB_ROLE)
    country=models.CharField(max_length=128,choices=COUNTRY)
    user_agreement=models.BooleanField(default=False)

    class Meta:
        ordering = ["id"]
    def _str_(self):
        return self.first_name

