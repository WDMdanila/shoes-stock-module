from odoo import models, fields, _


class ShoesBrand(models.Model):
    _name = 'shoes.brand'

    name = fields.Char(string=_("Brand"), required=True)
    shoes_ids = fields.One2many('shoes.shoe', 'brand_id', string=_("Shoes"))
