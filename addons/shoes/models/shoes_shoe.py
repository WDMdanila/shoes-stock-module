from odoo import models, fields, _


class ShoesShoe(models.Model):
    _name = 'shoes.shoe'
    _inherit = ['mail.thread']

    size_ids = fields.Many2many("shoes.size", string=_("Sizes"))
    length = fields.Float(string=_("Length"))
    model_ids = fields.Many2many("shoes.model", string=_("Models"))
    model_type_ids = fields.Many2many("shoes.model.type", string=_("Model Types"))
    brand_id = fields.Many2one("shoes.brand", string=_("Brand"))
    place_id = fields.Many2one("shoes.place", string=_("Place"), track_visibility='onchange')
    status_id = fields.Many2one("shoes.status", string=_("Status"), track_visibility='onchange')
    links = fields.Text(string=_("Links"))
    notes = fields.Text(string=_("Notes"), track_visibility='onchange')
