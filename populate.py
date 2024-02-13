from app.db.session import Session
from app.models import Genre, Game, Platform, AgeRating, Company, Category
import pandas as pd
from pathlib import Path
from datetime import datetime
import tqdm

current_file = Path(__file__).resolve()
csv_dir = current_file.parent.parent / "igdb_api_video_game_ratings_data"

games_csv = csv_dir / 'data_200K.csv'
companies_csv = csv_dir / 'companies.csv'
category_mapping_csv = csv_dir / 'category_mapping.csv'
genres_csv = csv_dir / 'genres.csv'
platforms_csv = csv_dir / 'platforms.csv'
age_ratings_csv = csv_dir / 'age_ratings.csv'

def populate_categories(session):
    df = pd.read_csv(category_mapping_csv)
    for index, row in df.iterrows():
        category = Category(
            id=row['category'],
            category_description=row['category_description']
        )
        session.add(category)
    
def populate_companies(session):
    df = pd.read_csv(companies_csv)
    for index, row in df.iterrows():
        company = Company(
            id=row['id'],
            country=row['country'],
            description=row['description'],
            name=row['name'],
            url=row['url'],
            parent=row['parent']
        )
        session.add(company)
    
def populate_genres(session):
    df = pd.read_csv(genres_csv)
    for index, row in df.iterrows():
        genre = Genre(
            id=row['id'],
            name=row['name'],
            url=row['url']
        )
        session.add(genre)
    
def populate_platforms(session):
    df = pd.read_csv(platforms_csv)
    for index, row in df.iterrows():
        
        platform = Platform(
            id=row['id'],
            alternative_name=row['alternative_name'],
            category_id=int(row['category']) if not pd.isna(row['category']) else None,
            generation=int(row['generation']) if not pd.isna(row['generation']) else None,
            abbreviation=row['abbreviation'],
            summary=row['summary']
        )
        session.add(platform)
    
def populate_age_ratings(session):
    df = pd.read_csv(age_ratings_csv)
    for index, row in df.iterrows():
        age_rating = AgeRating(
            id=row['id'],
            category_id=int(row['category']) if not pd.isna(row['category']) else None,
            rating=row['rating'],
            rating_system=row['rating_system'],
            rating_description=row['rating_description']
        )
        session.add(age_rating)
    
def populate_tables():
    session = Session()
    try:
        print('Populating categories')
        populate_categories(session)
        print('Populating companies')
        populate_companies(session)
        print('Populating genres')
        populate_genres(session)
        print('Populating Platforms')
        populate_platforms(session)
        print('Populating age rating')
        populate_age_ratings(session)
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()


def populate_games():
    session = Session()
    cols = ['id', 'category', 'first_release_date', 'name', 'summary', 'url', 'parent_game', 'age_ratings', 'involved_companies', 'parent_game', 'rating', 'rating_count', 'storyline', 'total_rating', 'total_rating_count', 'genres', 'platforms']
    df = pd.read_csv(games_csv, usecols=cols)
    for index, row in tqdm.tqdm(df.iterrows()):
        first_release_date = datetime.fromtimestamp(row['first_release_date']) if not pd.isna(row['first_release_date']) else None
        game = Game(
            id=row['id'],
            category_id=int(row['category']) if not pd.isna(row['category']) else None,
            first_release_date=first_release_date,
            name=row['name'],
            summary=row['summary'],
            url=row['url'],
            parent_game=int(row['parent_game']) if not pd.isna(row['parent_game']) else None,
            rating=row['rating'],
            rating_count=row['rating_count'],
            storyline=row['storyline'],
            total_rating=row['total_rating'],
            total_rating_count=row['total_rating_count']
        )
        genres = row['genres']
        if not pd.isna(genres):
            game.genres = session.query(Genre).filter(Genre.id.in_(list(genres))).all()
        
        platforms = row['platforms']
        if not pd.isna(platforms):
            game.platforms = session.query(Platform).filter(Platform.id.in_(list(platforms))).all()
        
        age_ratings = row['age_ratings']
        if not pd.isna(age_ratings):
            game.age_ratings = session.query(AgeRating).filter(AgeRating.id.in_(list(age_ratings))).all()

        companies = row['involved_companies']
        if not pd.isna(companies):
            game.companies = session.query(Company).filter(Company.id.in_(list(companies))).all()
        
        session.add(game)
    
    session.commit()
        
        
if __name__ == '__main__':
    populate_games()
