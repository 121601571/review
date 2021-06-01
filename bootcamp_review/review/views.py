from django.shortcuts import render

# Create your views here.


from .models import reviewModel
from .sercls import reviewSerializer, reviewSerializer2
from rest_framework import generics, mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

class reviewList(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    generics.GenericAPIView ):
    queryset = reviewModel.objects.all()
    serializer_class = reviewSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # custom logic over ride to use CQGS...

        uname,rank = request.data.get('reviewee_email', ''),  request.data.get('rank', 0)
        print(uname+str(rank))
        return self.create(request, *args, **kwargs)



class reviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = reviewModel.objects.all()
    serializer_class = reviewSerializer
    lookup_field = 'reviewee_email'


class avgreviewDetail(APIView):
    #custom one..
    pass

    def get(self, request, reviewee_email):
        pass
        import time
        time.sleep(1)
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
        re_score = reviewModel.objects.filter(reviewee_email = reviewee_email)
        ser = reviewSerializer(re_score, many=True)
        return Response(ser.data)