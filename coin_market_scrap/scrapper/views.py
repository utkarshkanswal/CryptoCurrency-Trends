from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import ScrappedData
from .serializers import ScrappedDataSerializer
from datetime import datetime
from .web_scrawler import web_scrawler
import json
class ScrappedDataListApiView(APIView):
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the ScrappedData items for given requested user
        '''
        # result = web_scrawler.delay() 
        # print(result)
        scrappedData = ScrappedData.objects.filter()
        serializer = ScrappedDataSerializer(scrappedData, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the data with given Scrapped data
        '''
        # data = {
        #     'Name': request.data.get('Name'), 
        #     'Price': request.data.get('Price'), 
        #     'one_hr': request.data.get('one_hr'), 
        #     'twenty_four_hr': request.data.get('twenty_four_hr'), 
        #     'seven_days_hr': request.data.get('seven_days_hr'), 
        #     'market_cap': request.data.get('market_cap'), 
        #     'volume': request.data.get('volume'), 
        #     'circulating_supply': request.data.get('circulating_supply'), 
        #     'timestamp': datetime.now()
        # }
        # print("112-> ",json.loads(request.data))
        # serializer = ScrappedDataSerializer(data=request.data, many=True)
        dataList=[]
        try:
            dataList=json.loads(request.data)
        except Exception as e:
            dataList=request.data
        import copy

        for data in dataList:
            name = data['Name']
            
            scrappedData = ScrappedData.objects.filter(Name = name)
            if(len(scrappedData)>0):
                scrappedData = ScrappedData.objects.get(Name = name)
                serializer = ScrappedDataSerializer(scrappedData,data=data)
            else:
                serializer = ScrappedDataSerializer(data=data)
            try:
                if serializer.is_valid():
                    serializer.save()

            except Exception as e:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


        return Response("Successfully Added!!", status=status.HTTP_201_CREATED)