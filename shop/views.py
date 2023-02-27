from django.shortcuts import render
from .models import product,Contact,Order,OrderUpdate
from math import ceil
from django.http import HttpResponse
import json

# Create your views here.
def index(request):
    allProds=[]
    catprods=product.objects.values('Category','id')
    cats={item['Category'] for item in catprods}
    for cat in cats:
        prod=product.objects.filter(Category=cat)
        n=len(prod)
        nslides=n//4 + ceil((n/4) - (n//4))
        allProds.append([prod, range(1, nslides), nslides])
    params={'allProds':allProds}
    return render(request, 'shop/index.html', params)

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    thank=False
    if request.method=="POST":
        name=request.POST.get('name', '')
        email=request.POST.get('email', '')
        phone=request.POST.get('phone', '')
        desc=request.POST.get('desc', '')
        contact=Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        thank=True
    return render(request, 'shop/contact.html', {'thank':thank})

def tracker(request):
    if request.method=="POST":
        orderId=request.POST.get('orderId', '')
        email=request.POST.get('email', '')
        
        try:
            order=Order.objects.filter(order_id=orderId, email=email)
            if len(order)>0:
                update=OrderUpdate.objects.filter(order_id=orderId)
                updates=[]
                for item in update:
                    updates.append({'text':item.update_desc, 'time':item.timestamp})
                    response=json.dumps([updates, order[0].items_json], default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')

        except Exception as e:
            return HttpResponse('{}')

    return render(request, 'shop/tracker.html')

def search(request):
    return render(request, 'shop/search.html')

def productView(request,myid):
    #Fetch the product using the id
    Product=product.objects.filter(id=myid)
    return render(request, 'shop/prodView.html', {'Product': Product[0]})

def checkout(request):
    if request.method=="POST":
        items_json=request.POST.get('itemsjson', '')
        name=request.POST.get('name', '')
        email=request.POST.get('email', '')
        address=request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city=request.POST.get('city', '')
        state=request.POST.get('state', '')
        pin_code=request.POST.get('pin_code', '')
        phone=request.POST.get('phone', '')
        order=Order(items_json=items_json, name=name, email=email, address=address, city=city, state=state, pin_code=pin_code, phone=phone)
        order.save()
        update=OrderUpdate(order_id=order.order_id, update_desc="The order has been placed.")
        update.save()
        thank=True
        id=order.order_id
        return render(request, 'shop/checkout.html', {'thank':thank, 'id':id})
    return render(request, 'shop/checkout.html')
