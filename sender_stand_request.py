import configuration
import requests
import data

# Функция для получения постов
def get_all_posts():
    return requests.get(configuration.URL_SERVICE + configuration.POSTS_PATH)

# Функция для создания нового поста
def create_new_post(post_body):
    return requests.post(configuration.URL_SERVICE + configuration.POSTS_PATH,
                         json = post_body)

# Функция для удаления поста по id
def delete_new_post(id_post):
    return requests.delete(configuration.URL_SERVICE + configuration.POSTS_PATH + id_post)