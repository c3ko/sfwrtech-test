
class CalendarDay:

    def __init__(self, date, customer_slot_limit):
        self.date = date
        # 48 half-hour time slots
        self.time_slots = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.customer_slot_limit = customer_slot_limit


    def view_available_slots(self):
        hours_string = "hour O: "
        for i in range(len(self.time_slots)):
            if (i % 2 == 0) and i > 0:
                hours_string +=f"\nhour {i}"
            hours_string += "O " if 0 <= self.time_slots[i] < 2 else "X "

        return hours_string

    def book_time_slots(self, time_start: float, time_end: float):

        if self.check_if_time_slot_open(time_start, time_end):
            for i in range(int(time_start*2), int(time_end * 2) + 1):
                self.time_slots[i] +=1

    def free_time_slots(self, time_start, time_end):
        for i in range(int((time_start * 2)), int(time_end * 2) + 1):
            self.time_slots[i] -=1

    def check_if_time_slot_open(self, time_start: float, time_end: float):
        """

        :param time_start: time starting slot from 0-47 with 0 being 00:00 in HH:MM for 24 hour clock, 1 being 00:30, 2 being 01:00
        :param time_end: same format as time_start, but for ending time slot
        :return: True if open, False otherwise
        """
        for i in range(int(time_start * 2), int(time_end * 2) + 1):
            if self.time_slots[i] >= self.customer_slot_limit:
                return False
        return True


