from odoo import http
from odoo.http import request

class AppointmentController(http.Controller):

    @http.route('/fetch_appointments', type='json', auth='user')
    def fetch_appointments(self):
        """Permet de déclencher la mise à jour via l'interface web."""
        try:
            request.env['appointment'].fetch_appointments()
            return {"status": "success", "message": "Rendez-vous mis à jour"}
        except Exception as e:
            return {"status": "error", "message": str(e)}