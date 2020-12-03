
from data_classes.appointment import Appointment
from data_classes.calendar_day import CalendarDay
from data_classes.customer import Customer
from data_classes.repair_shop import RepairShop
from data_classes.service import Service
from data_classes.vehicle import Vehicle

def test_available_books_open_hours():
    """
    Test if time slot inside working hours is unavailable if time slot is fully booked
    Requirements:
        - 4.4.2 Set Working Hours
        - 4.1.1 Viewing available times on Calendar

    """
    operating_hours = {'open_time': 10, 'close_time': 19.5}
    repair_shop = RepairShop(operating_hours=operating_hours, customer_slot_limit=2)

    calendar_day = CalendarDay(date='12/1/2020', customer_slot_limit=repair_shop.customer_slot_limit)

    # Book one appointments for time slot
    calendar_day.book_time_slots(time_start=11, time_end=12.5)

    assert calendar_day.check_if_time_slot_open(time_start=11, time_end=12) == True

def test_no_available_bookings_closed_hours():
    """
    Test if time slot outside working hours is unavailable
    Requirements:
        - 4.4.2 Set working hours
        - 4.1.1 Viewing available times on Calendar

    """

    operating_hours = {'open_time': 10, 'close_time': 19.5}
    repair_shop = RepairShop(operating_hours=operating_hours, customer_slot_limit=2)

    calendar_day = CalendarDay(date='12/1/2020', customer_slot_limit=repair_shop.customer_slot_limit)

    #Time is entered as float in 24 hour time with half our increments. Ex: 14.5 is 2:30 PM

    #Set time outside at 6:30 AM, which is before the 10:00AM start time
    assert calendar_day.check_if_time_slot_open(time_start=6.5, time_end=7.5) == True

def test_no_available_bookings_full():
    """
    Test if time slot inside working hours is unavailable if time slot is fully booked
    Requirements:
        - 4.4.2 Set working hours
        - 4.1.1 Viewing available times on Calendar

    """
    operating_hours = {'open_time': 10, 'close_time': 19.5}
    repair_shop = RepairShop(operating_hours=operating_hours, customer_slot_limit=2)


    calendar_day = CalendarDay(date='12/1/2020', customer_slot_limit=repair_shop.customer_slot_limit)

    # Book two appointments for same time slot
    calendar_day.book_time_slots(time_start=11, time_end=12.5)
    calendar_day.book_time_slots(time_start=11, time_end=12.5)

    assert calendar_day.check_if_time_slot_open(time_start=11, time_end=12) == False


def test_select_vehicle_exists():
    """
    Test user selecting from list of available vehicles, if vehicle model is Found then is Vehicle object matching year, make ,model
    other wise none
        - 4.2.2 Vehicle selection

    """
    year = "2011"
    make = "Toyota"
    model = "Sienna"

    vehicle: Vehicle = Appointment.select_vehicle(year=year, make=make, model=model)

    assert vehicle.make == make and vehicle.model == model and vehicle.year == year

def test_select_vehicle_not_exists():
    """
    Test user selecting from list of available vehicles, if vehicle model is Found then is Vehicle object matchin year, make ,model
    other wise none
        - 4.2.2 Vehicle selection

    """
    year = "2024"
    make = "Toyota"
    model ="Tundra"

    vehicle: Vehicle = Appointment.select_vehicle(year=year, make=make, model=model)

    assert vehicle == None

def test_select_existing_service():
    """
        4.2.1.1 Select from the drop down list of common repairs
    """
    customer = Customer('mk@gmail.com', 'blah', '416-948-1912', 'Mohamed', "K")
    vehicle = Vehicle('2012', 'Toyota', 'Corolla')

    appointment = Appointment(customer=customer, vehicle=vehicle, current_mileage="127000", calender_date="12/1/2020", start_time=13.5)

    # add brake service to appointment from list of existing services
    appointment.add_service_to_appointment(0)

    assert appointment.service.service_type == "Brake Service"


