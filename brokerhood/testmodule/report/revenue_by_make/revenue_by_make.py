# Copyright (c) 2025, TEI and contributors
# For license information, please see license.txt

import frappe
from frappe import _


def execute(filters: dict | None = None):
	"""Return columns and data for the report.

	This is the main entry point for the report. It accepts the filters as a
	dictionary and should return columns and data. It is called by the framework
	every time the report is refreshed or a filter is updated.
	"""

	print("----"*10)
	print(filters)
	columns = get_columns()
	data = get_data()

	chart = {
		"data":{
		"labels":[x.make for x in data],
		"datasets":[
			{
				"values":[x.total_revenue for x in data]
			}
		],
		# "colors":["#666","#982" ]
		},
		
		"type":"donut"
	}
	return columns, data , "This is third argus" , chart

def get_columns() -> list[dict]:
	"""Return columns for the report.

	One field definition per column, just like a DocType field definition.
	"""
	return [{
		"fieldname":"make",
		"lable":"Make",
		"fieldtype":"Data"
			 },
			 {
		"fieldname":"total_revenue",
		"lable":"Total Revenue",
		"fieldtype":"Currency",
		"options":"AED"
			 },
			 ]


def get_data() -> list[list]:
	"""Return data for the report.

	The report data is a list of rows, with each row being a list of cell values.
	"""

	data = frappe.get_all(
		"Ride Booking",
		fields =["SUM(amount) AS total_revenue","vehicle.make"],
		filters={"docstatus":1},
		group_by="make")
	return data

	
