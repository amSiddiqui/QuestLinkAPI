import strawberry
from typing import List, Optional
from datetime import datetime

@strawberry.type
class Genre:
    id: strawberry.ID
    name: str
    url: Optional[str]


@strawberry.type
class Platform:
    id: strawberry.ID
    alternative_name: Optional[str]
    generation: Optional[int]
    abbreviation: Optional[str]
    summary: Optional[str]


@strawberry.type
class AgeRating:
    id: strawberry.ID
    rating: int
    rating_system: str
    rating_description: Optional[str]


@strawberry.type
class Company:
    id: strawberry.ID
    country: int
    description: Optional[str]
    name: str
    url: Optional[str]
    parent: Optional[strawberry.ID]


@strawberry.type
class Game:
    id: strawberry.ID
    first_release_date: Optional[datetime]
    name: str
    summary: Optional[str]
    url: Optional[str]
    parent_game: Optional[strawberry.ID]
    rating: Optional[float]
    rating_count: Optional[int]
    storyline: Optional[str]
    total_rating: Optional[float]
    total_rating_count: Optional[int]
    genres: List[Genre] = strawberry.field(resolver=lambda self: self.resolve_genres())
    platforms: List[Platform] = strawberry.field(resolver=lambda self: self.resolve_platforms())
    age_ratings: List[AgeRating] = strawberry.field(resolver=lambda self: self.resolve_age_ratings())
    companies: List[Company] = strawberry.field(resolver=lambda self: self.resolve_companies())

    def resolve_genres(self, info) -> List[Genre]:
        # Implement the logic to fetch genres for the game
        pass

    def resolve_platforms(self, info) -> List[Platform]:
        # Implement the logic to fetch platforms for the game
        pass

    def resolve_age_ratings(self, info) -> List[AgeRating]:
        # Implement the logic to fetch age ratings for the game
        pass

    def resolve_companies(self, info) -> List[Company]:
        # Implement the logic to fetch companies for the game
        pass

@strawberry.type
class Category:
    id: strawberry.ID
    category_description: str
