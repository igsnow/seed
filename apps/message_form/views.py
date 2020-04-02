from django.shortcuts import render


def message_form(request):
    age = 18

    return render(request, 'message_form.html', {"age": age})

# Create your views here.
