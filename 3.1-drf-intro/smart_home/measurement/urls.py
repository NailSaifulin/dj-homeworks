from django.urls import path

from measurement.views import SensorListCreate, SensorRetrieveUpdate, MeasurementsCreate, SensorDetail

urlpatterns = [
    path('sensorlist/', SensorListCreate.as_view()),
    path('sensorretrieve/<pk>/', SensorRetrieveUpdate.as_view()),
    path('measurementscreate/', MeasurementsCreate.as_view()),
    path('sensorlist/<pk>/', SensorDetail.as_view())
]
