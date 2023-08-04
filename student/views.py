from django.shortcuts import render
from student.forms import ContactForm

def index(request):
    form = ContactForm(request.POST or None)
    if request.method == "Post":
        if form.is_valid():
            print(form.cleaned_data)
        else:
            print(form.errors)
    context = {
        "form":form
    }
    return render(request, "index.html",context)
