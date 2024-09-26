# -*- coding: utf-8 -*-
# from odoo import http


# class ZinfogTask(http.Controller):
#     @http.route('/zinfog_task/zinfog_task', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/zinfog_task/zinfog_task/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('zinfog_task.listing', {
#             'root': '/zinfog_task/zinfog_task',
#             'objects': http.request.env['zinfog_task.zinfog_task'].search([]),
#         })

#     @http.route('/zinfog_task/zinfog_task/objects/<model("zinfog_task.zinfog_task"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('zinfog_task.object', {
#             'object': obj
#         })
