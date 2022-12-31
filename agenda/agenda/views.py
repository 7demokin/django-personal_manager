from django.shortcuts import render

def index(request):
    """
    Purpose: request
    """
    return render(request, 'index.html', {})
# end def