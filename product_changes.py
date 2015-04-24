import pytz
from openerp import SUPERUSER_ID, workflow
from datetime import datetime
from dateutil.relativedelta import relativedelta
from operator import attrgetter
from openerp.tools.safe_eval import safe_eval as eval
from openerp.osv import fields, osv
from openerp.tools.translate import _
import openerp.addons.decimal_precision as dp
from openerp.osv.orm import browse_record_list, browse_record, browse_null
from openerp.tools import DEFAULT_SERVER_DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT, DATETIME_FORMATS_MAP
from openerp.tools.float_utils import float_compare

class product_template(osv.osv):    
    _inherit = 'product.template'
    
    _columns = {
                'saleprice_method': fields.many2one('product.sale.price','Pricing Category'),
        }
    
    def onchange_pricecategory(self, cr, uid, ids, category_id, cost_price, context=None):
        """
        onchange handler of price category.
        """
        if context is None:
            context = {}

        res = {'value': {'list_price': 1.0,}}
        if not category_id:
            return res
            
        print ids,category_id,cost_price,'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
        price_category = self.pool.get('product.sale.price')
        cp = cost_price
        percent = price_category.browse(cr, uid, category_id).price_increase
        sp = cp + ((percent *cp)/100)      
        res['value'].update({'list_price': sp})

        return res

product_template()


class product_sale_price(osv.osv):    
    _name = 'product.sale.price'
    
    _columns = {
                'name':fields.char('Type Name',required=True),
                'price_increase':fields.float('Percentage of Increase',required=True)
        }

product_sale_price()


