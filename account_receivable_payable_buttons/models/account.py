# -*- coding: utf-8 -*-

##############################################################################
#
# Account Receivable and Payable Buttons
# Copyright (C) 2016 OpusVL (<http://opusvl.com/>)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import models, fields, api
import openerp.addons.decimal_precision as dp

class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    account_type = fields.Selection(
        related=['account_id', 'type'],
        readonly=True,
        string='Account Internal Type',
    )

    line_amount_agg = fields.Float(
        compute='_compute_aggregate_amounts',
        readonly=True,
        store=True,
        digits=dp.get_precision('Account'),
    )

    line_amount_effective_currency_agg = fields.Float(
        compute='_compute_aggregate_amounts',
        readonly=True,
        store=True,
        digits=dp.get_precision('Account'),
    )

    effective_currency_id = fields.Many2one(
        comodel_name='res.currency',
        compute="_compute_effective_currency",
        store=True,
        readonly=True,
        string='Effective Currency',
    )

    @api.depends('amount_currency', 'currency_id', 'credit', 'debit')
    @api.one
    def _compute_aggregate_amounts(self):
        line_value = (self.credit - self.debit)
        self.line_amount_agg = line_value
        self.line_amount_effective_currency_agg = -self.amount_currency if self.currency_id else line_value

    @api.depends('currency_id', 'company_id.currency_id')
    @api.one
    def _compute_effective_currency(self):
        self.effective_currency_id = self.currency_id or self.company_id.currency_id

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
