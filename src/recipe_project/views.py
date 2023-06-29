from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm


# define function view called login_view
def login_view(request):
    error_message = None
    form = AuthenticationForm()

    # when user hits login, post request generated
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        # check if form is valid
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            # use Django auth function to validate
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('recipes:list')
        else:
            error_message = 'well shoot, that did not work.'

    context = {
        'form': form,
        'error_message': error_message
    }
    return render(request, 'auth/login.html', context)

# define logout function


def logout_view(request):
    logout(request)
    return render(request, 'auth/success.html')