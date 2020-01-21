# -*- coding: utf-8 -*-
# (C) 2019 Smile (<http://www.smile.fr>)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo import  models, api, tools, _
from odoo.exceptions import ValidationError


class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.constrains('email')
    def _check_email_valid(self):
        for partner in self:
            if partner.email and \
                    not tools.single_email_re.match(partner.email):
                raise ValidationError(_('Email is invalid.'))
