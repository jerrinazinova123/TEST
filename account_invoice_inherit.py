
import math
import openerp.addons.product.product

import logging
import time
import string

from openerp import tools
from openerp.osv import fields, osv
from openerp.tools.translate import _
from datetime import datetime

import openerp.addons.decimal_precision as dp
import openerp.addons.product.product
from openerp.addons.num2words import num2words

from openerp.tools import amount_to_text_en
#from openerp.tools.amount_to_text_en import amount_t

class account_invoice_inherit(osv.osv):
    _inherit='account.invoice'
    _description='Invoice Inherit'

    def _amount_in_words(self, cr, uid, ids, field_name, arg, context=None):
        cur_obj = self.pool.get('res.currency')
        res = {}
        for order in self.browse(cr, uid, ids, context=context):
            taxed = untaxed = 0.0
            res[order.id] = {
                'amount_words': '0.0',
                            }
            val = val1 = 0.0
            cur = order.currency_id
            for line in order.invoice_line:
                val1 += line.price_subtotal
            taxed = cur_obj.round(cr, uid, cur, val)
            untaxed = cur_obj.round(cr, uid, cur, val1)
            total = str(num2words(float(taxed + untaxed)))
            res[order.id] = total
            #res[order.id] = amount_to_text_en.amount_to_text(float(taxed + untaxed))
        return res


    _columns = {
        'amount_words': fields.function(_amount_in_words, string='In Words', type="char", store=True, help="The amount in words"),
                }
account_invoice_inherit()