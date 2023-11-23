import json
from app.utils.security_utils import hash_password
from sqlalchemy import text
from sqlalchemy.exc import IntegrityError, DataError


class RoleRepository:
    def __init__(self, engine):
        self._engine = engine

    def insert_all_roles(self):
        try:
            roles_query = """
                INSERT INTO Role(name, permissions) 
                VALUES (:name, :permissions)
            """

            roles_data = [
                {'name': 'admin', 'permissions': {'can_update_role': True, 'can_update_post': True, 'can_delete': True,
                                                  'can_post': True}},
                {'name': 'user', 'permissions': {}},
                {'name': 'moderator', 'permissions': {'can_update_post': True, 'can_delete': True, 'can_post': True}}
            ]

            with self._engine.connect() as connection:
                for role in roles_data:
                    existing_role = connection.execute(
                        text("SELECT id FROM Role WHERE name = :name").bindparams(name=role['name'])
                    ).fetchone()

                    if not existing_role:
                        connection.execute(
                            text(roles_query).bindparams(name=role['name'], permissions=json.dumps(role['permissions']))
                        )

        except Exception as e:
            raise RuntimeError(f"Error adding roles: {e}")

    def add_super_user(self, username, email, password):
        try:
            hashed_password = hash_password(password)
            with self._engine.connect() as connection:
                with connection.begin() as transaction:
                    try:
                        user_db = connection.execute(
                            text("SELECT * FROM User WHERE User.email = :email OR User.username = :username"),
                            {'email': email, 'username': username}
                        )
                        if user_db.fetchone():
                            raise ValueError("User with the given email or username already exists.")

                        add_super_user_query = """
                            INSERT INTO User(username, email, hashed_password, role_id)
                            VALUES (:username, :email, :password, :role_id)
                        """
                        super_user_data = {'username': username, 'email': email, 'password': hashed_password,
                                           'role_id': 1}
                        connection.execute(text(add_super_user_query).bindparams(**super_user_data))
                        transaction.commit()

                    except IntegrityError as e:
                        transaction.rollback()
                        raise ValueError("User with the given email or username already exists.")

                    except (DataError, Exception) as inner_exception:
                        transaction.rollback()
                        raise RuntimeError(f"Error adding super user: {inner_exception}")

        except Exception as e:
            raise RuntimeError(f"Error adding super user: {e}")

    def add_moderator(self, user_id: int):
        try:
            with self._engine.connect() as connection:
                with connection.begin() as transaction:
                    try:
                        user_db = connection.execute(
                            text("SELECT * FROM User WHERE id = :user_id"),
                            {'user_id': user_id}
                        )

                        if not user_db.fetchone():
                            raise ValueError("User not found")

                        add_moderator_query = """
                            UPDATE User SET role_id = 3 WHERE id = :user_id
                        """
                        moderator_data = {'user_id': user_id}
                        connection.execute(text(add_moderator_query).bindparams(**moderator_data))
                        transaction.commit()

                    except IntegrityError as e:
                        transaction.rollback()
                        raise ValueError("User with the given email or username already exists.")

                    except (DataError, Exception) as inner_exception:
                        transaction.rollback()
                        raise RuntimeError(f"Error adding moderator: {inner_exception}")

        except Exception as e:
            raise RuntimeError(f"Error adding moderator: {e}")

    def delete_moderator(self, user_id):
        try:
            with self._engine.connect() as connection:
                with connection.begin() as transaction:
                    try:
                        check_result = connection.execute(
                            text("SELECT * FROM User WHERE id = :user_id AND role_id = 3"),
                            {'user_id': user_id}
                        )
                        if check_result.rowcount == 0:
                            raise ValueError("Error deleting moderator: User not found or not a moderator.")
                        update_result = connection.execute(
                            text("UPDATE User SET role_id = 2 WHERE id = :user_id AND role_id = 3"),
                            {'user_id': user_id}
                        )
                        if update_result.rowcount == 0:
                            raise ValueError("Error deleting moderator: User not found or not a moderator.")

                        transaction.commit()

                    except Exception as inner_exception:
                        transaction.rollback()
                        raise RuntimeError(f"Error deleting moderator: {inner_exception}")

        except Exception as e:
            raise RuntimeError(f"Error deleting moderator: {e}")
