from locators import MainPageLocators, CheckOutPageLocators
from random import randint
from selenium.webdriver.support.ui import Select

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

class MainPage(BasePage):
    """Main page methods belong here"""

    def is_title_matches(self):
        """Verifies that correct page is returned"""
        return "JungleSocks" in self.driver.title

    def is_correct_header(self):
        """Verifies that the correct header is displayed"""
        return "Welcome To Jungle Socks!" in self.driver.find_element(*MainPageLocators.HEADER).text

    def enter_quantity(self, animal, number):
        """Enters quantity for specified animal sock"""
        animal = self.driver.find_element_by_class_name(animal)
        quantity = animal.find_element_by_tag_name('input')
        quantity.send_keys(number)

    def get_in_stock_amount(self, animal):
        """Gets displayed quantity for animal"""
        animal = self.driver.find_element_by_class_name(animal)
        in_stock = animal.find_elements_by_tag_name('td')[2].text #Need id or data-element
        return int(in_stock)

    def generate_quantity(self, animal):
        """Generates a random quantity to order based on provided animal"""
        count = randint(0, self.get_in_stock_amount(animal))
        return count

    def fill_order_data(self, zebra_count, lion_count, elephant_count, giraffe_count):
        """Fills in order data for all the fields"""
        self.enter_quantity('zebra', zebra_count)
        self.enter_quantity('giraffe', giraffe_count)
        self.enter_quantity('lion', lion_count)
        self.enter_quantity('elephant', elephant_count)

    def get_price (self, animal):
        """Gets displayed price for animal"""
        animal = self.driver.find_element_by_class_name(animal)
        price = animal.find_elements_by_tag_name('td')[1].text #Need id or data-element
        return float(price)

    def is_checkout_enabled(self):
        """Verifies if checkout button is enabled"""
        return self.driver.find_element(*MainPageLocators.CHECKOUT_BUTTON).is_enabled()

    def select_state(self, state=None):
        """Selects state from dropdown menu. If no state is provided, a random state is selected"""
        select = Select(self.driver.find_element(*MainPageLocators.STATE_DROPDOWN))
        if state==None:
            state_number = randint(1,50)
            select.select_by_index(state_number)
        else:
            select.select_by_visible_text(state)

    def submit_form(self):
        """Submits the form"""
        self.driver.find_element(*MainPageLocators.CHECKOUT_BUTTON).click()

class CheckOutPage(BasePage):
    """Check out page methods belong here"""

    def is_correct_header(self):
        """Verifies that the correct header is displayed"""
        return "Please Confirm Your Order" in self.driver.find_element(*CheckOutPageLocators.HEADER).text

    def calculate_subtotal(self, zebra_count=0, lion_count=0, elephant_count=0, giraffe_count=0):
        """Calculates subtotal of order"""
        subtotal=0
        if zebra_count > 0:
            subtotal = subtotal + zebra_count * 13.00
        if lion_count > 0:
            subtotal = subtotal + lion_count * 20.00
        if elephant_count > 0:
            subtotal = subtotal + elephant_count * 35.00
        if giraffe_count > 0:
            subtotal = subtotal + giraffe_count * 17.00
        return subtotal

    def calculate_taxes(self, state, subtotal):
        """Calculate taxes for order"""
        if state == 'California':
            tax = subtotal * 0.08
        elif state == 'New York':
            tax = subtotal * 0.06
        elif state == 'Minnesota':
            tax = 0
        else:
            tax = subtotal * 0.05
        return float(format(tax, '.2f'))

    def calculate_total(self, state, subtotal):
        """Calculates total for order"""
        total = 0
        total = subtotal + self.calculate_taxes(state, subtotal)
        return total

    def get_quantity(self, animal):
        """Gets displayed quantity for animal"""
        animal = self.driver.find_element_by_class_name(animal)
        in_stock = animal.find_elements_by_tag_name('td')[2].text #Need id or data-element
        return int(in_stock)

    def get_subtotal(self):
        """Gets the subtotal for the order"""
        subtotal = self.driver.find_element(*CheckOutPageLocators.SUBTOTAL_LINE).text.lstrip('$').replace(",", "")
        return float(subtotal)

    def get_taxes(self):
        """Gets the taxes for the order"""
        taxes = self.driver.find_element(*CheckOutPageLocators.TAXES_LINE).text.lstrip('$').replace(",","")
        return float(taxes)

    def get_total(self):
        """Gets the subtotal for the order"""
        total = self.driver.find_element(*CheckOutPageLocators.TOTAL_LINE).text.lstrip('$').replace(",", "")
        return float(total)
