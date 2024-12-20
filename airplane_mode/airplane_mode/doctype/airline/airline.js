// Copyright (c) 2024, PUB and contributors
// For license information, please see license.txt

frappe.ui.form.on('Airline', {
    refresh: function(frm) {
        if (frm.doc.website) {
            frm.add_custom_button(__('Visit Website'), function() {
                window.open(frm.doc.website, '_blank'); 
            });
        }
    },

    onload: function(frm) { 
        if (frm.doc.website) {
            frm.add_web_link(__('Visit Official Website'), frm.doc.website);
        }
    }
});

