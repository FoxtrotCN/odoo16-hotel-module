from odoo import models, fields


class HotelRoom(models.Model):
    _name = 'hotel.room'
    _description = 'Habitación del Hotel'

    name = fields.Char(string='Número / Nombre', required=True)
    room_type = fields.Selection([
        ('simple', 'Simple'),
        ('double', 'Doble'),
        ('suite', 'Suite'),
    ], string='Tipo', required=True)
    floor = fields.Integer('Piso')
    capacity = fields.Integer(string='Capacidad')
    price_per_night = fields.Float(string='Precio por Noche')
    state = fields.Selection([
        ('available', 'Disponible'),
        ('occupied', 'Ocupada'),
        ('maintenance', 'Mantenimiento'),
    ], string='Estado', default='available')
    notes = fields.Text(string='Notas')
    amenity_ids = fields.Many2many('hotel.amenity', string='Comodidades')
    reservation_ids = fields.One2many('hotel.reservation', 'room_id', string='Reservas')
