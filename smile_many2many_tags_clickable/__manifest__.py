# -*- encoding: utf-8 -*-
##############################################################################
#
#    odoo, Open Source Management Solution
#    Copyright (C) 2017 Smile (<http://www.smile.fr>). All Rights Reserved
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    "name": "Many2many Tags Clickable",
    "version": "14.0.1.0.0",
    "category": "Hidden",
    "depends": [
        "web",
    ],
    "author": "Smile",
    "license": 'AGPL-3',
    "description": """

Many2many Tags Clickable
=================

* Allows to open record from many2many_tags widget in a non editable view.

Suggestions & Feedback to: corentin.pouhet-brunerie@smile.fr
    """,
    "website": "",
    "sequence": 0,
    "data": [
        "views/webclient_templates.xml",
    ],
    "demo": [],
    "auto_install": True,
    "installable": True,
    "application": False,
}
