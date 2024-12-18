from django.urls import path

from weather.views import GetMeteoWeather , GetOneServiceWeather

urlpatterns = [
    path("weather/meteo/get/",GetMeteoWeather.as_view(),name="get-weather-meteo"),
    path("weather/one-service/get/",GetOneServiceWeather.as_view(),name="get-weather-one-service"),
]
