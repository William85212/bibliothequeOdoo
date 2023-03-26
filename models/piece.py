from importlib.metadata import requires
import string 
from odoo import fields, models 


class bibliotheque(models.Model): 
    _name = "bc_bib.piece"
    _description="piece"

    namePiece = fields.Char(
        name="namePiece",
        require= "True",
        help="le nom de la piece", 
        index = "True"
    )

    ids_piece = fields.One2many(
        comodel_name="bc_bib.bibliotheque",
        inverse_name="piece_id",
        string="bibliotheque"
    )



    

