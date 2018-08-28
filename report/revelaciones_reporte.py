#!/usr/bin/python
# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#    
# 	 Autor: Brayhan Andres Jaramillo Castaño
#			Juan Camilo Zuluaga Serna
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

import datetime
import pytz
import time
from openerp import tools
from openerp.osv import osv
from openerp.report import report_sxw
import logging
_logger = logging.getLogger(__name__)


class revelaciones_reporte(report_sxw.rml_parse):


    def __init__(self, cr, uid, name, context):
        super(revelaciones_reporte, self).__init__(cr, uid, name, context=context)
        self.localcontext.update({
            'time': time,

        })

class report_revelaciones(osv.AbstractModel):
    _name = 'report.document_page_inherit.revelaciones'
    _inherit = 'report.abstract_report'
    _template = 'document_page_inherit.reporte_revelaciones_id'
    _wrapped_report_class = revelaciones_reporte

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
