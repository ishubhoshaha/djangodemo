from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect

from .forms import PersonForm
from .models import Person


# Create your views here.



# def list(request):
#     persons = Person.objects.all()
#     output = ", ".join(person.name for person in persons)
#     return HttpResponse(f"Registered Persons: \n {output}")


def list(request):
    persons = Person.objects.all()
    context = {"persons": persons}
    return render(request, "myapp/list.html", context)




def detail(request, person_id):
    try:
        person = Person.objects.get(pk=person_id)
    except Person.DoesNotExist:
        raise Http404("Person does not exist")

    return render(request, 'myapp/detail.html', {'person': person})



def create_person(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = PersonForm()

    return render(request, 'myapp/create_person.html', {'form': form})