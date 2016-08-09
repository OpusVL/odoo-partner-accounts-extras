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


{
    'name': 'Account Receivable and Payable Buttons',
    'version': '0.1',
    'author': 'OpusVL',
    'website': 'http://opusvl.com/',
    'summary': 'Add smart buttons to Partner form showing receivables and payables with link to journal items list',
    
    'category': 'Accounting & Finance',
    
    'description': """Add a smart button to Partner form showing receivables and payables with link to journal items list.

    Known Issue:
    
    In the journal entries list shown when you click one of the Receivables or Payables buttons,
    there is a total in the &quot;Residual Amount in Currency&quot;
    column.  Because this is adding values in different currencies, the grand total at the bottom will not be useful.
    However if you group by Effective Currency, the totals at the beginning of each currency group
    and any further groupings within should be useful.
""",
    'images': [
    ],
    'depends': [
        'base',
        'account',
        'decimal_precision',
    ],
    'data': [
        'views/journal.xml',
        'views/res_partner.xml',
    ],
    'demo': [
    ],
    'test': [
    ],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,

}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
