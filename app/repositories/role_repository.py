import json
from app.utils.security_utils import hash_password
from sqlalchemy import text


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
                    connection.execute(
                        text(roles_query).bindparams(name=role['name'], permissions=json.dumps(role['permissions'])))

        except Exception as e:
            raise RuntimeError(f"Error adding roles: {e}")

    def add_super_user(self, username, email, password):
        try:
            hashed_password = hash_password(password)
            with self._engine.connect() as connection:
                transaction = connection.begin()

                try:
                    user_db = connection.execute(
                        text("SELECT * FROM User WHERE User.email = :email OR User.username = :username").bindparams(
                            **{'email': email, 'username': username})
                    )
                    if user_db.fetchone():
                        raise ValueError("User with the given email or username already exists.")

                    add_super_user_query = """
                        INSERT INTO User(username, email, hashed_password, role_id)
                        VALUES (:username, :email, :password, :role_id)
                    """
                    super_user_data = {'username': username, 'email': email, 'password': hashed_password, 'role_id': 1}
                    connection.execute(text(add_super_user_query).bindparams(**super_user_data))
                    transaction.commit()

                except Exception as inner_exception:
                    transaction.rollback()
                    raise RuntimeError(f"Error adding super user: {inner_exception}")

        except Exception as e:
            raise RuntimeError(f"Error adding super user: {e}")

    def get_all_moderators(self):
        try:
            with self._engine.connect() as connection:
                transaction = connection.begin()

                try:
                    users = connection.execute(
                        text("SELECT id, username, email, role_id FROM User WHERE role_id = 3")
                    )
                    return users

                except Exception as inner_exception:
                    transaction.rollback()
                    raise RuntimeError(f"Error retrieving moderators: {inner_exception}")

        except Exception as e:
            raise RuntimeError(f"Error retrieving moderators: {e}")
