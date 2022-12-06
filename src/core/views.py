from users.models import Profile
from classroom.models import Classroom, ClassroomTeachers
from django.shortcuts import render
from newsletter.forms import SubscribeForm
from contactus.forms import ContactUsForm
import sys
sys.path.append('..')


def landing(request):
    subscribe_form = SubscribeForm()
    contactus_form = ContactUsForm()
    context = {
        'title': "Home",
        'subscribe_form': subscribe_form,
        'contactus_form': contactus_form
    }
    return render(request, "landing_page.html", context)


def search_funtion(request):
    if request.method == 'GET':
        query = request.GET.get('search')
        try:
            status = Profile.objects.filter(name__icontains=query)
            return render(request, 'core/partials/_topbar.html', {'users': status})
        except:
            return render(request, 'core/partials/_topbar.html', {})
