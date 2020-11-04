from django.shortcuts import render

# Create your views here.


def about(request):
    """ A view to return the about page """

    return render(request, 'about/about.html')


def contact(request):
    """ Imported emailJS code here """

    # I realized the code is still visible in chrome dev tools,
    # since Javascript is client-side, but I keep this in order
    # to show that I understand this at least, and for further development.
    # I aim to look into using the django sendmail function instead

    email_code = 'user_SNJGyOEpTaT5O7pC1cJUM'

    return render(request, 'about/contact.html', {'email_code': email_code})
