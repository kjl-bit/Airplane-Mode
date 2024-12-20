# Copyright (c) 2024, PUB and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Demo(Document):
    def validate(self):
        if len(self.contact) > 10:
            frappe.throw("Contact number cannot be more than 10 digits.")

