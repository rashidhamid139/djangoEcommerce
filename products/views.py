from django.shortcuts import render

# Create your views here.
def  home(request):
    if request.user.is_authenticated:
        username_is = "Justin Context"
        print(dir(request.user))
        context = {"username_is": request.user}
    else:
        context = {'username_is': "unknown"}

    return render(request, 'base.html', context)