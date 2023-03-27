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

    #@api.model
    #def my_method(self):
    #    self.bibliothequeCount = self._cr.execute("select count(*) from public.bc_bib_etageres")




    #etageresCount = fields.Float(
    #    compute="associate_account",

    #)


    #livresCount = fields.Float(
    #    compute="_compute_bibliotheque",
    #)



    #one2many & many2one
    ids_piece = fields.One2many(
        comodel_name="bc_bib.bibliotheque",
        inverse_name="piece_id",
        string="bibliotheque"
    )


    ##function 
    #@api.depends("bibliothequeCount")
    #def _compute_bibliotheque(self):
    #    self.bibliothequeCount = self.env["bc_bib.bibliotheque"].search_count([])

    @api.depends("bibliothequeCount")
    def _compute_bibliotheque(self):
        for piece in self:
            self.bibliothequeCount = len(piece.ids_piece)

    ##@api.depends("etageresCount")
    ##def _compute_etageres(self):
    ##    for record in self:
    ##        record.total = 2.0 * record.amount

    ##@api.depends("livresCount")
    ##def _compute_book(self):
    ##    for record in self:
    ##        record.total = 2.0 * record.amount



    

