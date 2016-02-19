# Testing Jungle Socks

To run this, clone the test repo available here: https://paulinadao@bitbucket.org/paulinadao/junglesocks.git

You will need Python 2.7.9 or higher. To check your version of Python, open up Terminal and type in the command

```
python -V
```

You will also need to install Selenium. Python 3.4 has pip available in the standard library. You can use *pip* to install Selenium. For instructions on how to install pip, visit this link: https://pip.pypa.io/en/stable/installing/

```
pip install selenium
```

To run the tests, navigate to the the directory where all the files are. Run this command

```
python -m unittest test
```

### Notes
* Quantity is spelled incorrectly on the main page
* Users should not be able to proceed without selecting a state. This results in a 500. The service should also return a 422 in case the UI is not forcing validation
* Validation is necessary on the input fields. Users should only be able to enter in numbers. Additionally, the service should return a 422 in case the UI is failing.
* Users should not be able to submit a quantity that is greater than the in stock amount.
* Adding ids, data-elements, or something to have Selenium more easily identify columns would be helpful for better implementation of the page object model