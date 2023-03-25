from importlib.metadata import requires 
from odoo import fields, models 


class bibliotheque(models.Model): 
    _name = "bc_bib.etageres"
    _description="etagere"

    id_bibliotheque = fields.One2many(
        comodel_name="bc_bib.book",
        inverse_name="etageresId",
        string="pk_bibliotheque"
    )

    etagereName = fields.Char(
        string="title",
        require="True",
        help="coucou bhou",
        index="True"
    )



