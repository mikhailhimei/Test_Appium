from appium.webdriver.common.appiumby import AppiumBy


class Lamoda():
    #Кнопка продолжить геолокация
    BTN_GEOLOCATION =(AppiumBy.ID, "com.lamoda.lite:id/buttonPrimary")
    
    #Доступ к геолокации
    BTN_ANDROID_GEOLOCATION=(AppiumBy.ID,"com.android.permissioncontroller:id/permission_allow_foreground_only_button")

    #Информация о доставке
    INFORMATION_DELIVERY = (AppiumBy.ID,"com.lamoda.lite:id/advantages_ok")

    #Информация о премиуме
    BTN_PREMIUM = (AppiumBy.ID,"com.lamoda.lite:id/closeButton")

    #Открыть поле поиска
    OPEN_SEARCH = (AppiumBy.ID, "com.lamoda.lite:id/searchTextView")
    
    #Ввести в поле поиска текст
    TEXT_SEARCH = (AppiumBy.ID, "com.lamoda.lite:id/searchEditTextCurrent")

    #Открыть сортировку
    OPEN_TITLE_SORT = (AppiumBy.ID, "com.lamoda.lite:id/sortTitleTextView")

    #Сортировать по популярности
    SORT_POPULARITY = (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.View/android.widget.ScrollView/android.view.View[1]")
    
    #Сортировать по возврастанию цены
    SORT_ASCENDING = (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.View/android.widget.ScrollView/android.view.View[2]")
    
    #Сортировать по убыванию цены
    SORT_DESCENDING = (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.View/android.widget.ScrollView/android.view.View[3]")
    
    #Сортировать по новинкам
    SORT_NOVELTIES = (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.View/android.widget.ScrollView/android.view.View[4]")
    
    #Сортировать по скидкам
    SORT_DISCOUNTS = (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.View/android.widget.ScrollView/android.view.View[5]")

    #Тултип с информацией при первом поиске
    TOOLTIP = (AppiumBy.ID, "com.lamoda.lite:id/tooltip_text")

    #Нажатие для скролла
    SHEET = (AppiumBy.ID, "com.lamoda.lite:id/recyclerView")

    #Панель с параметрами для уточнения запроса
    QUERY_REFINEMENT_PANEL = (AppiumBy.ID, "com.lamoda.lite:id/catalogHeaderContainer")