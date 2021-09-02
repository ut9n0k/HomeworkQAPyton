# Создайте класс с описанием любой компании. К примеру тошиба или глобал лоджик. Company.
# Буду оценивать полноту описанного класса и буду снимать за все лишнее балы. Хочу видеть чистый код.
# Ожидажю увидеть чистый код с аннотациями. Пока что без связей первого класса со вторым.
# Во всех методах ожидаю увидеть докстринги с вменяемым описанием.

class Company:
    def __init__(self,
                 name: str = None,
                 industry: str = None,
                 foundation_year: int = None,
                 location: str = None,
                 number_of_employees: int = None,
                 site: str = None
                 ):
        self.__name = name
        self.__industry = industry
        self.__foundation_year = foundation_year
        self.__location = location
        self.__number_of_employees = number_of_employees
        self.__site = site

    def get_name(self):
        """
            This method returns name of company
        """
        return self.__name

    def get_industry(self):
        """
            This method returns industry of company
        """
        return self.__industry

    def get_foundation_year(self):
        """
            This method returns foundation year of company
        """
        return self.__foundation_year

    def get_location(self):
        """
            This method returns location of company
        """
        return self.__location

    def get_number_of_employees(self):
        """
            This method returns number of employees of company
        """
        return self.__number_of_employees

    def get_site(self):
        """
            This method returns site of company
        """
        return self.__site

    @property
    def get_full_info_about_company(self):
        """
            This method returns full info about company
        """
        return f"Company name: {self.__name}; " \
               f"Industry: {self.__industry}; " \
               f"Foundation year: {self.__foundation_year}; " \
               f"Location: {self.__location}; " \
               f"Number of employees: {self.__number_of_employees}; " \
               f"Company site: {self.__site}."

    @staticmethod
    def mail_for_new_employee(number_of_employees):
        """
            This method returns mail for new member of company
        """
        new_num = number_of_employees + 1
        return f"Greeting, you're a {new_num} employee in our company!"


if __name__ == "__main__":
    cd_projekt_red = Company(
        "CDPojektRed",
        "Video Games",
        None,
        "Warsaw, Poland",
        None,
        "sdprojekt.com")

    print(cd_projekt_red.get_full_info_about_company)
    print(cd_projekt_red.mail_for_new_employee(1111))
    print(cd_projekt_red.get_name(), cd_projekt_red.get_site())
