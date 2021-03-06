# -*- coding: utf-8 -*-
from openerp import models, fields, api


class StockTransferDetailsItems(models.TransientModel):

    _inherit = 'stock.transfer_details_items'
    _description = 'Adjust Description field in all Transfer views'

    new_description = fields.Char(
        related='product_id.product_tmpl_id.name',
        string="Description",
        readonly=True,
        store=True,
    )





