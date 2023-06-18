import data
import sender_stand_request

# Тест 1. Успешное создание поста со всеми параметрами

def test_create_new_post_success():
    post_body_with_id = data.post_body.copy()
    post_body_with_id["id"] = 500
    create_new_post_response = sender_stand_request.create_new_post(post_body_with_id)
    assert create_new_post_response.status_code == 201
    assert create_new_post_response.json()["userId"] == post_body_with_id["userId"]
    # Сейчас все новые посты создаются с id 101, поэтому проверяем, что в любом случае новому посту присвоится id 101.
    assert create_new_post_response.json()["id"] == 101
    assert create_new_post_response.json()["title"] == post_body_with_id["title"]
    assert create_new_post_response.json()["body"] == post_body_with_id["body"]


# Тест 2. Успешное создание поста без параметра id

def test_create_new_post_without_id_success():
    create_new_post_response = sender_stand_request.create_new_post(data.post_body)
    assert create_new_post_response.status_code == 201
    assert create_new_post_response.json()["userId"] == data.post_body["userId"]
    assert create_new_post_response.json()["id"] == 101
    assert create_new_post_response.json()["title"] == data.post_body["title"]
    assert create_new_post_response.json()["body"] == data.post_body["body"]


# Тест 3. Нельзя создать пост без обязательного параметра userId

def test_create_new_post_without_userid_error():
    post_body_without_userid = data.post_body.copy()
    post_body_without_userid.pop("userId")
    create_new_post_response = sender_stand_request.create_new_post(post_body_without_userid)
    # Будем считать, что в негативных проверках должен вернуться код ошибки 400 (нет указаний на то, какой код должен быть на самом деле)
    assert create_new_post_response.status_code == 400


# Тест 4. Нельзя создать пост без обязательного параметра title

def test_create_new_post_without_title_error():
    post_body_without_title = data.post_body.copy()
    post_body_without_title.pop("userId")
    create_new_post_response = sender_stand_request.create_new_post(post_body_without_title)
    # Будем считать, что в негативных проверках должен вернуться код ошибки 400 (нет указаний на то, какой код должен быть на самом деле)
    assert create_new_post_response.status_code == 400


# Тест 5. Нельзя создать пост без обязательного параметра body

def test_create_new_post_without_body_error():
    post_body_without_body = data.post_body.copy()
    post_body_without_body.pop("userId")
    create_new_post_response = sender_stand_request.create_new_post(post_body_without_body)
    # Будем считать, что в негативных проверках должен вернуться код ошибки 400 (нет указаний на то, какой код должен быть на самом деле)
    assert create_new_post_response.status_code == 400

# Тест 6. Нельзя создать набор при неверном типе параметра userId
# Передадим неверный типа параметра userId - строку.
def test_create_new_post_incorrect_type_userId_error():
     post_body_with_incorrect_type_userId = data.post_body.copy()
     post_body_with_incorrect_type_userId["userId"] = "String"
     create_new_post_response = sender_stand_request.create_new_post(post_body_with_incorrect_type_userId)
     assert create_new_post_response.status_code == 400

# Тест 7. Нельзя создать набор при неверном типе параметра title
# Передадим неверный типа параметра title - число.
def test_create_new_post_incorrect_type_title_error():
     post_body_with_incorrect_type_title = data.post_body.copy()
     post_body_with_incorrect_type_title["title"] = 12345
     create_new_post_response = sender_stand_request.create_new_post(post_body_with_incorrect_type_title)
     assert create_new_post_response.status_code == 400

# Тест 8. Нельзя создать набор при неверном типе параметра body
# Передадим неверный типа параметра body - число.
def test_create_new_post_incorrect_type_body_error():
     post_body_with_incorrect_type_body = data.post_body.copy()
     post_body_with_incorrect_type_body["body"] = 12345
     create_new_post_response = sender_stand_request.create_new_post(post_body_with_incorrect_type_body)
     assert create_new_post_response.status_code == 400

# Тест 9. Нельзя создать набор с пустым значением в параметре title

def test_create_new_post_empty_title():
    post_body_with_empty_title = data.post_body.copy()
    post_body_with_empty_title["title"] = ""
    create_new_post_response = sender_stand_request.create_new_post(post_body_with_empty_title)
    assert create_new_post_response.status_code == 400

# Тест 10. Нельзя создать набор с пустым значением в параметре body

def test_create_new_post_empty_body():
    post_body_with_empty_body = data.post_body.copy()
    post_body_with_empty_body["body"] = ""
    create_new_post_response = sender_stand_request.create_new_post(post_body_with_empty_body)
    assert create_new_post_response.status_code == 400

