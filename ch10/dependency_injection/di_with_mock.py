from typing import Protocol


class WeatherApiClient(Protocol):
    def fetch_weather(self, location):
        """Fetch weather data for a given location"""
        ...


class RealWeatherApiClient:
    def fetch_weather(self, location):
        return f"Real weather data for {location}"


class WeatherService:
    def __init__(self, weather_api: WeatherApiClient):
        self.weather_api = weather_api

    def get_weather(self, location):
        return self.weather_api.fetch_weather(location)


if __name__ == "__main__":
    ws = WeatherService(RealWeatherApiClient())
    print(ws.get_weather("Paris"))
