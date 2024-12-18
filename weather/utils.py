import warnings

from weather.fake_data import FAKE_WEATHER_DATA

# Constants for default values
DEFAULT_ICON = "default_icon"
DEFAULT_MAIN = "default_main"
DEFAULT_DESCRIPTION = "default_description"

def map_daily_weather_data(daily_data):
    """
    Maps daily weather data to a standardized format.
    """
    daily_mapped = []
    for i, date in enumerate(daily_data.get("time", [])):
        daily_mapped.append({
            "dt": date,
            "pop": daily_data.get("precipitation_probability_max", [None])[i],
            "uvi": daily_data.get("uv_index_max", [None])[i],
            "rain": daily_data.get("precipitation_sum", [None])[i],
            "temp": {
                "max": daily_data.get("temperature_2m_max", [None])[i],
                "min": daily_data.get("temperature_2m_min", [None])[i],
                "day": None,
                "morn": None,
                "eve": None,
                "night": None,
            },
            "clouds": None,
            "sunset": daily_data.get("sunset", [None])[i],
            "sunrise": daily_data.get("sunrise", [None])[i],
            "weather": [{
                "id": daily_data.get("weather_code", [None])[i],
                "icon": DEFAULT_ICON,
                "main": DEFAULT_MAIN,
                "description": DEFAULT_DESCRIPTION,
            }],
            "humidity": daily_data.get("relative_humidity_2m_mean", [None])[i],
            "pressure": None,
            "wind_speed": daily_data.get("wind_speed_10m_max", [None])[i],
        })
    return daily_mapped

def map_current_weather_data(current_weather):
    """
    Maps current weather data to a standardized format.
    """
    return {
        "dt": current_weather.get("time"),
        "uvi": None,
        "rain": current_weather.get("rain", [None]),
        "temp": current_weather.get("temperature_2m"),
        "clouds": current_weather.get("cloud_cover"),
        "sunset": None,
        "sunrise": None,
        "weather": [{
            "id": None,
            "icon": current_weather.get("weather_code", DEFAULT_ICON),
            "main": DEFAULT_MAIN,
            "description": DEFAULT_DESCRIPTION,
        }],
        "humidity": current_weather.get("relative_humidity_2m"),
        "pressure": current_weather.get("surface_pressure"),
        "wind_deg": current_weather.get("wind_direction_10m"),
        "dew_point": None,
        "feels_like": current_weather.get("apparent_temperature"),
        "visibility": None,
        "wind_speed": current_weather.get("wind_speed_10m"),
    }

def map_weather_data_memento(data,lat,lon):
    """
    Maps weather data from Open-Meteo API to a standardized structure.
    """
    if not data.get("latitude",False):
        response_data = FAKE_WEATHER_DATA.copy()
        warnings.warn("Invalid API response")
    else :
        response_data =  {
            "lat": data.get("latitude"),
            "lon": data.get("longitude"),
            "daily": map_daily_weather_data(data.get("daily", {})),
            "current": map_current_weather_data(data.get("current", {})),
            "timezone": data.get("timezone", "UTC"),
            "timezone_offset": data.get("timezone_offset", 0),
        }
    return response_data

def map_one_service_daily_data(daily_data):
    """
    Maps daily weather data from One-Service API to a standardized format.
    """
    return [{
        "dt": day["dt"],
        "uvi": None,
        "temp": {
            "day": day["temp"]["day"],
            "min": day["temp"]["min"],
            "max": day["temp"]["max"],
            "night": day["temp"]["night"],
            "eve": day["temp"]["eve"],
            "morn": day["temp"]["morn"],
        },
        "weather": day["weather"],
        "humidity": day["humidity"],
        "pressure": day["pressure"],
        "clouds": day["clouds"],
        "wind_speed": day["speed"],
        "pop": day["pop"],
        "sunset": day["sunset"],
        "sunrise": day["sunrise"],
    } for day in daily_data[:7]]

def map_one_service_current_data(current_data):
    """
    Maps current weather data from One-Service API to a standardized format.
    """
    return {
        "dt": current_data["dt"],
        "uvi": None,
        "rain": None,
        "temp": current_data["main"]["temp"],
        "clouds": current_data["clouds"]["all"],
        "sunset": current_data["sys"]["sunset"],
        "sunrise": current_data["sys"]["sunrise"],
        "weather": current_data["weather"],
        "humidity": current_data["main"]["humidity"],
        "pressure": current_data["main"]["pressure"],
        "wind_deg": current_data["wind"]["deg"],
        "dew_point": None,
        "feels_like": current_data["main"]["feels_like"],
        "visibility": current_data["visibility"],
        "wind_speed": current_data["wind"]["speed"],
    }

def map_one_service(data, current_data, lat, lon):
    """
    Maps weather data from One-Service API to a standardized structure.
    """
    if data.get("status") != 200 or current_data.get("status") != 200:
        response_data = FAKE_WEATHER_DATA.copy()
        warnings.warn("Invalid API response")
    else:
        response_data = {
            "lat": lat,
            "lon": lon,
            "daily": map_one_service_daily_data(data.get("result", {}).get("list", [])),
            "current": map_one_service_current_data(current_data.get("result", {})),
            "timezone": current_data.get("result", {}).get("timezone", 0),
        }
    return response_data
