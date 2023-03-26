from importlib.metadata import requires
from sqlite3 import apilevel
from odoo import api,fields, models 


class bibliotheque(models.Model): 
    _name = "bc_bib.etageres"
    _description="etagere"
    

    etagereName = fields.Char(
        string="title",
        require="True",
        help="coucou bhou",
        index="True"
    )

    nombresLivres = fields.Float(compute="_compute_total")


    pieceId = fields.Many2one(
        comodel_name="bc_bib.piece", 
        string="Piece"
    )

    bibliothequeId = fields.Many2one(
        comodel_name="bc_bib.bibliotheque",
        string="bibliotheque"
    )

    idsBooks = fields.One2many(
        comodel_name="bc_bib.book",
        inverse_name="title",
        string = "books"
    )

    @api.depends("nombresLivres")
    def _compute_total(self):
        for record in self:
            record.total = 2.0 * record.amount
            






