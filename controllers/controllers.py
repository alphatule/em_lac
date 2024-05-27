# -*- coding: utf-8 -*-
# from odoo import http


# class EmLact(http.Controller):
#     @http.route('/em_lact/em_lact', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/em_lact/em_lact/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('em_lact.listing', {
#             'root': '/em_lact/em_lact',
#             'objects': http.request.env['em_lact.em_lact'].search([]),
#         })

#     @http.route('/em_lact/em_lact/objects/<model("em_lact.em_lact"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('em_lact.object', {
#             'object': obj
#         })
