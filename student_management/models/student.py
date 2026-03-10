from odoo import models, fields

class Student(models.Model):
    _name = 'school.student'
    _description = 'Student Record'

    name = fields.Char(string='Student Name', required=True)
    age = fields.Integer(string='Age')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], string='Gender', default='male')
    email = fields.Char(string='Email Address')
    phone = fields.Char(string='Phone Number')
    enrollment_date = fields.Date(string='Enrollment Date', default=fields.Date.context_today)
    active = fields.Boolean(string='Active', default=True)

    def action_return_to_list(self):
        return {
            'name': 'Students',
            'type': 'ir.actions.act_window',
            'res_model': 'school.student',
            'view_mode': 'list,form', 
            'target': 'current', 
        }