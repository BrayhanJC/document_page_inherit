# -*- coding: utf-8 -*-
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
#    Autor: Brayhan Andres Jaramillo Castaño
#           Juan Camilo Zuluaga Serna
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
import logging
import difflib
from openerp import models, fields, api, _
import datetime
from datetime import datetime

_logger = logging.getLogger(__name__)


class document_page(models.Model):
    _name = "revelaciones"
    _rec_name= 'name'

    _description = "Revelaciones"

    @api.model
    def _fill_year(self):
    	year=[]
        
    	for x in range(1990, 2019):
    		year.append((x, str(x)))

    	_logger.info(year)
    	return year

    year = fields.Selection(_fill_year, 'Year', required=True)
    date = fields.Date('Fecha', required=True)
    name = fields.Char(u'Título',required=True)
    content_ids = fields.One2many('revelaciones.contenido', 'revelaciones_id', 'Contenido')


