import frappe

def execute():
    vehicles = frappe.db.get_all("Vehicle",pluck="name")
    for v in vehicles:
        vehicle = frappe.get_doc("Vehicle",v)
        vehicle.title = f"{vehicle.make} {vehicle.model}, {vehicle.year}"
        vehicle.save()
    
    frappe.db.commit()