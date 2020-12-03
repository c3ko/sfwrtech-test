from data_classes.receptionist import Receptionist
from data_classes.repair_shop import RepairShop

operating_hours = {'open' : 10, 'close': 19.5}
repair_shop = RepairShop(operating_hours=operating_hours, customer_slot_limit=2)


def test_set_working_hours():
    """
    Requirements: 4.4.2 Set working hours
    """
    repair_shop.change_operating_hours(store_open=11, close=20)

    assert repair_shop.operating_hours['open'] == 11 and repair_shop.operating_hours['close'] == 20

def test_set_customer_per_time_slot_limit():
    """
    Requirements: 4.4.3 Set limit on number of customers per time slot
    """
    repair_shop.change_customer_slot_limit(4)
    assert repair_shop.customer_slot_limit == 4




def test_employee_onboarding():
    """
    Requirements: 4.4.1.2 Employee Onboarding/Registration
    """

    employee = Receptionist(username="marcusl", name='marcus',
                            password='blah', role="Receptionist",
                            permissions=["modify_appointments"],
                            extension=1234
                            )
    repair_shop.onboard_staff_member(username="marcusl", name='marcus',
                            password='blah', role="Receptionist",
                            extension=1234)

    assert repair_shop.receptionists_service_agents[0].username == employee.username

def receptionist_login():
    """
    Requirements: 4.4.1.1 General Login
    """

    repair_shop.onboard_staff_member(username="marcusl", name='marcus',
                            password='blah', role="Receptionist",
                            extension=1234)

    returned_user_from_login = repair_shop.login(username="marcusl", password="blah")
    assert returned_user_from_login.username == 'marcusl'
