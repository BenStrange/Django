from datetime import datetime
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect

from django.shortcuts import redirect
from django.urls import reverse

class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'home/register.html'
    success_url = '/smart/notes'  # This may not be necessary with the override below

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        response = super().form_valid(form)  # Saves the User model

        # Authenticate the user
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')  # UserCreationForm uses 'password1' for the password field
        user = authenticate(self.request, username=username, password=password)

        # Log the user in
        if user:
            login(self.request, user)
            return redirect('/smart/notes')  # Redirect to the notes list

        return response  # Fallback response if user authentication or login fails



class LogoutInterfaceView(LogoutView):
    template_name = 'home/logout.html'

class LoginInterfaceView(LoginView):
    template_name = 'home/login.html'

class HomeView(TemplateView):
    template_name = 'home/welcome.html' 
    extra_context = {'today': datetime.today()}