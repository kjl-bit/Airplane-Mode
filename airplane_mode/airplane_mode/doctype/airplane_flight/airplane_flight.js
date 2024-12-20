// Copyright (c) 2024, PUB and contributors
// For license information, please see license.txt

frappe.ui.form.on('Airplane Flight', {
    validate: function(frm) {
        if (!frm.doc.name) {
            console.log("Missing document name.");
        }
        if (frm.doc.crew_members) {
            const crewCount = frm.doc.crew_members.length;
            frm.set_value('total_crew', crewCount);

            if (crewCount > 5) {
                frappe.validated = false;
            }
        }
    },
    crew_members_add: function(frm) {
        const crewCount = frm.doc.crew_members.length;
        frm.set_value('total_crew', crewCount);
    },
    crew_members_remove: function(frm) {
        const crewCount = frm.doc.crew_members.length;
        frm.set_value('total_crew', crewCount);
    }
});




