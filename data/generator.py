import random
from faker import Faker
from schemas.models import Booking, BookingDates, BookingNames



class Generator_test_data(Faker):
    def booking(self):
        checkin = self.date_between(start_date="-5y", end_date="today")
        checkout = self.date_between(start_date=checkin, end_date="+1y")

        data = Booking(
            firstname=self.first_name(),
            lastname=self.last_name(),
            totalprice=self.random_int(min=50, max=1000),
            depositpaid=self.boolean(),
            bookingdates=BookingDates(
                checkin=checkin.strftime("%Y-%m-%d"),
                checkout=checkout.strftime("%Y-%m-%d")
            ),
            additionalneeds=random.choice(["Breakfast","Lunch","Dinner"])
        )
        return data.dict()

    def booking_with_name(self):

        checkin = self.date_between(start_date="-5y", end_date="today")
        checkout = self.date_between(start_date=checkin, end_date="+1y")

        data = {
            "totalprice":self.random_int(min=50, max=1000),
            "depositpaid":self.boolean(),
            "bookingdates":{
                "checkin":checkin.strftime("%Y-%m-%d"),
                "checkout":checkout.strftime("%Y-%m-%d")
            },
            "additionalneeds":random.choice(["Breakfast", "Lunch", "Dinner"])
        }
        return data

    def names(self):
        data = BookingNames(
            firstname=self.first_name(),
            lastname=self.last_name(),
        )
        return data.dict()

generator_test_data = Generator_test_data()