from selenium import webdriver
import page
import unittest
from random import randint

class JungleSocksTest(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Firefox()
		self.driver.maximize_window()
		self.driver.get("https://jungle-socks.herokuapp.com/")

	def test_form_submitted_successfully(self):
		"""Verifies that a form can be submitted successfully"""
		main_page = page.MainPage(self.driver)
		assert main_page.is_title_matches(), "JungleSocks title doesn't match."
		assert main_page.is_correct_header(), "Wrong header was displayed."
		zebra_count = main_page.generate_quantity('zebra')
		lion_count = main_page.generate_quantity('lion')
		elephant_count = main_page.generate_quantity('elephant')
		giraffe_count = main_page.generate_quantity('giraffe')
		main_page.fill_order_data(zebra_count, lion_count, elephant_count, giraffe_count)
		main_page.select_state()
		main_page.submit_form()
		checkout_page = page.CheckOutPage(self.driver)
		assert checkout_page.is_correct_header(), "Wrong header was displayed."

	def test_form_cannot_be_empty(self):
		"""Verifies that a form cannot be submitted blank"""
		main_page = page.MainPage(self.driver)
		assert main_page.is_checkout_enabled() == False, "Checkout button is enabled"

	def test_invalid_input_not_accepted(self):
		"""Verifies that only numeric characters can be input into the form"""
		main_page = page.MainPage(self.driver)
		main_page.enter_quantity('zebra', 'abcdefgh') #Input text fields should only allow numeric entry
		main_page.enter_quantity('giraffe','-!$#%^&*()') #Input text fields should only allow numeric entry
		main_page.enter_quantity('elephant', main_page.get_in_stock_amount('elephant')+1) #Input should not allow user to order more than what is in stock
		assert main_page.is_checkout_enabled() == False, "Checkout button is enabled"

	def test_subtotal_calculations_displayed_correctly(self):
		"""Verifies that subtotal calculations are displayed correctly"""
		main_page = page.MainPage(self.driver)
		zebra_count = main_page.generate_quantity('zebra')
		lion_count = main_page.generate_quantity('lion')
		elephant_count = main_page.generate_quantity('elephant')
		giraffe_count = main_page.generate_quantity('giraffe')
		main_page.fill_order_data(zebra_count, lion_count, elephant_count, giraffe_count)
		main_page.select_state()
		main_page.submit_form()
		checkout_page = page.CheckOutPage(self.driver)
		assert checkout_page.is_correct_header(), "Wrong header was displayed."
		actual = checkout_page.get_subtotal()
		expected = checkout_page.calculate_subtotal(zebra_count, lion_count, elephant_count, giraffe_count)
		assert expected == actual, "Wrong subtotal was displayed. Expected: %r. Actual: %r." % (expected, actual)

	def test_sales_tax_displayed_correctly(self):
		"""Verifies that sales tax is displayed correctly"""
		main_page = page.MainPage(self.driver)
		zebra_count = main_page.generate_quantity('zebra')
		lion_count = main_page.generate_quantity('lion')
		elephant_count = main_page.generate_quantity('elephant')
		giraffe_count = main_page.generate_quantity('giraffe')
		main_page.fill_order_data(zebra_count, lion_count, elephant_count, giraffe_count)
		main_page.select_state('California') #.08% sales tax
		main_page.submit_form()
		checkout_page = page.CheckOutPage(self.driver)
		assert checkout_page.is_correct_header(), "Wrong header was displayed."
		actual_subtotal = checkout_page.get_subtotal()
		expected_subtotal = checkout_page.calculate_subtotal(zebra_count, lion_count, elephant_count, giraffe_count)
		assert expected_subtotal == actual_subtotal, "Wrong subtotal was displayed. Expected: %r. Actual: %r." % (expected_subtotal, actual_subtotal)
		actual_taxes = checkout_page.get_taxes()
		expected_taxes = checkout_page.calculate_taxes('California', expected_subtotal)
		assert expected_taxes == actual_taxes, "Wrong subtotal was displayed for California. Expected: %r. Actual: %r. est %r. ast. %r" % (expected_taxes, actual_taxes, expected_subtotal, actual_subtotal)

		self.driver.get("https://jungle-socks.herokuapp.com/")
		main_page = page.MainPage(self.driver)
		main_page.fill_order_data(zebra_count, lion_count, elephant_count, giraffe_count)
		main_page.select_state('New York') #.06% sales tax
		main_page.submit_form()
		checkout_page = page.CheckOutPage(self.driver)
		assert checkout_page.is_correct_header(), "Wrong header was displayed."
		actual_subtotal = checkout_page.get_subtotal()
		expected_subtotal = checkout_page.calculate_subtotal(zebra_count, lion_count, elephant_count, giraffe_count)
		assert expected_subtotal == actual_subtotal, "Wrong subtotal was displayed. Expected: %r. Actual: %r." % (expected_subtotal, actual_subtotal)
		actual_taxes = checkout_page.get_taxes()
		expected_taxes = checkout_page.calculate_taxes('New York', expected_subtotal)
		assert expected_taxes == actual_taxes, "Wrong taxes was displayed for New York. Expected: %r. Actual: %r." % (expected_taxes, actual_taxes)

		self.driver.get("https://jungle-socks.herokuapp.com/")
		main_page = page.MainPage(self.driver)
		main_page.fill_order_data(zebra_count, lion_count, elephant_count, giraffe_count)
		main_page.select_state('Minnesota') #0% sales tax
		main_page.submit_form()
		checkout_page = page.CheckOutPage(self.driver)
		assert checkout_page.is_correct_header(), "Wrong header was displayed."
		actual_subtotal = checkout_page.get_subtotal()
		expected_subtotal = checkout_page.calculate_subtotal(zebra_count, lion_count, elephant_count, giraffe_count)
		assert expected_subtotal == actual_subtotal, "Wrong subtotal was displayed. Expected: %r. Actual: %r." % (expected_subtotal, actual_subtotal)
		actual_taxes = checkout_page.get_taxes()
		expected_taxes = checkout_page.calculate_taxes('Minnesota', expected_subtotal)
		assert expected_taxes == actual_taxes, "Wrong taxes was displayed for Minnesota. Expected: %r. Actual: %r." % (expected_taxes, actual_taxes)


		self.driver.get("https://jungle-socks.herokuapp.com/")
		main_page = page.MainPage(self.driver)
		main_page.fill_order_data(zebra_count, lion_count, elephant_count, giraffe_count)
		main_page.select_state('Arizona') #.05% sales tax
		main_page.submit_form()
		checkout_page = page.CheckOutPage(self.driver)
		assert checkout_page.is_correct_header(), "Wrong header was displayed."
		actual_subtotal = checkout_page.get_subtotal()
		expected_subtotal = checkout_page.calculate_subtotal(zebra_count, lion_count, elephant_count, giraffe_count)
		assert expected_subtotal == actual_subtotal, "Wrong subtotal displayed for Arizona. Expected: %r. Actual: %r." % (expected_subtotal, actual_subtotal)
		actual_taxes = checkout_page.get_taxes()
		expected_taxes = checkout_page.calculate_taxes('Arizona', expected_subtotal)
		assert expected_taxes == actual_taxes, "Wrong taxes was displayed for Arizona. Expected: %r. Actual: %r." % (expected_taxes, actual_taxes)


	def test_total_displayed_correctly(self):
		"""Verifies that total is displayed correctly"""
		main_page = page.MainPage(self.driver)
		zebra_count = main_page.generate_quantity('zebra')
		lion_count = main_page.generate_quantity('lion')
		elephant_count = main_page.generate_quantity('elephant')
		giraffe_count = main_page.generate_quantity('giraffe')
		main_page.fill_order_data(zebra_count, lion_count, elephant_count, giraffe_count)
		main_page.select_state('California') #.08% sales tax
		main_page.submit_form()
		checkout_page = page.CheckOutPage(self.driver)
		assert checkout_page.is_correct_header(), "Wrong header was displayed."
		actual_subtotal = checkout_page.get_subtotal()
		expected_subtotal = checkout_page.calculate_subtotal(zebra_count, lion_count, elephant_count, giraffe_count)
		assert expected_subtotal == actual_subtotal, "Wrong subtotal was displayed. Expected: %r. Actual: %r." % (expected_subtotal, actual_subtotal)
		actual_taxes = checkout_page.get_taxes()
		expected_taxes = checkout_page.calculate_taxes('California', expected_subtotal)
		assert expected_taxes == actual_taxes, "Wrong taxes displayed for California. Expected: %r. Actual: %r." % (expected_taxes, actual_taxes)
		actual_total = checkout_page.get_total()
		expected_total = checkout_page.calculate_total('California', expected_subtotal)
		assert expected_total == actual_total, "Wrong total was displayed for California. Expected: %r. Actual: %r." % (expected_total, actual_total)

	def test_zero_quantity_calculated_correctly(self):
		main_page = page.MainPage(self.driver)
		main_page.fill_order_data(0, 0, 0, 0)
		main_page.select_state('California') #.08% sales tax
		main_page.submit_form()
		checkout_page = page.CheckOutPage(self.driver)
		assert checkout_page.is_correct_header(), "Wrong header was displayed."
		actual_subtotal = checkout_page.get_subtotal()
		expected_subtotal = 0.0
		assert expected_subtotal == actual_subtotal, "Wrong subtotal was displayed. Expected: %r. Actual: %r." % (expected_subtotal, actual_subtotal)
		actual_taxes = checkout_page.get_taxes()
		expected_taxes = 0.0
		assert expected_taxes == actual_taxes, "Wrong taxes  displayed for California. Expected: %r. Actual: %r." % (expected_taxes, actual_taxes)
		actual_total = checkout_page.get_total()
		expected_total = 0.0
		assert expected_total == actual_total, "Wrong total was displayed for California. Expected: %r. Actual: %r." % (expected_total, actual_total)

	def tearDown(self):
		self.driver.close()

