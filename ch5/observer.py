class Observer:
    def update(self, temperature, humidity, pressure):
        pass


class WeatherStation:
    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def set_weather_data(self, temperature, humidity, pressure):
        # When weather data changes, notify all observers
        for observer in self.observers:
            observer.update(temperature, humidity, pressure)


# DisplayDevice observer
class DisplayDevice(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, temperature, humidity, pressure):
        print(f"{self.name} Display")
        print(
            f" - Temperature: {temperature}°C, Humidity: {humidity}%, Pressure: {pressure}hPa"
        )


# WeatherApp observer
class WeatherApp(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, temperature, humidity, pressure):
        print(f"{self.name} App - Weather Update")
        print(
            f" - Temperature: {temperature}°C, Humidity: {humidity}%, Pressure: {pressure}hPa"
        )


def main():
    # Create the WeatherStation
    weather_station = WeatherStation()

    # Create and register observers
    display1 = DisplayDevice("Living Room")
    display2 = DisplayDevice("Bedroom")
    app1 = WeatherApp("Mobile App")

    weather_station.add_observer(display1)
    weather_station.add_observer(display2)
    weather_station.add_observer(app1)

    # Simulate weather data changes
    weather_station.set_weather_data(25.5, 60, 1013.2)
    weather_station.set_weather_data(26.0, 58, 1012.8)


if __name__ == "__main__":
    main()
