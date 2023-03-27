from importlib.metadata import requires 
from odoo import api, fields, models 


class bibliotheque(models.Model): 
    _name = "bc_bib.bibliotheque"
    _description="bibli"

    bibliothequeName = fields.Char(
        string="title",
        required="True",
        help="Nom de la bilbiotheques",
        index="True"
    )

    etageres = fields.Float(
        compute="_compute_etageres"
    )

    livres = fields.Float(
        compute="_compute_livres"
    )


    #Many2one & One2Many  
    piece_id = fields.Many2one(
        comodel_name="bc_bib.piece", 
        string="namePiece",
        required="True"
    )
    
    idsetageres = fields.One2many(
        comodel_name="bc_bib.etageres",
        inverse_name="bibliothequeId",
        string="etageres"
    )

    @api.depends("idsetageres", "idsetageres.idsBooks")
    def _compute_livres(self):
        for bibliotheque in self:
            print()
            #bibliotheque.livres = sum(bibliotheque.idsetageres.mapped("idsBooks"))



    @api.depends("idsetageres")
    def _compute_etageres(self):
        for bibliotheque in self:
            bibliotheque.etageres = len(bibliotheque.idsetageres)

    @api.depends("idsetageres", "idsetageres.idsBooks")
    def _compute_livres(self):
        for bibliotheque in self:
            bibliotheque.livres = len(bibliotheque.idsetageres.mapped("idsBooks"))


  


