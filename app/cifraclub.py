from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

cifraclub_url = "https://www.cifraclub.com.br/"

class CifraClub():
    def __init__(self):
        self.driver = webdriver.Remote("http://selenium:4444/wd/hub", DesiredCapabilities.FIREFOX)

    def cifra(self, artist: str, song: str) -> dict:
        result = {}

        url = cifraclub_url + artist + "/" + song
        result['cifraclub_url'] = url
        try:
            self.driver.get(url)
            self.get_details(result)
            self.get_cifra(result)
            self.driver.quit()
        except: # NoSuchElementException
            result['error'] = "error description"

        return result

    def get_details(self, result):
        content = self.driver.find_element(By.CLASS_NAME, 'cifra').get_attribute('outerHTML')
        soup = BeautifulSoup(content, 'html.parser')
        result['name'] = soup.find('h1', class_='t1').text
        result['artist'] = soup.find('h2', class_='t3').text

        img_youtube = soup.find('div', class_='player-placeholder').img['src']
        cod = img_youtube.split('/vi/')[1].split('/')[0]
        result['youtube_url'] = f"https://www.youtube.com/watch?v={cod}"

    def get_cifra(self, result):
        content = self.driver.find_element(By.CLASS_NAME, 'cifra_cnt').get_attribute('outerHTML')
        soup = BeautifulSoup(content, 'html.parser')
        result['cifra'] = soup.find('pre').text.split('\n')
