from rest_framework import viewsets
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from . import models
from . import serializers

class MemberViewSet(viewsets.ModelViewSet):
    queryset = models.Member.objects.all()
    serializer_class = serializers.MemberSerializer

@csrf_exempt
def addMember(request):
    if request.method == 'POST':
        q = request.body
        print (q)
        
    return HttpResponse('Hello world')