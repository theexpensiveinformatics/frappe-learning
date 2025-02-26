import frappe

@frappe.whitelist(allow_guest = True)
def get_emoji():
    return "🤑"

def throw_emoji(doc,event):
    frappe.throw("🤑")

def send_payment_remainders():
    frappe.log_error("Cron job executed", "send_payment_remainders")

def my_function_submit_100_invoices():
    pass

# def get_query_conditions_for_vehicle(user):
#     return "name = 1"