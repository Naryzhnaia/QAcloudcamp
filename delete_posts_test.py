import data
import sender_stand_request

# Тест 1. Успешное удаление поста по id

def test_delete_post_success():
    for id_post_int in data.post_list:
        id_post = str(id_post_int)
        delete_post_response = sender_stand_request.delete_new_post(id_post)
        assert delete_post_response.status_code == 200

# Тест 2. Нельзя удалить несуществующий пост

def test_delete_unreal_post_error():
    delete_post_response = sender_stand_request.delete_new_post("501")
    assert delete_post_response.status_code == 404

