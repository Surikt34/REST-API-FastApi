import requests

BASE_URL = "http://0.0.0.0:8080"


# Функция для создания объявления
def create_advertisement():
    response = requests.post(f"{BASE_URL}/advertisement", json={
        "title": "Тестовое объявление",
        "description": "Это тестовое объявление",
        "price": 100.50,
        "author": "Иван Иванов"
    })
    print(f"Ответ на создание объявления: {response.status_code}")
    print(response.json())


# Функция для получения объявления по его ID
def get_advertisement(ad_id):
    response = requests.get(f"{BASE_URL}/advertisement/{ad_id}")
    print(f"Ответ на получение объявления: {response.status_code}")
    print(response.json())


# Функция для обновления объявления по его ID
def update_advertisement(ad_id):
    response = requests.patch(f"{BASE_URL}/advertisement/{ad_id}", json={
        "title": "Обновленное тестовое объявление",
        "price": 120.00
    })
    print(f"Ответ на обновление объявления: {response.status_code}")
    print(response.json())


# Функция для удаления объявления по его ID
def delete_advertisement(ad_id):
    response = requests.delete(f"{BASE_URL}/advertisement/{ad_id}")
    print(f"Ответ на удаление объявления: {response.status_code}")
    print(response.json())


# Функция для поиска объявлений по заголовку
def search_advertisements():
    response = requests.get(f"{BASE_URL}/advertisement?title=Тест")
    print(f"Ответ на поиск объявлений: {response.status_code}")
    print(response.json())


def main():
    # Создание объявления
    create_advertisement()
    #
    # Получение объявления по ID
    # get_advertisement(1)
    # #
    # # Обновление объявления
    # update_advertisement(1)
    #
    # # Удаление объявления
    # delete_advertisement(1)
    #
    # Поиск объявлений
    search_advertisements()


# Входная точка программы
if __name__ == "__main__":
    main()