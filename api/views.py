from .models import Data
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DataSerializer
from rest_framework.views import APIView
from django.db.models import Q
from drf_yasg.utils import swagger_auto_schema



"""
I used both functional approach and class based approach
While the api is visually documented on /
I recommend using Tools like Postman for testing
"""


###############################
#  FUNCTIONAL BASED APPROACH  #
###############################


@swagger_auto_schema(methods=['GET'], tags=["single_record"], operation_description="Get: Return a record by id", responses={200: DataSerializer(), 404: 'Record NOT Found'})
@swagger_auto_schema(methods=['HEAD'], tags=["single_record"], operation_description="Head: Check if record exists by id", responses={302: None, 404: 'Record NOT Found'})
@swagger_auto_schema(methods=['DELETE'], tags=["single_record"], operation_description="Delete: Delete a record by id", responses={200: "Record deleted!", 404: 'Record NOT Found'})
@api_view(['GET' , 'HEAD' , 'DELETE'])
def single_record_handler(request , id):

    try:
        key_value = Data.objects.get(pk=id)
    except Data.DoesNotExist:
        return Response({
            "status": "failed",
            "message": "Record Not Found"
        }, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DataSerializer(key_value)
        return Response({
            "status":"success",
            "message":"Record Found",
            "record" : serializer.data
        } , status=status.HTTP_200_OK)

    if request.method == 'HEAD':
        return Response(status=status.HTTP_302_FOUND , headers={
            "Content-Length": 50
        })

    if request.method == 'DELETE':
        key_value.delete()
        return Response({
            "status": "success",
            "message": "Record deleted!"
        }, status=status.HTTP_200_OK)


##################################
#  APIView CLASS BASED APPROACH  #
##################################


class MultipleRecordsHandler(APIView):

    @swagger_auto_schema(tags=["multiple_records"],
                         operation_description="Get: Return all records with or without filters",
                         responses={200: DataSerializer(many=True)})
    def get(self,request):
        filter = request.query_params.get("filter" , None)
        all_records = None
        if filter is not None:
            if "$" in filter:
                lookup_list = filter.split("$")
                all_records = Data.objects.filter(
                    Q(key__startswith=lookup_list[0]) & Q(key__endswith=lookup_list[1])
                )
            else:
                all_records = Data.objects.filter(key__icontains=filter)
        else:
            all_records = Data.objects.all()
        serializer = DataSerializer(all_records , many=True)
        return Response({
            "status":"success",
            "message":"Filtered records",
            "records": serializer.data
        } , status=status.HTTP_200_OK)

    @swagger_auto_schema(tags=["multiple_records"], operation_description="Put: Update a record",request_body=DataSerializer(), parameters=["expire_in"], responses={200: DataSerializer(), 404: 'Record Not Found',
                                    400: 'Please provide key value json object'})
    def put(self,request):
        key = request.data.get("key", None)
        value = request.data.get("value", None)
        expire_in = request.query_params.get("expire_in", None)

        if key is not None and value is not None:
            try:
                record = Data.objects.get(key=key)
            except Data.DoesNotExist:
                return Response({
                    "status": "failed",
                    "message": "Record Not Found"
                }, status=status.HTTP_404_NOT_FOUND)
            record.value = value
            if expire_in is not None:
                record.expire_in = expire_in
            record.save()
            serializer = DataSerializer(record)
            return Response({
                "status": "success",
                "message": "Record Updated successfully",
                "record": serializer.data
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                "status": "failed",
                "message": "Please provide key value json object"
            }, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(tags=["multiple_records"],
                         operation_description="Delete: Delete all records",
                         responses={200: 'All records Deleted!', 400: 'Cant delete all records'})
    def delete(self, request):

        try:
            Data.objects.all().delete()
        except:
            return Response({
            "status": "failed",
            "message": "Can't delete all records"
        }, status=status.HTTP_400_BAD_REQUEST)

        return Response({
            "status": "success",
            "message": "All records Deleted!"
        }, status=status.HTTP_200_OK)
