from importlib.metadata import requires
from odoo import fields, models


class book(models.Model):
    _name = "bc_bib.book" #nom du module.nom de la table
    _description = "un descriptif"
    #champ de la tables-->
    title = fields.Char( 
        string="title",
        required="True",
        help="Le titre du livre",
        index="True"
    )

    descriptionLivres = fields.Char(
        string="description",
        required="True",
        help="Description du livre",
        index="True"
    )

 

    etageresId = fields.Many2one(
        comodel_name="bc_bib.etageres", 
        string="Etageres",
        required="True"

    )

    

   



