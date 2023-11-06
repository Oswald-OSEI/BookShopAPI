from django.shortcuts import render, reverse
from .forms import UserRegistrationForm, LoginForm
from django.http import HttpResponse, HttpResponseRedirect
from .models import CustomUser
from bookapp.models import Books
from django.contrib.auth import authenticate, login
from .serializers import UserSerializer, LoginSerializer
from rest_framework.decorators import api_view
# Create your views here.
@api_view(['POST'])
def UserRegistration(request):
    if request.method=="POST":
        filled_form = UserSerializer(data=request.data) 
        if filled_form.is_valid(raise_exception=True):
           form = filled_form.save(commit=False)
           form.set_password(filled_form.data['password'])
           form.save()
           
        return Response(form.data)

@api_view(['POST'])    
def UserLogin(request):
    if request.method=='POST':
        LOGINFORM = LoginSerializer(data=request.data)
        if LOGINFORM.is_valid():
            cd= LOGINFORM.data
            Authorise = authenticate(request, username = cd['email'], password=cd['password'])

            if Authorise is not None:
                if Authorise.is_active:
                    login(request, Authorise)
                    return HttpResponseRedirect(reverse('bookapp:home'))

                else:
                    return HttpResponse('Disabled Account')  
            else:
                return HttpResponse("User Does not exist")

    #else:
        #return render(login_page)

    
    
    
    