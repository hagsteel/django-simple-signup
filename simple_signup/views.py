from django.contrib.auth import logout, login, authenticate
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, View
from .forms import UserCreationForm
from django.contrib.auth import get_user_model


class SignUp(CreateView):
    template_name = 'registration/user_form.html'
    model = get_user_model()
    form_class = UserCreationForm

    def form_valid(self, form):
        resp = super(SignUp, self).form_valid(form)
        user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
        login(self.request, user)
        return resp

    def get_success_url(self):
        return reverse('create_project')
