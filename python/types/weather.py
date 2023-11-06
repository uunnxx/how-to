from datetime import datetime
from dataclasses import dataclass
from enum import Enum



class Coordinate:
    pass


CELSIUS = float

class WeatherType(str, Enum):
    THUNDERSTORM = 'Groza'
    DRIZZLE = 'Izmoros'
    RAIN = 'DOZHD'
    SNOW = 'SNEG'
    CLEAR = 'YASNO'
    FOG = 'TUMAN'
    CLOUDS = 'OBLACHNO'


@dataclass(slots=True, frozen=True)
class Weather:
    temperature: CELSIUS
    weather_type: WeatherType
    sunrise: datetime
    sunset: datetime
    city: str


def get_weather(coordinates: Coordinate) -> Weather:
    '''Requests weather in OpenWeather API and returns it'''
    return Weather(
        temperature=20,
        weather_type=WeatherType.CLEAR,
        sunrise=datetime.fromisoformat("2022-05-04 04:00:00"),
        sunset=datetime.fromisoformat("2022-05-04 20:25:00"),
        city='Moscow'
    )
