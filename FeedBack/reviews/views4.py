from django.shortcuts import render

from django.http import HttpResponseRedirect

from . forms import ReviewForm

from django.views import View

from django.views.generic.base import TemplateView


from .models import Review


# Create your views here.

class ReviewView(View):
    
    def get(self,request):
        
        form=ReviewForm()
    
        
        return render(request,'reviews/review.html',{ 'form':form })

        
    def post(self,request):
        
        form=ReviewForm(request.POST)
        if form.is_valid():    
            form.save()
         
            
            return HttpResponseRedirect('/thank-you')  

        return render(request,'reviews/review.html',{ 'form':form })
    
    
# class ThankyouView(View):
#     def get(self, request):
        
#         return render(request,'reviews/thank_you.html')
    
    
class ThankyouView(TemplateView):
    
    template_name    = 'reviews/thank_you.html'  
    
    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        context['message'] = 'it works'
        
        return context
    

class ReviewListView(TemplateView):
    
    template_name='reviews/review_list.html'
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        reviews=Review.objects.all()
        context['reviews']=reviews
        
        return context
        
    
class SingleReviewView(TemplateView):
    template_name="reviews/single_review.html"
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        review_id=kwargs['id']
        selected_review=Review.objects.get(id=review_id)
       
        context['review']=selected_review
        
        return context
    


