class Customer:

    def __init__(self, email, password, phone, first_name, last_name):
        self.phone = phone
        self.password = password
        self.email = email
        self.last_name = last_name
        self.first_name = first_name

    def __eq__(self, other):
        return self.phone == other.phone and self.password == other.password and self.email == other.email and self.last_name == other.last_name and self.first_name == other.first_name


    def modify_contact_information(self, phone=None, email=None):
        if phone is not None:
            self.phone = phone

        if email is not None:
            self.email = email