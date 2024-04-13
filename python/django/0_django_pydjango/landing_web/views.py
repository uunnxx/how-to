from django.http import HttpResponse
from django.shortcuts import render


# def first_page(request):
#     text_h2 = '<h2>First Page</h2>'
#     return HttpResponse(text_h2)


def first_page(request):
    text_h2 = 'Got this text from views.py'
    text = 'got this text from views.py, too'
    return render(request, './first_page.html', {
        'text1': text_h2,
        'text2': text
    })
