
from .models import CustomUser, Profile, LoginModel
from bookapp.models import Books
from django.contrib.auth import authenticate, login
from .serializers import UserSerializer, LoginSerializer, ProfileSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
@api_view(['POST'])
def UserRegistration(request):
    if request.method=="POST":
        filled_form = UserSerializer(data=request.data) 
        if filled_form.is_valid(raise_exception=True):
           cd = filled_form.data
           form = CustomUser.objects.create(
               first_name = cd.get("first_name"), 
               middle_name = cd.get("middle_name"), 
               last_name = cd.get("last_name"), 
               email = cd.get("email"),
               tel_number = cd.get("tel_number"), 
               gender = cd.get("Gender")
           )
           form.set_password(cd.get('password'))
           form.save() 
           new_profile = Profile.objects.create(Holder = form)
           new_profile.save()

        return Response('registration succesful')

@api_view(['POST'])    
def UserLogin(request):
    if request.method=='POST':
        LOGINFORM = LoginSerializer(data=request.data)
        if LOGINFORM.is_valid():
            cd= LOGINFORM.data
            Authorise = authenticate(request, username = cd.get('email'), password=cd.get('password'))
            if Authorise is not None:
                if Authorise.is_active:
                    login(request, Authorise)
                    return Response('login successful')

                else:
                    return Response('Disabled Account')  
            else:
                return Response("User Does not exist")

@api_view(['GET'])
def viewProfile(request):
    try:
        userProfile = ProfileSerializer(Profile.objects.get( Holder = request.user)).data
        return Response(userProfile)
    except ObjectDoesNotExist:
        userProfile = ProfileSerializer(Profile.objects.create(Holder=request.user)).data
        return Response(userProfile)
 
@api_view(['POST'])   
def editProfile(request):
    try:
        userprofile = Profile.objects.get(Holder = request.user)
        if request.method == "POST":
            profile = ProfileSerializer(userprofile, data=request.data)
            if profile.is_valid(raise_exception=True):
                cd = request.FILES.get('profile_picture')
                if cd is not None:
                    profile.profile_picture = cd
                    profile.save()
                else:
                    profile.save()
                return Response("update successful")
            else:
                return Response("Invalid Data Input")
    except ObjectDoesNotExist:
        return Response("You have no profile created")




    
    
    