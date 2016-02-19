from selenium.webdriver.common.by import By

class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""

    HEADER = (By.TAG_NAME, 'h1')

    ZEBRA_LINE = (By.CLASS_NAME, 'zebra')

    LION_LINE = (By.CLASS_NAME, 'lion')

    ELEPHANT_LINE = (By.CLASS_NAME, 'elephant')

    GIRAFFE_LINE = (By.CLASS_NAME, 'giraffe')

    STATE_DROPDOWN = (By.NAME, 'state')

    CHECKOUT_BUTTON = (By.NAME, 'commit')

class CheckOutPageLocators(object):
    """A class for checkout page locators. All checkout page locators should come here"""

    HEADER = (By.TAG_NAME, 'h1')
    
    ZEBRA_LINE = (By.CLASS_NAME, 'zebra')

    LION_LINE = (By.CLASS_NAME, 'lion')

    ELEPHANT_LINE = (By.CLASS_NAME, 'elephant')

    GIRAFFE_LINE = (By.CLASS_NAME, 'giraffe')
    
    SUBTOTAL_LINE = (By.ID, 'subtotal')

    TAXES_LINE = (By.ID, 'taxes')

    TOTAL_LINE = (By.ID, 'total')