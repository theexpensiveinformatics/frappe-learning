// Copyright (c) 2025, TEI and contributors
// For license information, please see license.txt

frappe.ui.form.on("Ride Order", {
	refresh(frm) {
        frm.add_custom_button("Accept",()=>{console.log("button clicked")})
	},
});
