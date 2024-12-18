from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework import status
import requests

from weather.utils import map_weather_data_memento, map_one_service

# Constants
OPEN_METEO_API_URL = "https://api.open-meteo.com/v1/forecast"
ONE_SERVICE_API_URL = "https://one-api.ir/weather/"

class BaseWeatherView(APIView):
    """
    Base class for weather-related API views.
    Provides helper methods for validation and external API calls.
    """
    @staticmethod
    def validate_query_params(params, required_keys):
        """
        Validates that all required keys are present in the query parameters.
        """
        missing_keys = [key for key in required_keys if not params.get(key)]
        if missing_keys:
            raise ValidationError(
                {"error": f"Missing required query parameters: {', '.join(missing_keys)}"}
            )

    @staticmethod
    def fetch_external_api(api_url, params):
        """
        Fetch data from an external API and handle potential errors.
        """
        try:
            response = requests.get(api_url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            raise ValidationError({"error": f"Failed to fetch data from API: {str(e)}"})


class GetMeteoWeather(BaseWeatherView):
    def get(self, request, *args, **kwargs):
        """
        API view to fetch and return weather data based on latitude and longitude.
        """
        # Step 1: Validate query parameters
        self.validate_query_params(request.query_params, required_keys=["lat", "lon"])

        # Step 2: Prepare API call
        lat = request.query_params.get("lat")
        lon = request.query_params.get("lon")
        params = {
            "latitude": lat,
            "longitude": lon,
            "daily": "temperature_2m_max,temperature_2m_min,uv_index_max,precipitation_sum,sunrise,sunset,"
                     "weather_code,wind_speed_10m_max,precipitation_probability_max,relative_humidity_2m_mean",
            "current": "temperature_2m,relative_humidity_2m,apparent_temperature,precipitation,rain,"
                       "weather_code,cloud_cover,surface_pressure,wind_speed_10m,wind_direction_10m",
            "timezone": "auto",
        }

        # Step 3: Fetch data and map response
        weather_data = self.fetch_external_api(OPEN_METEO_API_URL, params)
        response_data = map_weather_data_memento(weather_data,lat,lon)

        # Step 4: Return response
        return Response(data=response_data, status=status.HTTP_200_OK)


class GetOneServiceWeather(BaseWeatherView):
    def get(self, request, *args, **kwargs):
        """
        API view to fetch and return weather data based on latitude, longitude, and token.
        """
        # Step 1: Validate query parameters
        self.validate_query_params(request.query_params, required_keys=["lat", "lon", "token"])

        # Step 2: Prepare API calls
        lat = request.query_params.get("lat")
        lon = request.query_params.get("lon")
        token = request.query_params.get("token")

        daily_params = {
            "lat": lat,
            "lon": lon,
            "action": "dailybylocation",
            "token": token,
        }
        current_params = {
            "lat": lat,
            "lon": lon,
            "action": "currentbylocation",
            "token": token,
        }

        # Step 3: Fetch data from APIs and map response
        daily_data = self.fetch_external_api(ONE_SERVICE_API_URL, daily_params)
        current_data = self.fetch_external_api(ONE_SERVICE_API_URL, current_params)
        response_data = map_one_service(daily_data, current_data, lat, lon)

        # Step 4: Return response
        return Response(data=response_data, status=status.HTTP_200_OK)
