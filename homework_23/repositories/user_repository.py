from homework_23.session import session
from homework_23.models.users import Users


class UsersRepository:
    def __init__(self):
        self.__session = session

    def select_all_users(self):
        for user in self.__session.query(Users).all():
            print(user)

    def delete_user_by_mail(self, delete_mail: str):
        self.__session.query(Users).filter(Users.email == delete_mail).delete()
        self.__session.commit()

    def modify_user_by_id(self, user_id: str, name: str, email: str, age: int):
        self.__session.query(Users).filter(Users.id == user_id).update({'name': name, 'email': email, 'age': age})
        self.__session.commit()

    def add_new_user(self, id: str, name: str, email: str, age: int):
        self.database_data = Users(id=id, name=name, age=age, email=email)
        self.__session.add(self.database_data)
        self.__session.commit()


if __name__ == '__main__':
    users_repository = UsersRepository()
    users_repository.add_new_user("user_1", "Harry", "doboi@gmail.com", 32)
    # users_repository.modify_user_by_id("user_1", "Harry", "harry_doboi@gmail.com", 33)
    # users_repository.select_all_users()
    # users_repository.delete_user_by_mail("harry_doboi@gmail.com")
