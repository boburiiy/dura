from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView
from accounts.forms import SignupForm, LoginForm


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'auth/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request=request,
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password')
            )
            if user:
                login(request, user)
                return redirect('/')
            form.add_error(None, 'Invalid username or password')
        return render(request, 'accounts/auth/login.html', {'form': form})


class SignupView(View):

    template = 'auth/signup.html'

    def get(self, request):
        form = SignupForm()
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = SignupForm(request.POST, request.FILES or None)

        if form.is_valid():
            user = form.save()
            # authenticate with the raw password provided in the form
            login(request, user)
            return redirect('/')
        form.add_error(None, 'authentication failed.')
        print(form.errors)
        return render(request, self.template, {'form': form})


def LogoutView(request):
    if request.method == "POST":
        logout(request)
        return redirect('index')
    return render(request, template_name='auth/logout.html')
