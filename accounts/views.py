from django.contrib.auth import login
from django.views.generic.edit import FormView
from .forms import SignupForm
from django.urls import reverse_lazy

class SignupView(FormView):
    template_name = 'signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('home')  # Replace 'index' with the name of the URL pattern for your index page

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)
