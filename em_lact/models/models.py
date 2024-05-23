# -*- coding: utf-8 -*-

from odoo import models, fields, api


class em_lact_em(models.Model):
    _name = 'em_lact.em'
    _description = 'em_lact.em'

    name = fields.Char('Nombre Empresa')
    fecha_creacion = fields.Date('Fecha creación')
    imagen_em = fields.Binary(string="Imagen")
    cif = fields.Char()
    # valoracion =
    direccion = fields.Text()
    dueno = fields.Char()
    num_empleados = fields.Integer()
    tipo_empresa = fields.Char(compute="_tipo_empresa", store=True)
    activo = fields.Boolean(compute="_tipo_empresa", store=True)

    notes = fields.Text('Notas')
    productos = fields.One2many(comodel_name="em_lact.prod", string="Productos", inverse_name="empresa")

    @api.depends('num_empleados','dueno')
    def _tipo_empresa(self):
        for record in self:
            if record.dueno == False:
                record.activo = False
            else:
                record.activo = True

            if record.num_empleados < 10:
                record.tipo_empresa = "Micropyme"
            elif record.num_empleados < 50:
                record.tipo_empresa = "Pequeña"
            elif record.num_empleados < 250:
                record.tipo_empresa = "Mediana"
            elif record.num_empleados < 1000:
                record.tipo_empresa = "Grande"
            elif record.num_empleados < 10000:
                record.tipo_empresa = "Multinacional"
                
class em_lact_prod(models.Model):
    _name = 'em_lact.prod'
    _description = 'em_lact.prod'

    codigo = fields.Char()
    name = fields.Char('Nombre Producto')
    imagen_prod = fields.Binary(string="Imagen")
    fecha_creacion = fields.Date('Fecha creación')
    dueno = fields.Char('Dueño')
    empresa = fields.Many2one(comodel_name="em_lact.em", string="Empresa asociada")
