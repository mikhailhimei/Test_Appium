# Test_Appium

**Информация об устройстве:**
* устройство Pixel 6, разрешение 1080px X 2400px, дюймы 6,4", плотностость пикселей 420dpi
* Версия устройства Android 11.0

**Информация, необходимая для запуска тестов:**
* версия Appium-Server 1.22.3-4
* язык Python 3.10.8 с использованием  библиотеки pytest 7.1.2, selenium 4.3.0, Appium-Python-Client 2.7.1
* тестируемое приложение Lamoda (apk версия 4.17.0_401700)

**Для того чтобы запустить тест необходимо выполнить следующие шаги:** 
1. Запустить виртуальное Android устройство 
2. Запустить Appium-Server
3. склонировать репозиторий
4. открыть папку Appium_Lamoda
5. открыть командрную строку
6. в командной строке ввести "py -m pytest --OS_name android" или "python3 -m pytest --OS_name android" и нажать Enter 
