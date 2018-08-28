from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

def keyboard(request):
    return JsonResponse({
        'type':'buttons',
        'buttons':['first','second']
    })

@csrf_exempt
def answer(request):

    json_str = ((request.body).decode('utf-8'))
    received_json_data = json.loads(json_str)
    datacontent = received_json_data['content']
    
    if datacontent == 'first':
        message = 'you pressed the first button'
        return JsonResponse({
            'message':{
                'text':message
            },
            'keyboard':{
                'type':'buttons',
                'buttons':['first','second']
            }
        })
    elif datacontent == 'second':
        message = 'you pressed the second button'
        return JsonResponse({
            'message':{
                'text':message
            },
            'keyboard':{
                'type':'buttons',
                'buttons':['first','second']
            }
        })



# Create your views here.
