import pytest
import allure
from config.base_requests import get_request, post_request, put_request
from config.endpoints import BOOKING_URL
from data.generator import generator_test_data
from data.temp_response import storage


class TestBookerAPINegative:
    @pytest.mark.negative
    @allure.feature("Booking API Negative")
    @allure.title("Создание нового бронирования без имени")
    def test_create_booking(self):
        body = generator_test_data.booking_with_name()
        response = post_request(url=BOOKING_URL,json=body)

        assert response.status_code in (400,500), f"Статус ответа не соответствует ожиданиям: {response.status_code}"

    @pytest.mark.negative
    @allure.feature("Booking API Negative")
    @allure.title("Запрос бронирования с несуществующим ID возвращает 404")
    @pytest.mark.parametrize("bookingid", [0, -1, 999999999, 2_147_483_647])
    def test_get_booking_id(self,bookingid):
        response = get_request(url=f"{BOOKING_URL}/{bookingid}")
        assert response.status_code == 404, f"Статус ответа не соответствует ожиданиям: {response.status_code}"

    @pytest.mark.negative
    @allure.feature("Booking API Negative")
    @allure.title("Запрос бронирования с несуществующим ID возвращает 404")
    @pytest.mark.parametrize("bookingid", [0, -1, 999999999, 2_147_483_647])
    def test_get_booking_id(self, bookingid):
        response = get_request(url=f"{BOOKING_URL}/{bookingid}")
        assert response.status_code == 404, f"Статус ответа не соответствует ожиданиям: {response.status_code}"

    @pytest.mark.negative
    @allure.feature("Booking API Negative")
    @allure.title("Полное обновление бронирования без авторизации")
    def test_update_booking(self, client_headers):
        body = generator_test_data.booking()
        bookingid = storage.get("booking_id")
        response = put_request(url=f"{BOOKING_URL}/{bookingid}", json=body)
        assert response.status_code == 403, f"Статус ответа не соответствует ожиданиям: {response.status_code}"

