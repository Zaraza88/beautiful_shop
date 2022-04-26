from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages


from .forms import FormContact


class CreateContact(SuccessMessageMixin, CreateView):

    form_class = FormContact
    success_url = '/feedback/'#перенаправлять обратно в контакты и сделать вывод сообщения
    template_name = 'contact/contact.html'
    success_message = "%(name)s сообщение успешно отправлено"