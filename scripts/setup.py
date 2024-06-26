from .files_config import download_verification
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager

#preparando o driver
def driver_setup(download_directory):
    options = ChromeOptions()
    options.add_argument("--headless") 

    #preferencias para o download 
    preferences = {
        "download.default_directory": f"{download_directory}",
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": False,
        "profile.default_content_setting_values.automatic_downloads": 1,
    }
    options.add_experimental_option("prefs", preferences)

    service = ChromeService(ChromeDriverManager().install())
    d = webdriver.Chrome(service=service, options=options)

    d.implicitly_wait(5) #tempo de espera antes dos elementos aparecerem
    return d

#fazendo a busca do link do primeiro video no youtube
def arbovirus_search(query, download_directory):
    driver = driver_setup(download_directory)

    search_url = f"https://www.ncbi.nlm.nih.gov/nuccore/?term={query}"

    driver.get(search_url) 

    #selecionando campos especificos para as sequencias e achando o botao p baixar as seq
    driver.find_element(By.CSS_SELECTOR, "#seqsendto > a:nth-child(1)").click()
    driver.find_element(By.CSS_SELECTOR, "#complete_rec").click()
    driver.find_element(By.CSS_SELECTOR, "#dest_File").click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#file_format > option:nth-child(7)"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#file_sort > option:nth-child(2)"))).click()
    driver.find_element(By.CSS_SELECTOR, "#submenu_File > button:nth-child(3)").click()

    time.sleep(120) #talvez aumentar esse tempo depois

    #conferindo dados
    print(f"link atual do driver: {driver.current_url}")
    download_verification()