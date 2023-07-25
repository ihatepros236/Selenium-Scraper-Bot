from RPA.Browser.Selenium import Selenium
from datetime import datetime

br = Selenium()


class Robot:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print("Hello, my name is " + self.name)
        print('\n')

    def say_goodbye(self):
        print("Goodbye, my name is " + self.name)

    def open_webpage(self, webpage):
        br.open_available_browser(webpage)
        

    def research_scientists(self, scientists):
        for scientist in scientists:
            self.research_scientist(scientist)

    def research_scientist(self, scientist):
        print(f"Researching scientist: {scientist}")
        print("Opening browser and Navigating through Wikipedia")
        self.open_webpage("https://www.wikipedia.org")
        self.search_scientist(scientist)
        birth_date, death_date = self.get_dates()
        age = self.calculate_age(birth_date, death_date)
        first_paragraph = self.get_first_paragraph()
        self.display_information(scientist, birth_date, death_date, age, first_paragraph)
        br.close_browser()

    def search_scientist(self, scientist):
        br.input_text("xpath://input[@id='searchInput']", scientist)
        br.press_keys("xpath://input[@id='searchInput']", "ENTER")
        

    def get_dates(self):
        
        element_Bd = br.find_element("xpath://span[@class='bday']")
        birth_date= br.get_element_attribute(element_Bd, "innerHTML")
        
        element_Dd = br.find_element("xpath://th[text()='Died']/..//td/span")
        death_date = br.get_element_attribute(element_Dd, "innerHTML")
        death_date = death_date.strip("()")
     
        return birth_date, death_date

    def calculate_age(self, birth_date, death_date):
        
        birth_date = datetime.strptime(birth_date, "%Y-%m-%d")
        death_date = datetime.strptime(death_date, "%Y-%m-%d")
        age = death_date.year - birth_date.year
        return age

    def get_first_paragraph(self):
        index=1
        
        first_paragraph = br.get_text("xpath://*[@id='mw-content-text']/div[1]/p[1]")
        while len(first_paragraph)==0:
            index+=1
            first_paragraph = br.get_text("xpath://*[@id='mw-content-text']/div[1]/p[" + str(index) + "]")
        return first_paragraph

    def display_information(self, scientist, birth_date, death_date, age, first_paragraph):
        print(f"Scientist: {scientist}")
        print(f"Birth Date: {birth_date}")
        print(f"Death Date: {death_date}")
        print(f"Age: {age}")
        print(f"First Paragraph: {first_paragraph}")
        print("\n")
        

# Create an instance of the Robot class
robot = Robot("Quandrinaut")


def introduce_yourself():
    robot.say_hello()


def main():
    introduce_yourself()
    robot.research_scientists(SCIENTISTS)
    robot.say_goodbye()


if __name__ == "__main__":
    main()