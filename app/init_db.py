from app.db.db import engine, Base, SessionLocal
from app.db import crud

Base.metadata.create_all(bind=engine)

db = SessionLocal()

try:
    cat1 = crud.create_category(db, title="Фантастика")
    cat2 = crud.create_category(db, title="Классика")
    print(f"Созданы категории: {cat1.title}, {cat2.title}")

    crud.create_book(db, title="Дюна", description="Эпическая сага о пустынной планете", price=800.0, url="", category_id=cat1.id)
    crud.create_book(db, title="Основание", description="Классика научной фантастики", price=650.0, url="", category_id=cat1.id)

    crud.create_book(db, title="Война и мир", description="Роман-эпопея Льва Толстого", price=1200.0, url="", category_id=cat2.id)
    crud.create_book(db, title="Преступление и наказание", description="Психологический роман Достоевского", price=550.0, url="", category_id=cat2.id)
    
    print("Книги добавлены")
finally:
    db.close()
