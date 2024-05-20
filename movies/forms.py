from django import forms

CHOICES = {"1": "1", "2": "2","3":"3","4":"4","5":"5"}

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'h-10 bg-background text-sm ring-offset-background file:border-0 file:bg-transparent file:text-sm file:font-medium placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50 block w-full appearance-none rounded-md border border-gray-300 px-3 py-2 placeholder-gray-400 shadow-sm focus:border-gray-800 focus:outline-none focus:ring-gray-800 dark:border-gray-700 dark:bg-gray-800 dark:text-gray-50 dark:placeholder-gray-400'
    }), label='Username')
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'h-10 bg-background text-sm ring-offset-background file:border-0 file:bg-transparent file:text-sm file:font-medium placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50 block w-full appearance-none rounded-md border border-gray-300 px-3 py-2 placeholder-gray-400 shadow-sm focus:border-gray-800 focus:outline-none focus:ring-gray-800 dark:border-gray-700 dark:bg-gray-800 dark:text-gray-50 dark:placeholder-gray-400'
    }), label='Password')
    
class CreateReviewForm(forms.Form):
    CHOICES= (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    rating = forms.CharField(widget=forms.Select(choices=CHOICES,attrs={
        'class':'rounded-lg border  text-card-foreground shadow-sm w-full  p-1 '
    }),label='Rating')
    description = forms.CharField(widget=forms.Textarea(attrs={
        'class':'rounded-lg border  text-card-foreground shadow-sm w-full  p-1 '
    }),label='Description')