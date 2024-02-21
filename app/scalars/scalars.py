import strawberry
from typing import List, Optional
from datetime import datetime
from strawberry.schema_directive import Location

@strawberry.schema_directive(locations=[Location.OBJECT])
class Keys:
    fields: str


@strawberry.type(directives=[Keys(fields="id")])
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
    genres: List[Genre]
    platforms: List[Platform]
    age_ratings: List[AgeRating]
    companies: List[Company]


@strawberry.type
class Category:
    id: strawberry.ID
    category_description: str
