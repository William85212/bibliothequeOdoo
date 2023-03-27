from importlib.metadata import requires
import string 
from odoo import api, fields, models 


class bibliotheque(models.Model): 
    _name = "bc_bib.piece"
    _description="piece"

    namePiece = fields.Char(
        name="namePiece",
        require= "True",
        help="le nom de la piece", 
        index = "True"
    )

    bibliothequeCount = fields.Float(
        compute="_compute_bibliotheque"
    )

    etageresCount = fields.Float(
       # compute="_compute_etageres",

    )

    livre = fields.Float(
        #compute="_compute_bibliotheque",
    )

    #one2many & many2one
    ids_piece = fields.One2many(
        comodel_name="bc_bib.bibliotheque",
        inverse_name="piece_id",
        string="bibliotheque"
    )

    #function 
    @api.depends("bibliothequeCount")
    def _compute_bibliotheque(self):
        for piece in self:
            self.bibliothequeCount = len(piece.ids_piece)

    #@api.depends("etageresCount")
    #def _compute_etageres(self):
    #    for piece in self:
    #        for bibli in piece:
    #            self.etageresCount = len(bibli.idsetageres)


    

