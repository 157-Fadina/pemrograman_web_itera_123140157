from pyramid.view import view_config
from .. import models

@view_config(route_name='home', renderer='json') # Ubah renderer ke json untuk tes
def my_view(request):
    try:
        # Coba ambil data mahasiswa
        query = request.dbsession.query(models.Mahasiswa).all()
        return {'status': 'success', 'data': [m.to_dict() for m in query]}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}