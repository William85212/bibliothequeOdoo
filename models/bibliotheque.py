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

    etageres = fields.Float(
            
    )

    livres = fields.Float(
        
    )


    #Many2one & One2Many  
    piece_id = fields.Many2one(
        comodel_name="bc_bib.piece", 
        string="namePiece"
    )
    
    idsetageres = fields.One2many(
        comodel_name="bc_bib.etageres",
        inverse_name="bibliothequeId",
        string="etageres"
    )



