from typing import Dict

from data_classes.customer import Customer
from data_classes.receptionist import Receptionist
from data_classes.service import Service
from data_classes.vehicle import Vehicle

existing_vehicles : Dict[int, Vehicle] = {
    0: Vehicle(year='2011', make='Toyota', model='Sienna'),
    1: Vehicle(year='2010', make='Toyota', model='Camry'),
    2: Vehicle(year='2009', make='Hyundai', model='Sonata')
}

class Appointment:



    @staticmethod
    def select_vehicle(year, make, model):

        for key, vehicle in existing_vehicles.items():
            if year == vehicle.year and make == vehicle.make and model == vehicle.model:
                return existing_vehicles[key]
        return None


    def __init__(self, customer, vehicle, current_mileage, calender_date, start_time):

        self.customer = customer
        self.vehicle = vehicle
        self.current_mileage = current_mileage
        self.service: Service = None
        self.calendar_date = calender_date
        self.time = start_time
        self.scheduled = True


        self.existing_services = {
        0: Service(service_type='Brake Service',
                   service_description='Replace Brake Pads and Rotors',
                   duration=2,
                   parts_required=['Brake Pads', 'Brake Rotor'],
                   ),
        1: Service(service_type='Engine Oil Change',
                   service_description='Change Engine Oil and Replace Filter',
                   duration=1,
                   parts_required=['Engine Oil', 'Engine Oil Filter']
                   ),
        2: Service(service_type='Engine Inspection',
                   service_description='Inspect Problem in Engine',
                   duration=1,
                   parts_required=[]
                   ),
        3: Service(service_type='Front Washer Pump Replacement',
                   service_description='Replace Replace Windshield Washer Pump',
                   duration=2,
                   parts_required=['Windshield Washer Pump']
                   ),

    }



    def add_service_to_appointment(self, service_id):
        self.service = self.existing_services[service_id]

    def add_custom_service(self, service_type, service_description):
        # default 1 hour service duration
        self.service = Service(service_type, service_description, 1, None)

    def change_service_in_appointment(self, service_id):
        self.service = self.existing_services[service_id]

    def cancel_appointment(self, user):
        if isinstance(user, Customer) and self.customer == user:
            self.scheduled = False
        elif isinstance(Receptionist) and 'modify_appointments' in user.permissions:
            self.scheduled = True



