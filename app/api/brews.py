from flask import jsonify
from app.api import bp
from app.models import Brew

@bp.route('/brews', methods=['GET'])
def get_brews():
    pass


@bp.route('/brews', methods=['POST'])
def create_brew():
    pass


@bp.route('/brews/<int:id>', methods=['GET'])
def get_brew(id):
    return jsonify(Brew.query.get_or_404(id).to_dict())


@bp.route('/brews/<int:id>', methods=['PUT'])
def update_brew(id):
    pass
