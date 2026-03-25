from django.shortcuts import render
import requests
from django.http import JsonResponse
# Create your views here.
# https://www.weatherapi.com/
API_KEY=''

def dashboard(request):

    url_base='http://api.weatherapi.com/v1'

    url_base=f'http://api.weatherapi.com/v1/current.json?key={API_KEY}q=Valdivia&aqi=no'
    
    headers={
        "Authorization":f"Bearer {API_KEY}"
    }
    try:
        response=requests.get(url_base,timeout=10,headers=headers)
        data=response.json()
        #aca se cocina la informacion para pasarla al template
    except requests.RequestException as e:
        return JsonResponse({
            "ok":False,
            "error":f"Error en la API: {e} "
        },status=500)

    context={
        'respuesta':data,
    }
    return render(request,'dashboard.html',context=context)