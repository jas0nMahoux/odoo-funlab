from odoo import http
from odoo.http import request

class SessionController(http.Controller):

    @http.route('/fetch_sessions', type='json', auth='user')
    def fetch_sessions(self):
        """Permet de déclencher la mise à jour via l'interface web."""
        try:
            request.env['session'].fetch_appointments()
            return {"status": "success", "message": "Sessions mis à jour"}
        except Exception as e:
            return {"status": "error", "message": str(e)}