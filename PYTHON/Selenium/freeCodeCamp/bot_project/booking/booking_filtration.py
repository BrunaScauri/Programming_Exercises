# from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class BookingFiltration:
  def __init__ (self, driver:WebDriver):
    self.driver = driver

  def sort_price_lowest_first(self):
    drop_down_menu = self.driver.find_element(By.CSS_SELECTOR, 'button[data-testid="sorters-dropdown-trigger"]')
    drop_down_menu.click()
    lowest_price_element = self.driver.find_element(By.CSS_SELECTOR, 'button[data-id="price"]')
    lowest_price_element.click()
    
  # def apply_star_rating(self):
    # star_filtration_box = self.driver.find_element(By.CSS_SELECTOR, 'data-testid="filter-class"')
    # star_child_sidebar = self.driver.find_elements(By.CSS_SELECTOR, 'name="class=5"')
    # star_child_elements = star_child_sidebar.find_elements(By.CLASS_NAME, 'bbdb949247')
    # star_child_sidebar.click()
    
    # for star_value in star_values:
    #   for star_element in star_child_elements:
    #     if str(star_element.get_attribute('innerHTML')).strip() == f'{star_value} stars':
    #       star_element.click()