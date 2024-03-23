from django import forms

from .models  import Review

# class ReviewForm(forms.Form):
    
#     user_name = forms.CharField(label='Your Name', max_length=100,error_messages={
#         'required':'Your name cannot be empty',
#         'max_lengrh':'Please enter a shorter name.',
#     })
#     review_text=forms.CharField(label='Your Feedback', max_length=200,widget=forms.Textarea )
#     rating=forms.IntegerField(min_value=1,max_value=5 )

class ReviewForm(forms.ModelForm):
    
    class Meta:
        model = Review
        #fields = ("",)
        fields= '__all__'
       # exclude=['']
       
        labels={
            "user_name":"Your Name",
            "review_text":"Your Feedback",
            "rating":"Your rating",
       }
        error_messages={
            
             'required':'Your name cannot be empty',
             'max_length':'Please enter a shorter name.',
            
        }
