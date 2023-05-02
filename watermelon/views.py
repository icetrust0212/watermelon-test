from django.shortcuts import render, redirect
from django.urls import reverse_lazy

# Create your views here.
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from .forms import SellerForm
from .models import Seller
from django.shortcuts import redirect
import uuid
from django.http import HttpResponse
from django.urls import reverse

def sellerForm(request):
    step_count = 6
    if request.method == 'GET':
        data = {'survey_id': uuid.uuid4(), 'step': 1, 'step_count': step_count}
        return render(request, 'seller_wizard.html', {'data': data})
    else:
        survey_id = request.POST.get('survey_id')
        if (survey_id == None): 
            survey_id = uuid.uuid4()
        step = int(request.POST.get('step'))
        direction = request.POST.get('direction')
        
        store_name = request.POST.get('store_name')
        gift_card_balance = request.POST.get('gift_card_balance')
        selling_price = request.POST.get('selling_price')
        funds_network = request.POST.get('funds_network')
        funds_address = request.POST.get('funds_address')
        email = request.POST.get('email')

        formData = {'survey_id' : survey_id}

        if (store_name):
            formData['store_name'] = store_name
        if (gift_card_balance):
            formData['gift_card_balance'] = gift_card_balance
        if (selling_price):
            formData['selling_price'] = selling_price
        if (funds_network):
            formData['funds_network'] = funds_network
        if (funds_address):
            formData['funds_address'] = funds_address
        if (email):
            formData['email'] = email

        obj, created = Seller.objects.update_or_create(survey_id = survey_id, defaults = formData)
        if step == step_count:
            return redirect(reverse('success'))

        if (direction == 'NEXT' and step < step_count):
            step = step + 1
        if (direction == 'PREV' and step > 0):
            step = step - 1
        data = {'survey_id': survey_id, 'step': step, 'step_count': step_count}
        
        return render(request, 'seller_wizard.html', {'data': data, 'form': obj})

def sellers(request):
    all_sellers = Seller.objects.all()
    return render(request, 'all_sellers.html', {'data' : all_sellers})

class ResultsView(TemplateView):
    template_name = 'congratulations.html'


