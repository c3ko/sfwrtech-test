from data_classes.service import Service
from data_classes.vehicle import Vehicle


class Recall:

    def __init__(self, recall_description, service, vehicles = []):
        self.recall_description = recall_description
        self.service: Service = service
        self.vehicles : list[Vehicle] = vehicles


    def add_vehicle_to_recall_list(self, vehicle):
        self.vehicles.append(vehicle)

    def check_if_vehicle_belongs_to_recall_list(self, vehicle):
        for recall_vehicle in self.vehicles:
            # checks if make, model, year are same. See implemented __eq__ in vehicle.py
            if recall_vehicle == vehicle:
                return True
        return False

    def update_recall_from_transport_canada_recall_database(self, database):
        """
        update the number
        :param database: a list containing recall information with an entry example:
        {vehicles_affected: [make: 'Toyota', model: 'Corolla', years_affected: [2008, 2009, 2010]], title: 'Faulty Seatbelt' , desc: 'Seatbelt requires replacing due to manufacturing error'}
        """
        for entry in database:
            for affected_vehicle in entry.vehicles_affected:
                for vehicle in self.vehicles:
                    for affected_year in affected_vehicle['years_affected']:
                        if not (vehicle.make == affected_vehicle['make'] and vehicle.model == affected_vehicle['model'] and vehicle.year == affected_year):
                            self.vehicles.append(Vehicle(year=affected_year, model=affected_vehicle['model'], make=affected_vehicle['make']))

