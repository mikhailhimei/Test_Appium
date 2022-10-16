from .base_page import BasePage
from .locators import *

class MainPage(BasePage): 
   #Начальная заствка с геолокаицей
   def popup_geolocation(self):
      self.drivers.find_element(*Lamoda.BTN_GEOLOCATION).click()
      self.drivers.find_element(*Lamoda.BTN_ANDROID_GEOLOCATION).click()
      self.drivers.find_element(*Lamoda.INFORMATION_DELIVERY).click() 
   
   #Попап с информацией премиум
   def popup_premiun(self):
      self.drivers.find_element(*Lamoda.BTN_PREMIUM).click()

   #Поиск 
   def search(self, text):
      self.drivers.find_element(*Lamoda.OPEN_SEARCH).click()  
      self.drivers.find_element(*Lamoda.TEXT_SEARCH).send_keys(text)
      self.start_search()
   
   
   def elements_name(self):
      element = self.drivers.find_element(*Lamoda.OPEN_TITLE_SORT)
      text = element.text
      return text

   #Нажать на кнопку сортировки
   def open_sort(self):
      self.drivers.find_element(*Lamoda.OPEN_TITLE_SORT).click()

   #Сортировать по возрастанию цены
   def sort_ascending(self):
      self.open_sort()
      self.drivers.find_element(*Lamoda.SORT_ASCENDING).click()
      return self.elements_name()

   #Сортировать по убыванию цены
   def sort_descending(self):
      self.open_sort()
      self.drivers.find_element(*Lamoda.SORT_DESCENDING).click()
      return self.elements_name()
   
   #Сортировать по новинкам
   def sort_novelties(self):
      self.open_sort()
      self.drivers.find_element(*Lamoda.SORT_NOVELTIES).click()
      return self.elements_name()

   #Сортировать по скидкам
   def sort_discounts(self):
      self.open_sort()
      self.drivers.find_element(*Lamoda.SORT_DISCOUNTS).click()
      return self.elements_name()

   #Сортировать по популярности 
   def sort_popularity(self):
      self.open_sort()
      self.drivers.find_element(*Lamoda.SORT_POPULARITY).click()
      return self.elements_name()

   #Скрол        
   def scroll(self):
      return self.drivers.find_element(*Lamoda.SHEET)
      