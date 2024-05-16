# -*- coding: utf-8 -*-

from odoo import models, fields, api


class em_lact(models.Model):
    _name = 'em_lact.em_lact'
    _description = 'em_lact.em_lact'

    name = fields.Char()
    fecha_creacion = fields.Date()
    imagen_em = fields.Binary(string="Imagen")
    cif = fields.Char()
    # valoracion =
    direccion = fields.Text()
    dueno = fields.Char()
    num_empleados = fields.Integer()
    tipo_empresa = fields.Char(compute="_tipo_empresa", store=True)
    activo = fields.Boolean(compute="_tipo_empresa", store=True)

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
                

    # name = fields.Char()
    # value = fields.Integer()
    # value2 = fields.Float(compute="_value_pc", store=True)
    # description = fields.Text()

    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100
