# Weather API Service

## What is the Problem?
Many applications rely on weather data from external APIs. But this can cause issues, such as:
- The weather API changes its format or endpoints, forcing you to update your entire app.
- The weather API fails to respond or goes offline, leaving your app without data and possibly breaking its functionality.

## How Does This Service Solve It?
1. **Stable Interface:**
   - This service acts as a bridge between your app and weather APIs. If the weather API changes, you only need to update this service, not your entire app.
   
2. **Fake Data Support:**
   - If the weather API fails or doesn't return data, this service generates fake weather data. Your app continues to work even when the external API is unavailable.

## Environment Variables
You need to set these variables in your environment:
- `SECRET_KEY`: The secret key for your Django app.
- `DEBUG`: Set to `True` for development or `False` for production.
- `ALLOWED_HOSTS`: A list of allowed hosts for the app (e.g., `localhost`, `127.0.0.1`).

## Available Gateways
Currently, the service supports the following endpoints:

### 1. Meteo Weather API Gateway
**Endpoint:**
```
GET /api/weather/meteo/get/
```
**Parameters:**
- `lat`: Latitude of the location (e.g., `35.6892` for Tehran).
- `lon`: Longitude of the location (e.g., `51.3890` for Tehran).

### 2. One-Service Weather API Gateway
**Endpoint:**
```
GET /api/weather/one-service/get/
```
**Parameters:**
- `lat`: Latitude of the location.
- `lon`: Longitude of the location.
- `token`: Authentication token for the One-Service API.

## Example JSON Response
When calling the API, the response may look like this (using fake data if the external API fails):

```json
{
    "latitude": 0.0,
    "longitude": 0.0,
    "daily": [
        {
            "dt": "2024-12-15",
            "pop": 20,
            "uvi": 5,
            "rain": 0.5,
            "temp": {
                "max": 30,
                "min": 15,
                "day": 22,
                "morn": 18,
                "eve": 20,
                "night": 16
            },
            "clouds": 10,
            "sunset": "2024-12-15T17:00:00",
            "sunrise": "2024-12-15T07:00:00",
            "weather": [
                {
                    "id": 800,
                    "icon": "clear_day",
                    "main": "Clear",
                    "description": "Clear sky"
                }
            ],
            "humidity": 50,
            "pressure": 1010,
            "wind_speed": 5
        }
    ],
    "current": {
        "dt": "2024-12-15T14:00:00",
        "uvi": 3,
        "rain": null,
        "temp": 22,
        "clouds": 15,
        "sunset": "2024-12-15T17:00:00",
        "sunrise": "2024-12-15T07:00:00",
        "weather": [
            {
                "id": 800,
                "icon": "clear_day",
                "main": "Clear",
                "description": "Clear sky"
            }
        ],
        "humidity": 48,
        "pressure": 1012,
        "wind_deg": 180,
        "dew_point": 10,
        "feels_like": 22,
        "visibility": 10000,
        "wind_speed": 5
    },
    "timezone": "UTC",
    "timezone_offset": 0,
    "fake": true
}
```

if the data is fake , it will have a fake key set to True, otherwise it won't have a fake key.
also there are 7 days info inside the daily key.

## Conclusion
This service ensures your app remains stable and functional by handling weather API changes and failures gracefully. It’s a simple and reliable solution for managing weather data.

