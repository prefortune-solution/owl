#-*- coding: utf-8 -*-

from odoo import models, fields, api


class todolist(models.Model):
    _name = 'todo.list'
    _description = 'Todo list'

    name = fields.Char(string="Task name")
    description = fields.Char(string="description")
    completed = fields.Boolean(string="Completed")