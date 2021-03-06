# -*- coding: utf-8 -*-
##########################################################################
#
#   Copyright (c) 2015-Present Webkul Software Pvt. Ltd. (<https://webkul.com/>)
#   See LICENSE file for full copyright and licensing details.
#   License URL : <https://store.webkul.com/license.html/>
#
##########################################################################

from odoo import api, models, fields

class ConnectorSnippet(models.TransientModel):
    _inherit = 'connector.snippet'


    @api.model
    def _get_ecomm_extensions(self):
        """
        create channels at dynamic time for instance
        @params : self
        @return : list
        """
        ecommece_channels = super(ConnectorSnippet,self)._get_ecomm_extensions()
        ecommece_channels.append(('opencart','Opencart'))
        return ecommece_channels

    @api.model
    def get_quantity(self,obj_pro, instance_id):
        """
            to get quantity of product or product template
            @params : product template obj or product obj,instance_id
            @return : quantity in hand or quantity forecasted
        """
        quantity = 0.0
        config_id = self.env['connector.instance'].browse(instance_id)
        qty = obj_pro.with_context()._product_available()
        if config_id.connector_stock_action =="qoh":
            quantity = qty[obj_pro.id]['qty_available']
        else:
            quantity = qty[obj_pro.id]['virtual_available']
        if type(quantity) == str:
            quantity = quantity.split('.')[0]
        if type(quantity) == float:
            quantity = quantity.as_integer_ratio()[0]
        return quantity