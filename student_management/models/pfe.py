from odoo import models, fields

class StudentPFE(models.Model):
    _name = 'school.pfe'
    _description = 'PFE / Internship Management'
    name = fields.Char(string='Project Title', required=True)
    student_id = fields.Many2one('school.student', string='Stagiaire', required=True)
    
    company_name = fields.Char(string='Host Company ')
    supervisor = fields.Char(string='Company Supervisor ')
    academic_tutor = fields.Char(string='Academic Tutor')
    
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')
    state = fields.Selection([
        ('draft', 'Draft '),
        ('progress', 'In Progress '),
        ('submitted', 'Report Submitted '),
        ('defended', 'Defended '),
    ], string='Status', default='draft')


    def action_start_progress(self):
        for record in self:
            record.state = 'progress'

    def action_submit_report(self):
        for record in self:
            record.state = 'submitted'

    def action_defend(self):
        for record in self:
            record.state = 'defended'

    def action_reset_draft(self):
        for record in self:
            record.state = 'draft'

    