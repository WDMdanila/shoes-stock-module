from odoo import models, fields, _


class ShoesModelType(models.Model):
    _name = 'shoes.model.type'

    name = fields.Char(string=_("Type"), required=True)
