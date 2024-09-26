from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def _action_confirm(self):
        res = super()._action_confirm()  

        self.picking_ids.unlink()

        product_groups = {}
        for line in self.order_line:
            key = (line.product_id.id, line.product_uom.id)
            if key not in product_groups:
                product_groups[key] = []
            product_groups[key].append(line)

        for group_key, lines in product_groups.items():
            new_picking = self.env['stock.picking'].create({
                'picking_type_id': self.warehouse_id.out_type_id.id,
                'location_id': self.warehouse_id.lot_stock_id.id,
                'location_dest_id': self.partner_id.property_stock_customer.id,
                'origin':self.name,
                'partner_id': self.partner_id.id,

            })

            for line in lines:
                new_picking.move_lines.create({
                    'name': line.name,
                    'product_id': line.product_id.id,
                    'product_uom_qty': line.product_uom_qty,
                    'product_uom': line.product_uom.id,
                    'picking_id': new_picking.id,
                    'location_id': self.warehouse_id.lot_stock_id.id,
                    'location_dest_id': self.partner_id.property_stock_customer.id,
                })
            
            new_picking.action_confirm()
            new_picking.action_assign()

        return res