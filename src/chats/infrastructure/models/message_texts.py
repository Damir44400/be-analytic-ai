from datetime import datetime

import sqlalchemy as sa
import sqlalchemy.orm as orm

from src.gateway.infrastructure.database import Base


class MessageTexts(Base):
    __tablename__ = 'messages_texts'

    id: orm.Mapped[int] = orm.mapped_column(sa.Integer, primary_key=True)
    sender: orm.Mapped[int] = orm.mapped_column(sa.ForeignKey("users.id"))
    receiver: orm.Mapped[int] = orm.mapped_column(sa.ForeignKey("users.id"))
    message: str = sa.Column(sa.Text, nullable=False)
    is_updated: orm.Mapped[bool] = orm.mapped_column(sa.Boolean)
    sent_at: datetime = sa.Column(sa.DateTime, nullable=False)

    user = orm.relationship("User", foreign_keys=[sender, receiver])
