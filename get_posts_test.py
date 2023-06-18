import data
import configuration
import sender_stand_request
import requests

# Тест 1. Успешное получение всех постов

def test_get_all_posts_success():
    get_all_posts_response = sender_stand_request.get_all_posts()
    assert get_all_posts_response.status_code == 200
    assert get_all_posts_response.json() == data.all_posts