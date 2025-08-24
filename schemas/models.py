from pydantic import BaseModel

class BookingIds(BaseModel):
    bookingid: int


class BookingDates(BaseModel):
    checkin: str
    checkout: str

class Booking(BaseModel):
    firstname: str
    lastname: str
    totalprice: int
    depositpaid: bool
    bookingdates: BookingDates
    additionalneeds: str

class BookingResponse(BaseModel):
    bookingid: int
    booking: Booking

class BookingNames(BaseModel):
    firstname: str
    lastname: str