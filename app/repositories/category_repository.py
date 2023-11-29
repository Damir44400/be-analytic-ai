from sqlalchemy.orm import Session
from app.models.models import Category


class CategoryRepository:
    def create_category(self, db: Session, name: str):
        genre = Category(name=name)
        db.add(genre)
        db.commit()
        return genre

    def get_category_by_id(self, db: Session, category_id: int):
        return db.query(Category).filter(Category.id == category_id).first()

    def get_category_by_name(self, db: Session, name: str):
        return db.query(Category).filter(Category.name == name).first()

    def get_all_categories(self, db: Session):
        return db.query(Category).all()

    def update_category(self, db: Session, category_id: int, new_name: str):
        category = self.get_category_by_id(db, category_id)
        if category:
            category.name = new_name
            db.commit()
        return category

    def delete_category(self, db: Session, category_id: int):
        category = self.get_category_by_id(db, category_id)
        if category:
            db.delete(category)
            db.commit()
        return category
