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

    

