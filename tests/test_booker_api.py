import pytest
import allure
from config.base_requests import get_request, post_request, put_request, patch_request, delete_request
from config.endpoints import BOOKING_URL
from data.generator import generator_test_data
from data.temp_response import storage
from schemas.models import BookingIds, BookingResponse, Booking


class TestBookerAPI:
    @allure.feature("Booking API")
    @allure.title("Получение всех ID бронирований")
    def test_get_booking_ids(self):
        response = get_request(url=BOOKING_URL)
        assert response.status_code == 200, f"Статус ответа не соответствует ожиданиям: {response.status_code}"

        bookings = [BookingIds.model_validate(item) for item in response.json()]
        # проверка JSON ответа
        assert len(bookings) > 0
        assert isinstance(bookings[0].bookingid, int)

    @pytest.mark.order(1)
    @allure.feature("Booking API")
    @allure.title("Создание нового бронирования")
    def test_create_booking(self):
        body = generator_test_data.booking()
        response = post_request(url=BOOKING_URL,json=body)
        assert response.status_code == 200, f"Статус ответа не соответствует ожиданиям: {response.status_code}"

        booking_data = BookingResponse.model_validate(response.json())

        # проверка JSON ответа
        assert booking_data.bookingid > 0
        assert booking_data.booking.firstname != ""
        assert isinstance(booking_data.booking.totalprice, int)
        bookingid = response.json()["bookingid"]
        storage.set("booking_id",bookingid)

    @pytest.mark.order(2)
    @allure.feature("Booking API")
    @allure.title("Получение бронирования по ID")
    def test_get_booking_id(self):
        bookingid = storage.get("booking_id")
        response = get_request(url=f"{BOOKING_URL}/{bookingid}")
        assert response.status_code == 200, f"Статус ответа не соответствует ожиданиям: {response.status_code}"
        booking_data = response.json()
        booking = Booking.model_validate(booking_data)

        # проверка JSON ответа
        assert booking.firstname != ""
        assert isinstance(booking.totalprice, int)
        assert booking.depositpaid in [True, False]

    @pytest.mark.order(3)
    @allure.feature("Booking API")
    @allure.title("Полное обновление бронирования")
    def test_update_booking(self, client_headers):
        body = generator_test_data.booking()

        bookingid = storage.get("booking_id")
        response = put_request(url=f"{BOOKING_URL}/{bookingid}", headers=client_headers,json=body)

        assert response.status_code == 200, f"Статус ответа не соответствует ожиданиям: {response.status_code}"
        assert response.json() == body, f"Данные не обновились"
        booking_data = response.json()
        booking = Booking.model_validate(booking_data)

        # проверка JSON ответа
        assert booking.firstname != ""
        assert isinstance(booking.totalprice, int)
        assert booking.depositpaid in [True, False]

    @pytest.mark.order(4)
    @allure.feature("Booking API")
    @allure.title("Частичное обновление данных бронирования")
    def test_partial_update_booking(self, client_headers):
        body = generator_test_data.names()

        bookingid = storage.get("booking_id")
        response = patch_request(url=f"{BOOKING_URL}/{bookingid}", headers=client_headers, json=body)
        assert response.status_code == 200, f"Статус ответа не соответствует ожиданиям: {response.status_code}"

    @pytest.mark.order(5)
    @allure.feature("Booking API")
    @allure.title("Удаление бронирования по ID")
    def test_delete_booking(self, client_headers):
        bookingid = storage.get("booking_id")
        response = delete_request(url=f"{BOOKING_URL}/{bookingid}", headers=client_headers)
        assert response.status_code == 201, f"Статус ответа не соответствует ожиданиям: {response.status_code}"
