
from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView

from django.http import HttpResponseRedirect

#from .forms import ProfileForm

from .models import User_Profile
# Create your views here.


# def store_file(file):
    
#     with open("temp/image.jpg", 'wb+') as dest:
#         for chunck in file.chunks():
#             file.write(chunck)
            
 
class CreateProfileView(CreateView):   
    
    template_name ="profiles/create_profile.html"
    model = User_Profile     
    fields= '__all__'
    success_url = "/profiles"
      

# class CreateProfileView(View):
#     def get(self, request):
        
#         form = ProfileForm()
#         return render(request, "profiles/create_profile.html", {'form':form})

#     def post(self, request):
        
#         submitted_form = ProfileForm(request.POST,request.FILES)
#         if submitted_form.is_valid():
            
#             profile = User_Profile(image= request.FILES['user_image'])
#             profile.save()
#             return HttpResponseRedirect('/profiles')
        
#         return render(request, "profiles/create_profile.html", {'form':submitted_form})
        
        