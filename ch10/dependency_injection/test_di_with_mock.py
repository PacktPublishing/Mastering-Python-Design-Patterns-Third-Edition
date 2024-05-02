import unittest
from di_with_mock import MockWeatherApi, WeatherService


class TestWeatherService(unittest.TestCase):
    def test_get_weather(self):
        mock_api = MockWeatherApi()
        weather_service = WeatherService(mock_api)
        self.assertEqual(
            weather_service.get_weather("Anywhere"),
            "Mock weather data for Anywhere",
        )


if __name__ == "__main__":
    unittest.main()
