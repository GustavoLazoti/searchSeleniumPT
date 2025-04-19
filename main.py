from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def clicar_letra(driver, letra, timeout=10):
    """
    Clica no botão de letra no índice de cursos.
    :param driver: Instância do Selenium WebDriver.
    :param letra: Letra (char) a ser clicada, ex: 'B'.
    :param timeout: Tempo máximo de espera pelo elemento.
    """
    xpath = f'//a[@href="indcurso.asp?letra={letra}" and @accesskey="{letra}"]'
    botao = WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable((By.XPATH, xpath))
    )
    botao.click()