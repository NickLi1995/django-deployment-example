from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . import forms
from .forms import NewTopic, UserForm, UserProfileInfoForm
from AppTow.models import Topic, Webpage, AccessRecord
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def index(request):
    # return HttpResponse('<em>My Second App</em>')
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_record': webpages_list}
    my_dict = {'insert_me': 'Hello, I am from views.py !'}
    return render(request, 'AppTwo/index.html', context=date_dict)


def form_name_view(request):
    form = forms.FormName()
    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            pass

    return render(request, 'AppTwo/form_page.html', {'form': form})


def topics(request):
    form = NewTopic()

    if request.method == 'POST':
        form = NewTopic(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            pass
    return render(request, 'AppTwo/topic.html', {'form': form})


def index1(request):
    context_dict = {'text': 'Hello World', 'number': 1000}
    return render(request, 'basic/index.html', context_dict)


def other(request):
    return render(request, 'basic/other.html')


def relative(request):
    return render(request, 'basic/relative_url_templates.html')


def index2(request):
    return render(request, 'user/index.html')


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.erroes)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'user/registration.html',
                  {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('AppTow:index2'))
            else:
                return HttpResponse('ACCOUNT NOT ACTIVE!')
        else:
            print('Someone tried to login and failed!')
            print('Username: {} and password {}'.format(username, password))
            return HttpResponse('Invalid login details supplied!')
    else:
        return render(request, 'user/login.html', {})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('AppTow:index2'))


@login_required
def special(request):
    return HttpResponse('You are logged in, Nice!')
