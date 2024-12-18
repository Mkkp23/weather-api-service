FAKE_WEATHER_DATA = {
    "latitude": 0.0,
    "longitude": 0.0,
    "daily": [
        {
            "dt": f"2024-12-{15 + i}",  # Generate sequential fake dates
            "pop": 20 + i,  # Example precipitation probability
            "uvi": 5 + i,   # Example UV index
            "rain": 0.5 + i * 0.1,  # Increment fake rain value
            "temp": {
                "max": 30 - i, 
                "min": 15 + i,
                "day": 22,
                "morn": 18,
                "eve": 20,
                "night": 16
            },
            "clouds": 10 + i * 5,  # Increment fake cloud coverage
            "sunset": f"2024-12-{15 + i}T17:00:00",
            "sunrise": f"2024-12-{15 + i}T07:00:00",
            "weather": [
                {
                    "id": 800 + i,  # Example weather ID
                    "icon": "clear_day",  # Use static or mapped icons
                    "main": "Clear",
                    "description": "Clear sky"
                }
            ],
            "humidity": 50 + i,
            "pressure": 1010 - i,
            "wind_speed": 5 + i * 0.5,
        }
        for i in range(7)  # Generate fake data for 7 days
    ],
    "current": {
        "dt": "2024-12-15T14:00:00",
        "uvi": 3,
        "rain": None,
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
    "fake":True,
}
