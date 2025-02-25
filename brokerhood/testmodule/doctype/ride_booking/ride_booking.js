// Copyright (c) 2025, TEI and contributors
// For license information, please see license.txt

frappe.ui.form.on("Ride Booking", {
	refresh(frm) {

	},

	rate(frm){
		//recalculate total
		frm.trigger("update_total_amount");

	},

	update_total_amount(frm){
		let total_distance = 0;
		for(let item of frm.doc.items){
			total_distance += item.distance; 
			// console.log(item.distance)
		}
		const amount = frm.doc.rate * total_distance;
		frm.set_value('amount',amount)
	},

});

frappe.ui.form.on('Ride Booking Item', {
	refresh(frm) {

	},
	distance(frm,cdt,cdn){
		// console.log(cdt,cdn);
		// console.log(frappe.get_doc(cdt,cdn));
		// my_child = frappe.get_doc(cdt,cdn);
		// frappe.model.set_value(cdt,cdn,"source","Update Source") 
		// console.log("Child Table value changed");
		frm.trigger("update_total_amount");

	},

	items_remove(frm){
		frm.trigger("update_total_amount");
	}


})
