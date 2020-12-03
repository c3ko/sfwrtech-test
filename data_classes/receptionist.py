from data_classes.staff_member import StaffMember


class Receptionist(StaffMember):

    def __init__(self, username, name, password, role, permissions, extension):
        super().__init__(username, name, password, role, permissions)
        self.extension = extension


