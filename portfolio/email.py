from django import forms
from django.conf import settings
from django.core.mail import send_mail
from django.core.validators import validate_email


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
        noreply_email = 'James Booth <noreply@mail.nuggetmuffin.tech>'
        my_email = 'j.r.booth01@gmail.com'
        full_message = f'Message from: {name}\n'
        f'Company: {company}'
        f'Email: {their_email}'
        f'Phone: {phone}'
        f'Location: {location}'
        f'Message:\n{message}'
        send_mail(
            subject=subject,
            message=full_message,
            from_email=noreply_email,
            recipient_list=[their_email, my_email],
            fail_silently=False,
        )
