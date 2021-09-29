from odoo import models, fields, _


class ShoesPlace(models.Model):
    _name = 'shoes.place'

    name = fields.Char(string=_("Place"), required=True)
    shoes_ids = fields.One2many('shoes.shoe', 'place_id', string=_("Shoes"))
