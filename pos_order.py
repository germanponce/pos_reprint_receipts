# -*- coding: utf-8 -*-
# Coded by German Ponce Dominguez 
#     ▬▬▬▬▬.◙.▬▬▬▬▬  
#       ▂▄▄▓▄▄▂  
#    ◢◤█▀▀████▄▄▄▄▄▄ ◢◤  
#    █▄ █ █▄ ███▀▀▀▀▀▀▀ ╬  
#    ◥ █████ ◤  
#     ══╩══╩═  
#       ╬═╬  
#       ╬═╬ Dream big and start with something small!!!  
#       ╬═╬  
#       ╬═╬ You can do it!  
#       ╬═╬   Let's go...
#    ☻/ ╬═╬   
#   /▌  ╬═╬   
#   / \
# Cherman Seingalt - german.ponce@outlook.com

from odoo import api, fields, models, _, tools, SUPERUSER_ID
from odoo.exceptions import UserError
from datetime import date, datetime, timedelta

import logging
_logger = logging.getLogger(__name__)

class PosOrder(models.Model):
    _inherit ='pos.order'

    def get_lots_name(self, orderline):
        pack_lots_name = ""
        if orderline.pack_lot_ids:
            for lot in orderline.pack_lot_ids:
                if lot.lot_name not in pack_lots_name:
                    pack_lots_name = pack_lots_name+", "+lot.lot_name if pack_lots_name else lot.lot_name
        return pack_lots_name

class PosOrderLine(models.Model):
    _inherit ='pos.order.line'

    def get_lots_name(self):
        pack_lots_name = ""
        for line in self:
            if line.pack_lot_ids:
                for lot in line.pack_lot_ids:
                    if lot.lot_name not in pack_lots_name:
                        pack_lots_name = pack_lots_name+", "+lot.lot_name if pack_lots_name else lot.lot_name
        return pack_lots_name
