// Copyright (c) 2024, PUB and contributors
// For license information, please see license.txt


frappe.ui.form.on('Airplane Ticket', {
    refresh: function(frm) {
        frm.add_custom_button(__('Set Seat Number'), function() {
            let dialog = new frappe.ui.Dialog({
                title: 'Enter Seat Number',
                fields: [
                    {
                        label: 'Seat Number',
                        fieldname: 'seat_number',
                        fieldtype: 'Data',
                        reqd: 1
                    }
                ],
                primary_action_label: 'Set',
                primary_action(values) {
                    frm.set_value('seat', values.seat_number);
                    dialog.hide();
                }
            });

            dialog.show();
        });
    }
});
