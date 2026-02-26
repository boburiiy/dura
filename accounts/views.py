from django.shortcuts import render, redirect
from django.views.generic import View
from accounts.forms import Signup
from django.contrib.auth import login, authenticate, get_user_model


class SignupView(View):
    template = 'accounts/auth/signup.html'

    def get(self, request):
        form = Signup()
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = Signup(request.POST, request.FILES or None)

        if form.is_valid():
            user = form.save()
            # authenticate with the raw password provided in the form
            user = authenticate(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password1')
            )
            if user:
                login(request, user)
                return redirect('/')
            form.add_error(
                None, 'Registration succeeded but authentication failed.')
        print(form.errors)
        return render(request, self.template, {'form': form})
