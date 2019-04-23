from flask import jsonify
from flask import request
from flask import url_for
from app import db
from app.api import bp
from app.api.errors import bad_request
from app.models import Brew

@bp.route('/brews', methods=['GET'])
def get_brews():
  page = request.args.get('page', 1, type=int)
  per_page = min(request.args.get('per_page', 10, type=int), 100)
  data = Brew.to_collection_dict(Brew.query, page, per_page, 'api.get_brews')
  return jsonify(data)


@bp.route('/brews', methods=['POST'])
def create_brew():
  data = request.get_json() or {}
  if 'name' not in data or 'description' not in data or 'batch_size' not in data:
    return bad_request('must include name, description and batch_size')
  brew = Brew()
  brew.from_dict(data)
  db.session.add(brew)
  db.session.commit()
  response = jsonify(brew.to_dict())
  response.stats_code = 201
  response.headers['Location'] = url_for('api.get_brew', id=brew.id)
  return response


@bp.route('/brews/<int:id>', methods=['GET'])
def get_brew(id):
    return jsonify(Brew.query.get_or_404(id).to_dict())


@bp.route('/brews/<int:id>', methods=['PUT'])
def update_brew(id):
  brew = Brew.query.get_or_404(id)
  data = request.get_json() or {}
  brew.from_dict(data)
  db.session.commit()
  return jsonify(brew.to_dict())
