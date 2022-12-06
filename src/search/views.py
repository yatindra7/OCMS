from . import models
from . import forms
from django.db.models import Q
from django.shortcuts import render, redirect
from users.models import Profile
from django.contrib.auth.models import User

#from .models import Search
#from .forms import SearchFrom
#from .models import Search
# import . as search

# Create your views here.

app_name = 'search'

def search_view(requests):
    if requests.method == 'POST':
        form = forms.SearchForm(requests.POST)
        print('[LOG]-----')
        if form.is_valid():
            query = form.cleaned_data('query')

            print('[LOG] ', Profile.objects.all())

            results = User.objects.filter(
                Q(name__icontains=query) | Q(email__icontains=query))
            context = {
                'students': results
            }
            _search = models.Search(query=query, results=results)
            _search.save()
            #return render(requests, 'search/search.html', context)
    else:
        form = forms.SearchForm()
        print('[LOG] Form made')
        print(form)
        print('-------')
        print('[GET] ', requests.GET)
        print('POST] ', requests.POST)
        query = requests.GET.get('search', None)
        print('-------')
        print(query)
        if query:
            results = User.objects.filter(
                Q(username__icontains=query) | Q(useremail__icontains=query))
            context = {
                'students': results
            }
            _search = models.Search(query=query, results=results)
            _search.save()
            print('success-----')
        else:
            context = {}
            print('bruh------')
        #context = {}
        #return redirect('classroom:home')
    return render(requests, 'search/search.html', context)
