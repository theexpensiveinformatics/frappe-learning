# Copyright (c) 2025, TEI and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Drivers(Document):

	def before_save(self):
		self.full_name = f"{self.first_name} {self.last_name}"

	def send_alert(self):
		print('sending message')

# hooks  -> whenever document is updated : make sure you set first + last = full name
# hook and add your own code

