from odoo import models, fields


class HotelAmenity(models.Model):
    _name = 'hotel.amenity'
    _description = 'Comodidad del Hotel'

    name = fields.Char(string='Nombre', required=True)
    description = fields.Text(string='Descripción')
