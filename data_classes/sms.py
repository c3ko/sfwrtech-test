from data_classes.appointment import Appointment
from data_classes.customer import Customer
from data_classes.recall import Recall
import math

class SMS:

    def __init__(self, customer: Customer, release_time):
        self.message: str = None
        self.release_time: str = release_time
        self.customer: Customer = customer
        self.has_been_sent: bool = False

    def generate_appointment_reminder_message(self, appointment: Appointment):

        self.message =  f"""Hi Mr/Ms. {self.customer.first_name} {self.customer.last_name},
                            This is a reminder that you have an appointment to service your vehicle:
                            Vehicle: {appointment.vehicle.year} {appointment.vehicle.make} {appointment.vehicle.model}
                            Time: {appointment.calendar_date} at {math.floor(appointment.time)}:{"00" if math.modf(appointment.time) == 0 else "30"}
                        """

    def generate_recall_notification_message(self, recall: Recall):
        self.message =  f"""Hi Mr/Ms. {self.customer.first_name} {self.customer.last_name},
                            This is a notice that there is a Recall notice for one of your vehicles:
                            Recall Campaign: {recall.recall_description}
                        """


    def send_sms_message(self):
        self.has_been_sent = True