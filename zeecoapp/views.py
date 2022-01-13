from django.shortcuts import render
from .models import Enquiry
from bot.chat import get_response
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def index(request):
    if request.method == "POST":
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email_address = request.POST['email']
        services_rendered = request.POST['services']
        message = request.POST['message']
        enquiry = Enquiry.objects.create(firstname= request.POST['firstname'],lastname=request.POST['lastname'],
               email=request.POST['email'],services=request.POST['services'],message=request.POST['message'])
        enquiry.save()



    return render(request,"index.html")


@csrf_exempt
def botts(request):
    data = json.loads(request.body)
    message = data['message']
    response = get_response(message)
    messg = {"answer": response}
    re = messg["answer"]
    # message = {"answer": response}
    # return jsonify(message)



    return JsonResponse({"answer": re })


