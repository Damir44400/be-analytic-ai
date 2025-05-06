from datetime import datetime

import sqlalchemy as sa
import sqlalchemy.orm as orm

from src.core.infrastructure.database import Base


class MessageFiles(Base):
    __tablename__ = 'messages_files'

    id: orm.Mapped[int] = orm.mapped_column(sa.Integer, primary_key=True)
    sender: orm.Mapped[int] = orm.mapped_column(sa.ForeignKey("users.id"))
    receiver: orm.Mapped[int] = orm.mapped_column(sa.ForeignKey("users.id"))
    file: str = sa.Column(sa.Text, nullable=False)
    sent_at: datetime = sa.Column(sa.DateTime, nullable=False)

    user = orm.relationship("User", foreign_keys=[sender, receiver])
