from _pytest import mark
from _pytest.mark.structures import Mark
from selenium import webdriver
import pytest
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

Kunci = [
    ("masrisyad","@test1234"),      #username benar password salah
    ("risyad123","@Test12345"),      #username salah password benar
    ("risyadabdala","@test1234"),      #username salah password salah
]

@pytest.fixture
def setup():
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://demoqa.com/login")
    driver.implicitly_wait(10)
    yield driver
    driver.quit()        

def test_login_berhasil(setup):
    
    setup.find_element_by_id("userName").send_keys("masrisyad")
    setup.find_element_by_id("password").send_keys("@Test12345")
    setup.find_element_by_id("login").click()
    time.sleep(3)
    
    mainHeader = setup.find_element_by_class_name("main-header").text
    
    assert mainHeader == "Profile"
    
@pytest.mark.parametrize('a,b', Kunci)
def test_login_salah(setup,a,b):
    
    setup.find_element_by_id("userName").send_keys(a)
    setup.find_element_by_id("password").send_keys(b)
    setup.find_element_by_id("login").click()
    
    invalidText = setup.find_element_by_id("name").text
    
    assert invalidText == "Invalid username or password!"
