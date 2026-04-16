from odoo import models, fields


class HotelGuest(models.Model):
    _name = 'hotel.guest'
    _description = 'Huesped del Hotel'
    _inherits = {'res.partner': 'partner_id'}

    partner_id = fields.Many2one(
        'res.partner',
        string='Contacto',
        required=True,
        ondelete='cascade'
    )
    membership_number = fields.Char(string='Numero de Membresia')
    special_requests = fields.Text(string='Solicitudes Especiales')
