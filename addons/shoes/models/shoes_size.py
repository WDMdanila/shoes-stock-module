from odoo import models, fields, _


class ShoesSize(models.Model):
    _name = 'shoes.size'

    name = fields.Integer(string=_("Size"), required=True)
