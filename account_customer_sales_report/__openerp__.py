# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (c) Rooms For (Hong Kong) Limited T/A OSCG. All Rights Reserved.
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

{
    'name': 'Customer Sales Report',
    'version': '1.0',
    'category': "Report",
    'summary': 'Adds a report function to print sales by customer',
    'description': """
 * Adds a boolean field 'Customer Sales Report' in account definition screen. \
 The field is expected to be selected for sales accounts that should be considered in amount calculation.
 * Adds a menu item 'Customer Sales Report' which generates a sales report by customer by period 
     """,
    'author': 'Rooms For (Hong Kong) T/A OSCG',
    'depends': ['base','account','report_aeroo_ooo','report_aeroo'],
    'init_xml': [],
    'update_xml': [
        'wizard/customer_sales_wizard.xml',
        'customer_sales.xml',
        'account.xml',
    ],
   
    'demo_xml': [],
    'installable': True,
    'active': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
