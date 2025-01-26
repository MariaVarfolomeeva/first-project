import pytest
from main import BooksCollector

@pytest.fixture
def books_collector():
    return BooksCollector()

def test_add_new_book(books_collector):
    books_collector.add_new_book("1984")
    assert "1984" in books_collector.books_genre
    books_collector.add_new_book("1984")
    assert len(books_collector.books_genre) == 1  
    books_collector.add_new_book("A" * 41)  
    assert "A" * 41 not in books_collector.books_genre

@pytest.mark.parametrize("book_name, genre, expected_genre", [
    ("1984", "Фантастика", "Фантастика"),
    ("Мстители", "Комедии", "Комедии"),
])
def test_set_book_genre(books_collector, book_name, genre, expected_genre):
    books_collector.add_new_book(book_name)
    books_collector.set_book_genre(book_name, genre)
    assert books_collector.get_book_genre(book_name) == expected_genre

def test_set_book_genre_invalid(books_collector):
    books_collector.add_new_book("1984")
    books_collector.set_book_genre("1984", "Неизвестный жанр")
    assert books_collector.get_book_genre("1984") == ""

def test_get_book_genre(books_collector):
    books_collector.add_new_book("1984")
    books_collector.set_book_genre("1984", "Фантастика")
    assert books_collector.get_book_genre("1984") == "Фантастика"

@pytest.mark.parametrize("genre, expected_books", [
    ("Фантастика", ["1984"]),
    ("Комедии", ["Мстители"]),
])
def test_get_books_with_specific_genre(books_collector, genre, expected_books):
    books_collector.add_new_book("1984")
    books_collector.set_book_genre("1984", "Фантастика")
    books_collector.add_new_book("Мстители")
    books_collector.set_book_genre("Мстители", "Комедии")
    books = books_collector.get_books_with_specific_genre(genre)
    assert books == expected_books

def test_get_books_for_children(books_collector):
    books_collector.add_new_book("1984")
    books_collector.set_book_genre("1984", "Фантастика")
    books_collector.add_new_book("Зловещие мертвецы")
    books_collector.set_book_genre("Зловещие мертвецы", "Ужасы")
    books = books_collector.get_books_for_children()
    assert "1984" in books
    assert "Зловещие мертвецы" not in books

def test_add_book_in_favorites(books_collector):
    books_collector.add_new_book("1984")
    books_collector.set_book_genre("1984", "Фантастика")
    books_collector.add_book_in_favorites("1984")
    assert "1984" in books_collector.favorites
    books_collector.add_book_in_favorites("1984")  
    assert len(books_collector.favorites) == 1

def test_delete_book_from_favorites(books_collector):
    books_collector.add_new_book("1984")
    books_collector.set_book_genre("1984", "Фантастика")
    books_collector.add_book_in_favorites("1984")
    books_collector.delete_book_from_favorites("1984")
    assert "1984" not in books_collector.favorites

def test_get_list_of_favorites_books(books_collector):
    books_collector.add_new_book("1984")
    books_collector.set_book_genre("1984", "Фантастика")
    books_collector.add_book_in_favorites("1984")
    favorites = books_collector.get_list_of_favorites_books()
    assert favorites == ["1984"]


def test_get_books_genre(books_collector):
    books_collector.add_new_book("1984")
    books_collector.set_book_genre("1984", "Фантастика")
    books_collector.add_new_book("Мстители")
    books_collector.set_book_genre("Мстители", "Комедии")

    
    books_genre = books_collector.get_books_genre()

    
    assert books_genre == {
        "1984": "Фантастика",
        "Мстители": "Комедии"
    }


def test_delete_book_from_favorites_not_in_favorites(books_collector):
    books_collector.add_new_book("1984")
    books_collector.set_book_genre("1984", "Фантастика")
    
    
    books_collector.delete_book_from_favorites("1984")  
    
    
    assert "1984" not in books_collector.favorites
