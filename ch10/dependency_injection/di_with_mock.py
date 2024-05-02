from typing import Protocol


class WeatherApi(Protocol):
    def fetch_weather(self, location):
        """Fetch weather data for a given location"""
        ...


class RealWeatherApi:
    def fetch_weather(self, location):
        # In a real scenario, this method would perform
        # an API call to a weather service
        return f"Real weather data for {location}"


class MockWeatherApi:
    def fetch_weather(self, location):
        # Return a fixed response that can be used in tests
        return f"Mock weather data for {location}"


class WeatherService:
    def __init__(self, weather_api: WeatherApi):
        self.weather_api = weather_api

    def get_weather(self, location):
        return self.weather_api.fetch_weather(location)


if __name__ == "__main__":
    real_weather_service = WeatherService(RealWeatherApi())
    print(real_weather_service.get_weather("Paris"))
