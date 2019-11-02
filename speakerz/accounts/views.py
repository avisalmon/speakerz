from django.urls import reverse_lazy
from .forms import UserCreatForm
from django.views.generic import CreateView


class SignUp(CreateView):
    form_class = UserCreatForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'
