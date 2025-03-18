from odoo import models, fields, api
from datetime import datetime
import requests

class Session(models.Model):
    _name = 'session'
    _description = 'Session'

    name = fields.Char(string="Nom", required=True)
    squad_name = fields.Char(string="Équipe")
    begin_date = fields.Datetime(string="Début")
    end_date = fields.Datetime(string="Fin")
    displayed = fields.Boolean(string="Affiché", default=True)

    @api.model
    def fetch_session(self):
        try:
                data = [ # Mock Data
                    {
                        "id": 1,
                        "squadName": "Alpha Squad",
                        "beginDate": "2025-03-17T08:30:00",
                        "endDate": "2025-03-17T10:30:00",
                        "bookingName": "John Doe"
                    },
                    {
                        "id": 2,
                        "squadName": "Bravo Team",
                        "beginDate": "2025-03-18T14:00:00",
                        "endDate": "2025-03-18T16:00:00",
                        "bookingName": "Alice Smith"
                    },
                    {
                        "id": 3,
                        "squadName": "Charlie Unit",
                        "beginDate": "2025-03-19T09:15:00",
                        "endDate": "2025-03-19T11:45:00",
                        "bookingName": "Bob Johnson"
                    },
                    {
                        "id": 4,
                        "squadName": "Delta Force",
                        "beginDate": "2025-03-20T13:00:00",
                        "endDate": "2025-03-20T15:30:00",
                        "bookingName": "Emma Brown"
                    },
                    {
                        "id": 5,
                        "squadName": "Echo Team",
                        "beginDate": "2025-03-21T10:00:00",
                        "endDate": "2025-03-21T12:30:00",
                        "bookingName": "Michael Wilson"
                    },
                    {
                        "id": 6,
                        "squadName": "Foxtrot Unit",
                        "beginDate": "2025-03-22T08:45:00",
                        "endDate": "2025-03-22T11:15:00",
                        "bookingName": "Sophia Garcia"
                    },
                    {
                        "id": 7,
                        "squadName": "Golf Squad",
                        "beginDate": "2025-03-23T15:30:00",
                        "endDate": "2025-03-23T18:00:00",
                        "bookingName": "Daniel Martinez"
                    },
                    {
                        "id": 8,
                        "squadName": "Hotel Team",
                        "beginDate": "2025-03-24T12:00:00",
                        "endDate": "2025-03-24T14:30:00",
                        "bookingName": "Olivia Davis"
                    },
                    {
                        "id": 9,
                        "squadName": "India Unit",
                        "beginDate": "2025-03-25T07:30:00",
                        "endDate": "2025-03-25T09:45:00",
                        "bookingName": "James White"
                    },
                    {
                        "id": 10,
                        "squadName": "Juliet Force",
                        "beginDate": "2025-03-26T16:00:00",
                        "endDate": "2025-03-26T18:30:00",
                        "bookingName": "Isabella Thomas"
                    }
                ]
                self.env['session'].sudo().search([]).unlink()  # Nettoie les anciens RDV
                for item in data:
                    self.create({
                        'name': item['bookingName'],
                        'squad_name': item['squadName'],
                        'begin_date': datetime.strptime(item['beginDate'], "%Y-%m-%dT%H:%M:%S"),
                        'end_date': datetime.strptime(item['endDate'], "%Y-%m-%dT%H:%M:%S"),
                        'displayed': True
                    })
        except Exception as e:
            raise Exception(f"Erreur de connexion : {str(e)}")