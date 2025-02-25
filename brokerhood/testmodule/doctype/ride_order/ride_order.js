// Copyright (c) 2025, TEI and contributors
// For license information, please see license.txt

frappe.ui.form.on("Ride Order", {
    onload(frm) {


        console.log('running load...');
    },
    setup(frm){

        console.log("on setup");
    },
    
    refresh(frm) {

        if(frm.doc.status=== "New"){
            frm.add_custom_button("Accept", () => {
                console.log("on refresh");
                // status -> accpeted
                // save the form
                frm.set_value("status", "Accepted");
                frm.save();
            },"Actions")

            frm.add_custom_button("Reject", () => {
                console.log("on refresh");
                // status -> rejected
                // save the form
                frm.set_value("status", "Rejected");
                frm.save();
            },"Actions")
        }

       
    },

    status (frm){
        console.log("status is changed => ",frm.doc.status);
        frm.set_value("status", frm.doc.status);
        frm.save();
    }
});
