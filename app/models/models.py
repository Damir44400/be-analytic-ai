from sqlalchemy import Column, String, Integer, ForeignKey, Boolean

from app.database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, index=True, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False, unique=True, index=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    is_superuser = Column(Boolean, nullable=False, default=False)
    is_representative = Column(Boolean, default=False)


class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer, index=True, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    type_company = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))


class CompanyMachine(Base):
    __tablename__ = 'company_machines'
    id = Column(Integer, index=True, primary_key=True, autoincrement=True)
    title = Column(String, unique=True, nullable=True)
    train_data = Column(String, nullable=False)
    company_id = Column(Integer, ForeignKey('companies.id'))


class RequestRegister(Base):
    __tablename__ = 'request_registers'

    id = Column(Integer, index=True, primary_key=True, autoincrement=True)
    company_id = Column(Integer, ForeignKey('companies.id'))
    is_confirmed = Column(Boolean, default=False)
