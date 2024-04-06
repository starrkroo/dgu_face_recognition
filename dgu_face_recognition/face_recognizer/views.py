import numpy as np
import io
import cv2

from django.shortcuts import render
from django.http import JsonResponse
from .face_verification.main import FaceVerificator
from django.views.decorators.csrf import csrf_exempt
from .models import Accounts
from django.core.files.images import ImageFile


def get_image_bytes_of(image_bytes):
    image_np = np.frombuffer(image_bytes, np.uint8)
    image = cv2.imdecode(image_np, cv2.IMREAD_COLOR)
    return image

@csrf_exempt
def verify_face(request):
    uniqcode = request.POST.get('uniqcode')
    if uniqcode == "yYjQz3vV9tAZE67ECsbbRAsnhLPf1mc8":
        user_image_bytes = request.FILES.get("user_image_bytes").read()
        user_image_bytes = get_image_bytes_of(user_image_bytes)
        
        for account in Accounts.objects.values("image"):
            with open(account['image'], 'rb') as f:
                compare_db_image_bytes = f.read()
                compare_db_image_bytes = get_image_bytes_of(compare_db_image_bytes)
                print(compare_db_image_bytes)
                
                FaceVer = FaceVerificator(compare_db_image_bytes, user_image_bytes)
                if FaceVer.do_verify_face()['verified']:
                    return JsonResponse(dict(result='OK'))
                print(FaceVer.do_verify_face())
        else:
            return JsonResponse(dict(result='Error', explain='You are not in db'))
        
    else:
        return JsonResponse({"Error": "Failed getting info by unknown unique code"})

@csrf_exempt
def register_face(request):
    uniqcode = request.POST.get('uniqcode')
    print(uniqcode)
    if uniqcode == "yYjQz3vV9tAZE67ECsbbRAsnhLPf1mc8":
        image_bytes = request.FILES.get("image_account_to_store")

        Accounts.objects.create(image=image_bytes)
        
        return JsonResponse(dict(result="OK"))
    else:
        return JsonResponse({"Error": "Failed getting info by unknown unique code"})