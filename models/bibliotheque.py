from importlib.metadata import requires 
from odoo import fields, models 


class bibliotheque(models.Model): 
    _name = "bc_bib.bibliotheque"
    _description="bibli"

    bibliothequeName = fields.Char(
        string="title",
        require="True",
        help="Nom de la bilbiotheques",
        index="True"
    )


    piece_id = fields.Many2one(
        comodel_name="bc_bib.piece", 
        string="fk_piece"
    )
