import allure

from config.base_requests import get_request
from config.endpoints import BASE_URL


class TestHealthCheck:
    @allure.feature("Booking API")
    @allure.title("Запрос HealthCheck")
    def test_get_booking_ids(self):
        response = get_request(url=f"{BASE_URL}/ping")
        assert response.status_code == 201, f"Статус ответа не соответствует ожиданиям: {response.status_code}"

