from django.urls import path
from . import views


urlpatterns = [

    #######
    #get a value (GET /keys/{id})
    #check if a value exists (HEAD /keys/<id>)
    #delete a value (DELETE /keys/{id})
    path('keys/<int:id>' , views.single_record_handler),
    #######

    #######
    #set a value (PUT /keys)
    # delete all values (DELETE /keys)
    # set an expiry time when adding a value (PUT /keys?expire_in=60)
    #get all values (GET /keys)
    #support wildcard keys when getting all values (GET /keys?search=wo$d)
    path('keys', views.MultipleRecordsHandler.as_view()),
    #######

]