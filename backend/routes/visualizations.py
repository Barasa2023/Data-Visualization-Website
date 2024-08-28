from flask import Blueprint, jsonify, request
from models import Visualization

bp = Blueprint('visualizations', __name__)

@bp.route('/api/visualizations/<int:id>', methods=['GET'])
def get_visualization(id):
    # Logic to retrieve visualization data
    viz = Visualization.query.get_or_404(id)
    return jsonify(viz.to_dict()), 200

@bp.route('/api/visualizations/<int:id>', methods=['PUT'])
def update_visualization(id):
    # Logic to update visualization settings
    viz = Visualization.query.get_or_404(id)
    data = request.json
    # Update visualization properties here
    db.session.commit()
    return jsonify({"message": "Visualization updated successfully"}), 200
