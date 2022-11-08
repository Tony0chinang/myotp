from django.shortcuts import render
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
import pyotp
from .models import phoneNumber
from rest_framework.views import APIView
import base64
from rest_framework.response import Response
from django.conf import settings

class generatekey:
    @staticmethod
    def returnValue(phone):
            return str(phone) + str(datetime.date(datetime.now())) + "Some Random key"



class getPhoneNumber(APIView):
    @staticmethod
    def get(request, phone):
        try:
            mbile = phoneNumber.objects.get(mobile=phone)
        except ObjectDoesNotExist:
            phoneNumber.objects.create(mobile=phone,)
            mbile = phoneNumber.objects.get(mobile=phone)
                
        
        mbile.counter += 1
        mbile.save()
        
        key = generatekey()
        otp = base64.b32encode(key.returnValue(phone).encode())
        newotp = pyotp.HOTP(otp)
        print(newotp.at (mbile.counter))
        return Response({"OTP": newotp.at (mbile.counter)}, status=200 )
    
    @staticmethod
    def post(request, phone):
        try:
            mbile = phoneNumber.objects.get(mobile=int(phone))
        except ObjectDoesNotExist:
                return Response("invalid phone number", status=404)
        
        key = generatekey()
        otp = base64.b32encode(key.returnValue(phone).encode())
        newotp = pyotp.HOTP(otp)
        print(newotp.at (mbile.counter))
        if newotp.verify(request.data["otp"], mbile.counter):
            mbile.isverified = True
            mbile.save()
            return Response("you are authorised", status=200 )

        return Response("invalid OTP", status=400 )

     
class getPhoneNumber_TimeBased(APIView):
    @staticmethod
    def get(request, phone):
        try:
            mbile = phoneNumber.objects.get(mobile=phone)
        except ObjectDoesNotExist:
            phoneNumber.objects.create(mobile=phone,)
            mbile = phoneNumber.objects.get(mobile=phone)
                
        
        mbile.counter += 1
        mbile.save()
        
        key = generatekey()
        otp = base64.b32encode(key.returnValue(phone).encode())
        newotp = pyotp.TOTP(otp,interval = settings.EXPIRY_TIME)
        print(newotp.now())
        return Response({"OTP": newotp.now()}, status=200 )
    
    @staticmethod
    def post(request, phone):
        try:
            mbile = phoneNumber.objects.get(mobile=int(phone))
        except ObjectDoesNotExist:
                return Response("invalid phone number", status=404)
        
        key = generatekey()
        otp = base64.b32encode(key.returnValue(phone).encode())
        newotp = pyotp.TOTP(otp,interval = settings.EXPIRY_TIME)
        if newotp.verify(request.data["otp"]):
            mbile.isverified = True
            mbile.save()
            return Response("you are authorised", status=200 )

        return Response("invalid or expired OTP", status=400 )