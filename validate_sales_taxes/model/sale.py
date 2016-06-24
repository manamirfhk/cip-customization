# -*- coding: utf-8 -*-

from openerp.osv import osv, fields
from openerp.tools.translate import _
import openerp.exceptions

class sale_order(osv.osv):
    _inherit = "sale.order"
    
    def action_wait(self, cr, uid, ids, context=None):
        context = context or {}
        for so in self.browse(cr, uid, ids, context=context):
            if so.order_line:
                for line in so.order_line:
                    if not line.tax_id:
                        raise openerp.exceptions.Warning(_('You can not confirm sales order without taxes on order lines.'))
        return super(sale_order, self).action_wait(cr, uid, ids, context)
    
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
