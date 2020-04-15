from django.shortcuts import render

# Create your views here.
def  home(request):
    if request.user.is_authenticated:
        username_is = "Justin Context"
        context = {"username_is": request.user}
    else:
        context = {'username_is': "unknown"}

    return render(request, 'products/home.html', context)