import argparse
import json
from app import create_app, db
from app.models.book import Book

app = create_app()
app.app_context().push()

parser = argparse.ArgumentParser(description="Импорт книг из JSON файла")
parser.add_argument("file", help="Путь к JSON файлу")
args = parser.parse_args()

with open(args.file, encoding="utf-8") as f:
    books = json.load(f)
    for data in books:
        book = Book(title=data["title"], author=data["author"],
                    genre=data.get("genre", ""), condition=data.get("condition", ""))
        db.session.add(book)
    db.session.commit()
print("Книги успешно импортированы.")
