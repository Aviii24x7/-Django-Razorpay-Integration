from django.shortcuts import render
from .models import DonateModel
import razorpay
from razorpayments.settings import RAZOR_KEY_ID,RAZOR_KEY_SECRET
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
    if request.method=="POST":
        name=request.POST.get("name")
        amount= int(request.POST.get("amount")) * 100

        client=razorpay.Client(auth=(RAZOR_KEY_ID, RAZOR_KEY_SECRET))
        #payment has a dict key as "id" which is needed for razorpay
        payment=client.order.create({'amount':amount,'currency':'INR', 'payment_capture': '1'})
        print(payment)
        obj=DonateModel(name=name,amount=amount/100,payment_id=payment['id'])
        obj.save()
        return render(request,"donate.html",context={'payment':payment})
    return render(request,"donate.html")

@csrf_exempt
def success(request):
    if request.method=="POST":
        a=request.POST
        print(a)
        order_id=""
        for key,val in a.items():
            if key=="razorpay_order_id":
                order_id=val
                break
        inst=DonateModel.objects.get(payment_id=order_id)
        inst.paid=True
        inst.save()
        print(order_id)
    return render(request,"success.html")




