from django.shortcuts import render
from web.models import Contact, Subscribe, Customer, Feature, Review, Testimonial, MarketingFeature, Product, Blog
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
import json
from web.forms import ContactForm

def index(request):
    customers = Customer.objects.all()
    latest_customers = Customer.objects.all()[:4]
    features = Feature.objects.all()
    reviews = Review.objects.all()
    true_testimonials = Testimonial.objects.filter(is_featured=True)
    false_testimonials = Testimonial.objects.filter(is_featured=False)
    marketings = MarketingFeature.objects.all()
    products = Product.objects.all()
    blogs = Blog.objects.all()

    form = ContactForm()

    context = {
            "customers" : customers,
            "features" : features,
            "reviews" : reviews,
            "true_testimonials" : true_testimonials,
            "false_testimonials" : false_testimonials,
            "marketings" : marketings,
            "products" : products,
            "blogs" : blogs,
            "form" : form,
            "latest_customers" : latest_customers
    }
    
    return render(request,"index.html",context=context)

def subscribe(request):
    email = request.POST.get('email')

    if not Subscribe.objects.filter(email=email).exists() and email:

        Subscribe.objects.create(email=email)

        response_data = {
            "status":"success",
            "title":"SuccessFully Registered",
            "message":"You subscribed to our newsletter successfully"
        }
    elif not email:
        response_data = {
           "status" : "error",
            "title" : "Enter a Valid Email",
            "message" : "You Enter a Invalid Email,Check the Email"
        }
    else:
        response_data = {
            "status" : "error",
            "title" : "Already Registered",
            "message" : "You are Already Subscribed to the News Letter,no need to Subscribe again"
        }
    return HttpResponse(json.dumps(response_data),content_type="application/javascripts")


def contact(request):
    form = ContactForm(request.POST)
    print(form, "form========")
    if form.is_valid():
        form.save()
        response_data = {
            "status":"success",
            "title":"SuccessFully Registered",
            "message":"You subscribed to our newsletter successfully"
        }
    else:
        response_data = {
                "status" : "error",
                "title" : "Your Form is Not Valid",
                "message" : "Your Form is Not Valid,Try again"
            }
    return HttpResponse(json.dumps(response_data),content_type="application/javascripts")

def product(request,pk):
    product = get_object_or_404(Product.objects.filter(pk=pk))

    customers = Customer.objects.filter(product=product)

    context = {
        "product" : product,
        "customers" : customers
    }
    return render(request, "product.html", context = context)