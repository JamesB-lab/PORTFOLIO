from django import forms
from django.conf import settings
from django.core.mail import send_mail
from django.core.validators import validate_email
from django.template.loader import get_template


class EmailForm(forms.Form):
    required_css_class = 'required'

    name = forms.CharField(label='Name')
    company = forms.CharField(label='Company')
    email = forms.CharField(label='E-mail', validators=[validate_email])
    phone = forms.CharField(label='Phone')
    location = forms.CharField(label='Location',
                               widget=forms.Select(
                                   choices=[
                                       ('remote', 'Remote'),
                                       ('hybrid', 'Hybrid'),
                                       ('onsite', 'Onsite'),
                                   ]
                               ))
    message = forms.CharField(label='Subject', widget=forms.Textarea)

    def send_email(self):
        # From the form
        name = self['name'].value()
        company = self['company'].value()
        their_email = self['email'].value()
        phone = self['phone'].value()
        location = self['location'].value()
        message = self['message'].value()
        # Configured
        subject = 'Portfolio contact form'
        noreply_email = 'James Booth <noreply@mail.jbooth.dev>'
        my_email = 'j.r.booth01@gmail.com'
        data = [{'label': self.fields.get(key).label, 'value': value} for key, value in self.cleaned_data.items()]
        context = {'data': data}
        text_template = get_template('email.txt')
        text_message=text_template.render(context)
        html_template = get_template('email.html')
        html_message=html_template.render(context)
        send_mail(
            subject=subject,
            message=text_message,
            from_email=noreply_email,
            recipient_list=[their_email, my_email],
            fail_silently=False,
        )
