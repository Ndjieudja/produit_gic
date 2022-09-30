# --*-- coding:utf8 --*--

from odoo import models, api, fields
from datetime import date


class AbsGic(models.AbstractModel):
    _name = 'gic.abstract'

    active = fields.Boolean(default=False, string='Active')

    def do_archive(self):
        for record in self:
            record.active = not record.active


# class principale du module
class Gic(models.Model):

    _name = 'gic.gic'
    _inherit = ['product.template', 'mail.thread', 'mail.activity.mixin', 'gic.abstract']

    _description = 'Base de gestion de produit gic'

    # Creation d un nouvel article dans le module stock suit de create de l article dans le model courant
    @api.model
    def create(self, vals):
        vals['product_id'] = self.env['product.template'].create(vals).id
        res = super(Gic, self).create(vals)
        print(vals)
        return res

    # Fonction de mise a jour des donner de la base courant suivit de leur equivalent dans le base stock assosier
    @api.multi
    def write(self, vals):
        model = self.env['product.template'].search([('id','=', self.product_id.id),])
        model.write(vals)

        res = super(Gic, self).write(vals)
        return res

    # Fonction de gestion de nom a afficher
    def name_get(self):
        result = []
        for record in self:
            rec_name = "{0}".format(record.name,)
            result.append((record.id, rec_name))
        return result

    # fonction d appel lors l impression des article et leurs etats dans le model courant
    def print_etat(self):
        model = self.env['gic.gic'].search([])
        list_val = list()
        for record in model:
            list_val.append((record.name, record.info_produit))
        return list_val


    # ============================ Declaration des champs ==============================

    etat_produit = fields.Selection(selection=[('frais', 'Frais'), ('recent', 'Recent'),
            ('fletri', 'Flétri')], string='Etat', default='frais')

    # declaration des defferents champs
    info_produit = fields.Char(string='Information Produit', help='entre les information concernant le produit')
    name = fields.Char(string='Name')

    product_id = fields.Many2one('product.template', ondelete='cascade')


