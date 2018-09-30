from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import FormView
from .forms import FeedbackForm


class ContactsView(FormView):
    template_name = 'contacts/contacts.html'
    form_class = FeedbackForm
    success_url = reverse_lazy('contacts:mail-sent')

    def form_valid(self, form):
        subject = form.cleaned_data['subject']
        sender = form.cleaned_data['sender']
        message = form.cleaned_data['message']
        copy = form.cleaned_data['copy']
        recipients = ['antongramenko@gmail.com']
        if copy:
            recipients.append(sender)
        send_mail(subject, message, 'admin@myshop.com', recipients)
        return super(ContactsView, self).form_valid(form)
