from odoo import models, fields, api
import requests

class Appointment(models.Model):
    _name = 'appointment'
    _description = 'Appointment'

    name = fields.Char(string="Nom", required=True)
    squad_name = fields.Char(string="Équipe")
    begin_date = fields.Datetime(string="Début")
    end_date = fields.Datetime(string="Fin")

    @api.model
    def fetch_appointments(self):
        """Récupère les rendez-vous depuis l'API externe et les enregistre dans Odoo."""
        url = "https://example.com/rdv"  # Remplacez par l'URL réelle
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                self.env['appointment'].sudo().search([]).unlink()  # Nettoie les anciens RDV
                for item in data:
                    self.create({
                        'name': item.get('bookingName'),
                        'squad_name': item.get('squadName'),
                        'begin_date': item.get('beginDate'),
                        'end_date': item.get('endDate'),
                    })
            else:
                raise Exception("Erreur lors de la récupération des données")
        except Exception as e:
            raise Exception(f"Erreur de connexion : {str(e)}")