def test_add_custom_service():
    """
        4.2.1.2 Select from the drop down list of common repairs
    """
    customer = Customer('mk@gmail.com', 'blah', '416-948-1912', 'Mohamed', "K")
    vehicle = Vehicle('2012', 'Toyota', 'Corolla')

    appointment = Appointment(customer=customer, vehicle=vehicle, current_mileage="127000", calender_date="12/1/2020", start_time=13.5)
    appointment.add_custom_service(service_type="Change Blinker Fluid", service_description="Change the blinker fluids and replace filter")

    assert appointment.service.service_type == "Change Blinker Fluid" and appointment.service.service_description == "Change the blinker fluids and replace filter"

def test_add_contact_information():
    """
        Requirements: 4.2.3 Add contact information
    """
    customer = Customer('mk@gmail.com', 'blah', '416-948-1912', 'Mohamed', "K")
    vehicle = Vehicle('2012', 'Toyota', 'Corolla')

    appointment = Appointment(customer=customer, vehicle=vehicle, current_mileage="127000", calender_date="12/1/2020",
                              start_time=13.5)
    appointment.add_custom_service(service_type="Change Blinker Fluid",
                                   service_description="Change the blinker fluids and replace filter")

    appointment.customer.modify_contact_information(phone="416-111-2222", email="mcmaster@mcmaster.ca")

    assert appointment.customer.phone == "416-111-2222" and appointment.customer.email == "mcmaster@mcmaster.ca"

def test_modify_repair_type():
    """
        Requirements: 4.2.4 Add contact information
    """
    customer = Customer('mk@gmail.com', 'blah', '416-948-1912', 'Mohamed', "K")
    vehicle = Vehicle('2012', 'Toyota', 'Corolla')

    appointment = Appointment(customer=customer, vehicle=vehicle, current_mileage="127000", calender_date="12/1/2020",
                              start_time=13.5)
    appointment.add_custom_service(service_type="Change Blinker Fluid",
                                   service_description="Change the blinker fluids and replace filter")

    appointment.change_service_in_appointment(service_id=2)

    assert appointment.service.service_type == "Engine Inspection"


def test_customer_book_appointment():
    """
        Requirements: 4.2.5 Service Request Finalization
    """
    operating_hours = {'open_time': 10, 'close_time': 19.5}
    repair_shop = RepairShop(operating_hours=operating_hours, customer_slot_limit=2)

    calendar_day = CalendarDay(date='12/1/2020', customer_slot_limit=repair_shop.customer_slot_limit)

    customer = Customer('mk@gmail.com', 'blah', '416-948-1912', 'Mohamed', "K")
    vehicle = Vehicle('2012', 'Toyota', 'Corolla')

    appointment = Appointment(customer=customer, vehicle=vehicle, current_mileage="127000", calender_date="12/1/2020", start_time=13.5)
    appointment.add_service_to_appointment(service_id=0)
    calendar_day.book_time_slots(time_start=appointment.time, time_end=appointment.time + appointment.service.duration)

    assert calendar_day.time_slots[27] == 1 and calendar_day.time_slots[28] == 1 and calendar_day.time_slots[29] == 1

def test_customer_book_then_cancel_own_appointment():
    """
        Requirements: 4.1.2 Cancel Appointment
    """
    operating_hours = {'open_time': 10, 'close_time': 19.5}
    repair_shop = RepairShop(operating_hours=operating_hours, customer_slot_limit=2)

    calendar_day = CalendarDay(date='12/1/2020', customer_slot_limit=repair_shop.customer_slot_limit)

    customer = Customer('mk@gmail.com', 'blah', '416-948-1912', 'Mohamed', "K")
    vehicle = Vehicle('2012', 'Toyota', 'Corolla')

    appointment = Appointment(customer=customer, vehicle=vehicle, current_mileage="127000", calender_date="12/1/2020", start_time=13.5)
    appointment.add_service_to_appointment(service_id=0)
    calendar_day.book_time_slots(time_start=appointment.time, time_end=appointment.time + appointment.service.duration)
    calendar_day.free_time_slots(time_start=appointment.time, time_end=appointment.time + appointment.service.duration)
    assert calendar_day.time_slots[27] == 0 and calendar_day.time_slots[28] == 0 and calendar_day.time_slots[29] == 0
