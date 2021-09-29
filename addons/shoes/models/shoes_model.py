from odoo import models, fields, _


class ShoesModel(models.Model):
    _name = 'shoes.model'

    name = fields.Char(string=_("Model"), required=True)
