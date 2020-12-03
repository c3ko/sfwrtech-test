from data_classes.appointment import Appointment
from data_classes.calendar_day import CalendarDay
from data_classes.customer import Customer
from data_classes.receptionist import Receptionist
from data_classes.staff_member import StaffMember


class RepairShop:

    def __init__(self, operating_hours, customer_slot_limit):
        self.technicians = []
        self.receptionists_service_agents = []
        self.calendar_days : list[CalendarDay] = []
        self.customer_slot_limit = customer_slot_limit
        self.operating_hours = operating_hours
        self.customers: list[Customer] = []
        self.SMS_queue = []
        self.appointments: list[Appointment] = []

    def onboard_staff_member(self, username, password, name, role, extension=None):
        if role == 'Technician':
            self.technicians.append(StaffMember(username, password, name, role))
        elif role == 'Receptionist':
            self.receptionists_service_agents.append(Receptionist(username, password, name, role, permissions=["modify_appointments"], extension=extension))


    def change_operating_hours(self, store_open=None, close=None):
        self.operating_hours['open'] = store_open
        self.operating_hours['close'] = close

    def change_customer_slot_limit(self, new_limit):
        self.customer_slot_limit = new_limit

    def is_store_open(self, current_time):
        return self.operating_hours['close'] > current_time >= self.operating_hours['open']

    def login(self, username, password):
        for receptionist in self.receptionists_service_agents:
            if receptionist.username == username and receptionist.password == password:
                return receptionist

    def add_appointment(self, appointment: Appointment):
        self.appointments.append(appointment)

    def remove_appointment(self, appointment: Appointment):
        self.appointments.remove(appointment)