from data_classes.recall import  Recall
from data_classes.appointment import Appointment
from data_classes.calendar_day import CalendarDay
from data_classes.customer import Customer
from data_classes.repair_shop import RepairShop
from data_classes.service import Service
from data_classes.sms import SMS
from data_classes.vehicle import Vehicle

def test_generated_sms_notification_recall():
    """
    Requirement 4.3.2 send SMS Appointment Reminder to Customer
    """
    customer = Customer('mk@gmail.com', 'blah', '416-948-1912', 'Mohamed', "K")

    sms = SMS(customer=customer, release_time=26)
    vehicle = Vehicle('2010', 'Toyota', 'Corolla')
    service = Service(service_type='Recall', service_description='Seatbelt requires replacing due to manufacturing error',
            duration=1, parts_required=['airbag'])
    recall= Recall(recall_description="Seatbelt requires replacing due to manufacturing error", service=service, vehicles=[vehicle])

    sms.generate_recall_notification_message(recall=recall)
    expected_message = """Hi Mr/Ms. Mohamed K,
                            This is a notice that there is a Recall notice for one of your vehicles:
                            Recall Campaign: Seatbelt requires replacing due to manufacturing error
                        """
    assert sms.message == expected_message


def test_generated_sms_notification_appointment():
    """
    Requirement 4.3.2 send SMS Appointment Reminder to Customer

    """
    vehicle = Vehicle('2010', 'Toyota', 'Corolla')

    customer = Customer('mk@gmail.com', 'blah', '416-948-1912', 'Mohamed', "K")

    service = Service(
                service_type='Front Washer Pump Replacement',
                service_description='Replace Replace Windshield Washer Pump',
                duration=2,
                parts_required=['Windshield Washer Pump']
    ),

    appointment = Appointment(customer=customer, vehicle=vehicle, current_mileage="127,000", calender_date="12/1/2020", start_time=11.5)
    sms = SMS(customer=customer, release_time=13)
    sms.generate_appointment_reminder_message(appointment)

    assert sms.message == """Hi Mr/Ms. Mohamed K,
                            This is a reminder that you have an appointment to service your vehicle:
                            Vehicle: 2010 Toyota Corolla
                            Time: 12/1/2020 at 11:30
                        """


def test_check_and_update_recall_status():

    """
        Requirement 4.3.2 send SMS Appointment Reminder to Customer

    """
    recall_database = [
        {'recall_id': 1, 'vehicles_affected': [{'make': 'Toyota', 'model': 'Corolla', 'year_affected': [2008, 2009, 2010]}],
         'title': 'Faulty Seatbelt', 'description': 'Seatbelt requires replacing due to manufacturing error' },
    ]

    vehicle = Vehicle('2010', 'Toyota', 'Corolla')
    service = Service(service_type='Recall', service_description='Seatbelt requires replacing due to manufacturing error',
            duration=1, parts_required=['airbag'])
    recall= Recall(recall_description="Seatbelt requires replacing due to manufacturing error", service=service, vehicles=[vehicle])

    assert recall.check_if_vehicle_belongs_to_recall_list(vehicle)


