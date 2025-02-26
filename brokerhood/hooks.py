app_name = "brokerhood"
app_title = "Brokerhood"
app_publisher = "TEI"
app_description = "Manage Rentals in Frappe"
app_email = "tei@yopmail.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "brokerhood",
# 		"logo": "/assets/brokerhood/logo.png",
# 		"title": "Brokerhood",
# 		"route": "/brokerhood",
# 		"has_permission": "brokerhood.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/brokerhood/css/brokerhood.css"
# app_include_js = "/assets/brokerhood/js/brokerhood.js"

# include js, css files in header of web template
# web_include_css = "/assets/brokerhood/css/brokerhood.css"
# web_include_js = "/assets/brokerhood/js/brokerhood.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "brokerhood/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "brokerhood/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# automatically load and sync documents of this doctype from downstream apps
# importable_doctypes = [doctype_1]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "brokerhood.utils.jinja_methods",
# 	"filters": "brokerhood.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "brokerhood.install.before_install"
# after_install = "brokerhood.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "brokerhood.uninstall.before_uninstall"
# after_uninstall = "brokerhood.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "brokerhood.utils.before_app_install"
# after_app_install = "brokerhood.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "brokerhood.utils.before_app_uninstall"
# after_app_uninstall = "brokerhood.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "brokerhood.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Vehicle": "brokerhood.api.get_query_conditions_for_vehicle",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"ToDo": {
#         "before_insert":"brokerhood.api.throw_emoji"
# 	}
# }

# Scheduled Tasks
# ---------------

scheduler_events = {
    "cron": {  # "cron" should be lowercase
        "30 15 * * 3": [
            "brokerhood.api.send_payment_remainders"
        ]
    }
}

# Testing
# -------

# before_tests = "brokerhood.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "brokerhood.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "brokerhood.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["brokerhood.utils.before_request"]
# after_request = ["brokerhood.utils.after_request"]

# Job Events
# ----------
# before_job = ["brokerhood.utils.before_job"]
# after_job = ["brokerhood.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"brokerhood.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

