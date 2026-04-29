from odoo import models, fields


class HotelReservation(models.Model):
    _name = 'hotel.reservation'
    _description = 'Reserva de Hotel'

    name = fields.Char(string='Referencia', required=True)
    guest_id = fields.Many2one('hotel.guest', string='Huésped', required=True)
    room_id = fields.Many2one('hotel.room', string='Habitación', required=True)
    check_in = fields.Date(string='Check-in', required=True)
    check_out = fields.Date(string='Check-out', required=True)
    state = fields.Selection(
        [
            ('draft', 'Borrador'),
            ('confirmed', 'Confirmada'),
            ('checked_in', 'En curso'),
            ('checked_out', 'Finalizada'),
            ('cancelled', 'Cancelada'),
        ], string='Estado', default='draft'
    )
    notes = fields.Text(string='Notas')
