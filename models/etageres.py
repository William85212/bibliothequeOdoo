from importlib.metadata import requires 
from odoo import fields, models 


class bibliotheque(models.Model): 
    _name = "bc_bib.etageres"
    _description="etagere"

    etagereName = fields.Char(
        string="title",
        require="True",
        help="coucou bhou",
        index="True"
    )

