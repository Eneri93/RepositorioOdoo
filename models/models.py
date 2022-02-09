# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class proyectos(models.Model):
#     _name = 'proyectos.proyectos'
#     _description = 'proyectos.proyectos'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
from odoo import models,fields, api

class departamento(models.Model):
    _name= 'proyectos.departamento'
    _description= 'Define los atributos de un departamento'


    #atributos
    nombreDpto= fields.Char(string='Nombre departamento',required=True)


class empleado(models.Model):
    _name='proyectos.'
    _description = 'Define los atributos de un departamento'

        # atributos
    dniEmpleado = fields.Char(string='DNI', required=True)
    nombreEmpleado = fields.Char(string='Nombre', required=True)
    fechaNacimiento=fields.Date(string='Fecha nacimiento', required=True,default= fields.date.today())
    direccionEmpleado = fields.Char(string='Direccion', required=True)
    telefonoEmpleado = fields.Char(string='Telefono')

class proyeto(models.Model):
    _name = 'proyectos.proyecto'
    _description= 'Atributos de un proyecto'

    # atributos
    nombreProyecto = fields.Char(string='Nombre proyecto', required=True)
    tipoProyecto= fields.Selection(string='Tipo proyecto', selection=[('f','Front-end'),('b','Back-end')],help='Tipo de proyecto al que esta destinado')
    fechaInicio = fields.Date(string='Fecha de inicio', required=True)
    fechaFin = fields.Date(string='Fecha de fin', required=True)
    descripcionProyecto= fields.Text(string='descripcion del proyecto')

    