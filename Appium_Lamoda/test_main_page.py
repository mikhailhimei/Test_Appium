from .pages.MainPage import MainPage
from .pages.locators import *
  

def test_sorting_search_results(drivers):
    page = MainPage(drivers) 

    page.popup_geolocation() 

    page.popup_premiun()

    page.search("Nike")

    assert page.is_element_present(*Lamoda.TOOLTIP)

    page.is_back()

    assert page.elements_name() == 'По популярности'
    
    assert page.sort_ascending() == 'По возрастанию цены'

    assert page.sort_descending() == 'По убыванию цены'

    assert page.sort_novelties() == 'По новинкам'

    assert page.sort_discounts() == 'По скидкам'

    assert page.sort_popularity() == 'По популярности'
        

def test_swipe_elements(drivers):
    page = MainPage(drivers)

    page.popup_geolocation()

    page.popup_premiun()

    page.search("Nike")

    assert page.is_element_present(*Lamoda.TOOLTIP)

    page.is_back()

    page.scroll_element(page.scroll())

    assert page.is_not_element_present(*Lamoda.QUERY_REFINEMENT_PANEL)
    
