# Создайте класс с описанием работника. Любого работника. Employee.
# Буду оценивать полноту описанного класса и буду снимать за все лишнее балы. Хочу видеть чистый код.
# Ожидажю увидеть чистый код с аннотациями. Пока что без связей первого класса со вторым.
# Во всех методах ожидаю увидеть докстринги с вменяемым описанием.

class Employee:
    def __init__(
            self, name: str, last_name: str, age: int, gender: bool, position: str, salary: int, years_of_work: float
    ):
        self.__name = name
        self.__last_name = last_name
        self.__age = age
        self.__gender = gender
        self.__position = position
        self.__salary = salary
        self.__years_of_work = years_of_work

    def get_full_name(self):
        """
            This method returns full name of employee
        """
        return self.__name, self.__last_name

    def get_age(self):
        """
            This method returns age of employee
        """
        return self.__age

    def get_gender(self):
        """
            This method returns gender of employee
        """
        return self.__gender

    def get_position(self):
        """
            This method returns position of employee
        """
        return self.__position

    def get_salary(self):
        """
            This method returns salary of employee
        """
        return self.__salary

    def get_years_of_work(self):
        """
            This method returns years of work of employee
        """
        return self.__years_of_work

    @property
    def get_full_info_about_employee(self):
        """
            This method returns full info about employee
        """
        return f"Name: {self.__name} {self.__last_name}; " \
               f"Age: {self.__age}; " \
               f"Gender: {self.__gender}; " \
               f"Position: {self.__position}; " \
               f"Salary: {self.__salary}$; " \
               f"Years of work: {self.__years_of_work} years."

    @staticmethod
    def bonuses(salary, overtime):
        """
            This method returns overtime bonuses for employee
        """
        rate = salary / 160
        return rate * 2 * overtime


if __name__ == "__main__":
    employee = Employee(
        "Harry",
        "Douboi",
        32,
        True,
        "Manager",
        1500,
        1.5)
    print(employee.get_full_info_about_employee)
    print(employee.bonuses(1500, 20))
    print(employee.get_full_name())
# Good code but it could be better if you will modify state of object in some method -2 points
