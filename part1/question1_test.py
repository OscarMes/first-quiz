import pytest
from question1 import get_city_weather

def test_get_city_weather_quito():
    assert get_city_weather("Quito") == "22 degrees and sunny"

def test_get_city_weather_sao_paulo():
    assert get_city_weather("Sao Paulo") == "17 degrees and cloudy"

def test_get_city_weather_san_francisco():
    with pytest.raises(TypeError):
        get_city_weather("San Francisco")

def test_get_city_weather_new_york():
    assert get_city_weather("New York") == "14 degrees and rainy"
