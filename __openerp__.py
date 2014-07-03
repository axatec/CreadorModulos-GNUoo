# -*- coding: utf-8 -*-
#/#############################################################################
#
#    BizzAppDev
#    Copyright (C) 2004-TODAY bizzappdev(<http://www.bizzappdev.com>).
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
#/#############################################################################
{
    "name": "OpenERP Module Maker",
    "version": "1.0.6",
    "author": "Ruchir Shukla (Bizzappdev)",
    "website": "http://bizzappdev.com",
    "category": "GenericModules",
    "depends": ["base"],
    "summary": "OpenERP Module Maker",
    "description": """
OpenERP Module Maker/Generator
==============================

OpenERP/Odoo Module which help you to Create/Generate OpenERP Module.

Just few configurations for Object, Fiels, Field type, views
and it will generate module zip file for you.
You can extract zip file put file in addons path and it is ready to install.

Benifits
--------

* No Python knowledge is required
* Hassle free OpenERP Module creation
* All field types
* Button Event
* Inheriting object

""",
    'images': [],
    "init_xml": [],
    "data": [
        "module_maker_view.xml",
    ],
    'demo_xml': [
    ],
    'test':[
    ],
    'installable': True,
    'active': False,
    'auto_install': False,
    'application':False
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
