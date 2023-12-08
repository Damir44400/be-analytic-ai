from sqlalchemy.orm import Session
from app.models.models import Comment


class CommentRepository:
    @staticmethod
    def create_comment(db: Session, content: str, user_id: int, anime_id: int):
        comment = Comment(content=content, user_id=user_id, anime_id=anime_id)
        db.add(comment)
        db.commit()
        return comment

    @staticmethod
    def check_owner_comment(db: Session, comment_id: int, user_id: int):
        return db.query(Comment).filter(Comment.id == comment_id, Comment.user_id == user_id).first()

    @staticmethod
    def get_comment_by_id(db: Session, comment_id: int):
        return db.query(Comment).filter(Comment.id == comment_id).first()

    @staticmethod
    def get_comments_by_user_id(db: Session, user_id: int):
        return db.query(Comment).filter(Comment.user_id == user_id).all()

    def update_comment_content(self, db: Session, comment_id: int, user_id: int, new_content: str):
        comment = self.check_owner_comment(db, comment_id, user_id)
        if comment:
            comment.content = new_content
            db.commit()
            db.refresh(comment)
        return comment

    def delete_comment(self, db: Session, comment_id: int, user_id: int, is_admin=False):
        if is_admin:
            comment = db.query(Comment).filter(Comment.id == comment_id).first()
            if comment:
                db.delete(comment)
                db.commit()
            return comment
        else:
            comment = self.check_owner_comment(db, comment_id, user_id)
            if comment:
                db.delete(comment)
                db.commit()
            return comment

    @staticmethod
    def get_comment_of_anime(db: Session, anime_id: int):
        return db.query(Comment).filter(Comment.anime_id == anime_id).all()
