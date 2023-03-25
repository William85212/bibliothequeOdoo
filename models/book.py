from importlib.metadata import requires
from odoo import fields, models


class book(models.Model):
    _name = "bc_bib.book" #nom du module.nom de la table
    _description = "un descriptif"
    #champ de la tables-->
    title = fields.Char( 
        string="title",
        require="True",
        help="Le titre du livre",
        index="True"
    )

    descriptionLivres = fields.Char(
        string="description",
        require="True",
        help="Description du livre",
        index="True"
    )

    pieceId = fields.Many2one(
        comodel_name="bc_bib.piece", 
        string="Piece"
    )

    bibliothequeId = fields.Many2one(
        comodel_name="bc_bib.bibliotheque", 
        string="bibliotheque"
    )

    etageresId = fields.Many2one(
        comodel_name="bc_bib.etageres", 
        string="Etageres"
    )

    

   



