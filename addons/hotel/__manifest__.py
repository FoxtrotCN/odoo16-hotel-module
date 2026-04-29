{
    'name': 'Hotel',
    'version': '16.0.1.0.0',
    'summary': 'Gestión Hotelera: Habitaciones, huéspedes y reservas',
    'description': 'Gestión Hotelera: Habitaciones, huéspedes y reservas',
    'author': 'Fernando Cedeno',
    'category': 'Services',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/hotel_room_views.xml',
        'views/hotel_amenity_views.xml',
        'views/hotel_reservation_views.xml',

    ],
    'installable': True,
    'application': True,
}
