from .files_config import download_verification
from .data_handling import get_num_seq
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
    #options.add_argument("--headless") 
    #options.add_argument('--disable-popup-blocking') 

    #preferencias para o download 
    preferences = {
        "download.default_directory": f"{download_directory}",
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": False,
        "profile.default_content_setting_values.automatic_downloads": 1,
    }
    options.add_experimental_option("prefs", preferences)

    service = ChromeService(executable_path=ChromeDriverManager().install())
    d = webdriver.Chrome(service=service, options=options)

    d.implicitly_wait(5) 
    return d

def arbovirus_search(query, download_directory, sleep_time):
    driver = driver_setup(download_directory)

    search_url = f"https://www.ncbi.nlm.nih.gov/nuccore/?term={query}"

    driver.get(search_url) 

    #selecionando campos especificos para as sequencias e achando o botao p baixar as seq
    driver.find_element(By.CSS_SELECTOR, "#seqsendto > a:nth-child(1)").click()
    driver.find_element(By.CSS_SELECTOR, "#complete_rec").click()
    driver.find_element(By.CSS_SELECTOR, "#dest_File").click()

    seq_num = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#submenu_File_hint"))).text

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#file_format > option:nth-child(7)"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#file_sort > option:nth-child(2)"))).click()
    driver.find_element(By.CSS_SELECTOR, "#submenu_File > button:nth-child(3)").click()

    while(True):
        time.sleep(sleep_time)
        if download_verification():
            return get_num_seq(seq_num)
        else:
            #poderia colocar mais um sleep aqui, ver melhor dps
            return -1