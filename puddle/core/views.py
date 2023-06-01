from django.shortcuts import render, redirect

from item.models import Category, Item

from .forms import SignupForm


def index(request):
    # get the 6 newest items
    items = Item.objects.all()[0:6]
    categories = Category.objects.all()

    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items
    })


def contact(request):
    return render(request, 'core/contact.html')


def signup(request):
    # checking to see if form as been submitted
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })
