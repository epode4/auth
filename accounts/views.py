from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.

def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:index') 

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():

        # 회원가입시 자동 로그인 후 index로 
            user = form.save()
            auth_login(request,user)
            return redirect('articles:index')

        # 회원가입시 로그인 창으로
            # form.save()
            # return redirect('accounts:login')
    else:
        form = CustomUserCreationForm()

    context = {
        'form': form
    }

    return render(request, 'account_form.html', context)


def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index') 

    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)

        if form.is_valid():
            auth_login(request, form.get_user())

            # http://127.0.0.1:8000/accounts/login/?next=/articles/create/
            next_url = request.GET.get('next') # next 키를 기준으로 이동 (/articles/create/)
            
            # next 인자가 url에 있을 때 : ('/articles/create/' or 'articles:index')
            # or 단축평가 : '/articles/create/'가 True로 바로 True 값 반환

            # next 인자가 url에 없을 때 : (None or 'articles:index')
            # or 단축평가 : None이 False로 바로 뒤에 있는 값 반환 

            return redirect(next_url or 'articles:index')
    
    else:
        form = CustomAuthenticationForm()

    context = {
        'form': form
    }

    return render(request, 'account_form.html', context)

def logout(request):
    auth_logout(request)

    return redirect('accounts:login')