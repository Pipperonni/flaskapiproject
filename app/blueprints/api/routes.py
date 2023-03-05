from . import bp as api_bp
from app.blueprints.collect.models import CollectedPokemon

@api_bp.route('/collect')
def api_cards():
    result = []
    collection = CollectedPokemon.query.all()
    for card in collection:
        result.append({
            'id': card.id,
            'pokemon': card.pokemon,
            'timestamp': card.timestamp,
            'user_id': card.user_id
        })
    return result

@api_bp.route('/collect/<id>', methods=['GET'])
def api_card(id):
    card = CollectedPokemon.query.get(int(id))
    return {
            'id': card.id,
            'pokemon': card.pokemon,
            'timestamp': card.timestamp,
            'user_id': card.user_id
        }