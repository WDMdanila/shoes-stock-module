from odoo import models, fields, _


class ShoesStatus(models.Model):
    _name = 'shoes.status'

    name = fields.Char(string=_("Status"), required=True)
    shoes_ids = fields.One2many('shoes.shoe', 'brand_id', string=_("Shoes"))
