# Copyright (c) 2024, Parwati Bai and contributors
# For license information, please see license.txt

import frappe
import random
from frappe.model.document import Document
from frappe import _

class AirplaneTicket(Document):
    def validate(self):
        if not self.price:
            frappe.throw("Please provide a price")

        total_amount = 0
        for item in self.items:
            total_amount += item.amount

        self.total_amount = total_amount + self.price

    def before_submit(self):
        if self.status != "Boarded":
            frappe.throw("The ticket can only be submitted if the status is 'Boarded'.")

    def before_insert(self):
        random_number = random.randint(1, 99)
        random_letter = random.choice('ABCDE')
        self.seat = f"{random_number} {random_letter}"


def validate_ticket_creation(doc, method):

    def check_airplane_capacity(self):
        """Check if the number of tickets exceeds the airplane's capacity."""
        # Ensure airplane is set
        if not self.airplane:
            frappe.throw("Airplane is not specified for this ticket.")

        # Fetch the airplane document
        airplane = frappe.get_doc('Airplane', self.airplane)
        airplane_capacity = airplane.capacity

        current_tickets = frappe.db.count('Airplane Ticket', {
            'flight': self.flight,
            'ticket_status': 'Booked'
        })

        # Throw an error if current tickets exceed or match the airplane capacity
        if current_tickets >= airplane_capacity:
            frappe.throw(f"The airplane for this flight has a capacity of {airplane_capacity} seats, and all seats are already booked.")

    def assign_random_seat(self):
        """Assign a random seat to the ticket before insert."""
        random_number = random.randint(1, 99)
        random_letter = random.choice('ABCDE')
        self.seat = f"{random_number}{random_letter}"
