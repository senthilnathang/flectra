# -*- coding: utf-8 -*-
# Part of Odoo,Flectra. See LICENSE file for full copyright and licensing details.
{
    'name': 'Website Wishlist',
    'description': 'Let returning shoppers save products in a wishlist',
    'author': 'Odoo SA, Flectra',
    'website': 'https://www.flectrahq.com',
    'category': 'Website',
    'version': '1.0',
    'depends': ['website_sale'],
    'data': [
        'security/website_sale_wishlist_security.xml',
        'security/ir.model.access.csv',
        'views/website_sale_wishlist_template.xml',
    ],
    'installable': True,
}
