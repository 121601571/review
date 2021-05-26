from django.shortcuts import render

# Create your views here.


from .models import reviewModel
from .sercls import reviewSerializer, reviewSerializer2
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class reviewList(generics.ListCreateAPIView ):
    queryset = reviewModel.objects.all()
    serializer_class = reviewSerializer



class reviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = reviewModel.objects.all()
    serializer_class = reviewSerializer
    lookup_field = 'reviewee_email'


class avgreviewDetail(APIView):
    #custom one..
    pass

    def get(self, request, reviewee_email):
        pass
        print(reviewee_email)
        re_score = reviewModel.objects.filter(reviewee_email = reviewee_email)
        avg ,cnt = 0,0
        for i in re_score:
            avg += i.rating
            cnt += 1
        if cnt == 0:
            return Response({'average_rating': 0.0})
        #serializer = reviewSerializer(re_score, many=True)
        return Response({'average_rating': avg/cnt })


class multireviewDetail(APIView):

    def get(self, request, reviewee_email):
        pass
        print(reviewee_email,'!!!')
        re_score = reviewModel.objects.filter(reviewee_email = reviewee_email)
        ser = reviewSerializer(re_score, many=True)
        return Response(ser.data)