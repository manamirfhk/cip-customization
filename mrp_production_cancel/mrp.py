# -*- coding: utf-8 -*-
###########################################################################
#    Module Writen to OpenERP, Open Source Management Solution
#
#    Copyright (c) 2012 Vauxoo - http://www.vauxoo.com
#    All Rights Reserved.
#    info@vauxoo.com
############################################################################
#    Coded by: julio (julio@vauxoo.com)
############################################################################
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp.osv import osv

import openerp.netsvc as netsvc


class mrp_production(osv.Model):
    _inherit = "mrp.production"

    def action_cancel(self, cr, uid, ids, context=None):
        if context is None:
            context = {}

        pick_obj = self.pool.get('stock.picking')
        move_obj = self.pool.get('stock.move')
        for production in self.browse(cr, uid, ids, context=context):
            if production.picking_id.id:
                pick_obj.action_cancel(cr, uid, [production.picking_id.id])
            for move in production.move_lines2:
                account_move_line_id = self.pool.get('account.move.line').search(
                    cr, uid, [('stock_move_id', '=', move.id)])
                if move.product_id.valuation == 'real_time' and not account_move_line_id:
                    raise osv.except_osv(
                        'Warning!',
                        'Cannot cancel manufacturing order without related journal items!'
                    )
                else:
                    move_obj.action_cancel(cr, uid, [move.id])
            if production.move_created_ids2:
                for move in production.move_created_ids2:
                    account_move_line_id2 = self.pool.get('account.move.line').search(
                        cr, uid, [('stock_move_id', '=', move.id)])
                    if move.product_id.valuation == 'real_time' and not account_move_line_id2:
                        raise osv.except_osv(
                            'Warning!',
                            'Cannot cancel manufacturing order without related journal items!'
                        )
                    else:
                        move_obj.action_cancel(cr, uid, [move.id])
        return super(mrp_production, self).action_cancel(cr, uid, ids,
                                                        context=context)


#    def action_cancel(self, cr, uid, ids, context=None):
#        wf_service = netsvc.LocalService("workflow")
#
#        if context is None:
#            context = {}
#
#        move_obj = self.pool.get('stock.move')
#        for production in self.browse(cr, uid, ids, context=context):
#            if production.picking_id.id:
#                wf_service.trg_validate(
#                    uid, 'stock.picking', production.picking_id.id,
#                    'button_cancel', cr)
#            move_obj.action_cancel(cr, uid, [
#                                   x.id for x in production.move_lines2])
#            if production.move_created_ids2:
#                move_obj.action_cancel(cr, uid, [
#                    x.id for x in production.move_created_ids2])
#        return super(mrp_production, self).action_cancel(cr, uid, ids,
#                                                         context=context)
