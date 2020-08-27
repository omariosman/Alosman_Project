from django import forms
from .models import Product, AddTransaction




class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['code','name', 'cost','selling_price', 'size', 'img']
        widgets = {
            'code': forms.TextInput(attrs={'readonly': 'readonly'})
        }
     
class AddTransactionForm(forms.ModelForm):
    class Meta:
        model = AddTransaction
        fields = ['date', 'product_code', 'quantity']
        
    

        

