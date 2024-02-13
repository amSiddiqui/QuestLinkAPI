from app.db.session import Session
from app.models import Genre

def test_insert():
    db = Session()
    new_genre = Genre(name="Test Genre")
    db.add(new_genre)
    db.commit()
    db.refresh(new_genre)
    print(new_genre.id)
    db.close()

if __name__ == "__main__":
    test_insert()
