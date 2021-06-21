from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

@login_required
def index(request):
    return render(request, 'myapp/index.html')


def signup(request):
    context = {}
    form = UserCreationForm(request.POST)
    print(f'{form=}')
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(request, 'myapp/index.html')
    context['form'] = form
    return render(request, 'registration/signup.html', context)