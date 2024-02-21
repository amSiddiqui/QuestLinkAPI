import strawberry
from typing import List, Optional
from app.scalars.scalars import Game as GameType
from strawberry.types import Info
from app.models.models import Game as GameModel
from app.db.session import Session
from app.helpers.helper import get_only_selected_fields, get_valid_data


@strawberry.type
class Query:
    @strawberry.field
    def games(self, info: Info, limit: Optional[int] = 10) -> List[GameType]:
        db = Session()
        field_names = get_only_selected_fields(GameModel, info)
        fields = [getattr(GameModel, field) for field in field_names]
        games = db.query(GameModel).with_entities(*fields).limit(limit).all()

        games_data = []
        for game in games:
            game_data = get_valid_data(game, GameModel)
            for rel_field in ['genres', 'platforms', 'age_ratings', 'companies']:
                if rel_field not in game_data:
                    game_data[rel_field] = []  # Provide an empty list as default
            games_data.append(GameType(**game_data))

        return games
        
        
        
    
