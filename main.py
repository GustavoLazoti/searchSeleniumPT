from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

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


def main():
    cod_faculdade = [
    '0140', '0150', '0160', '0170', '0201', '0203', '0204', '0206', '0300', '0400', '0501', '0502', '0503', '0504',
    '0505', '0506', '0507', '0508', '0520', '0602', '0603', '0604', '0605', '0901', '0902', '0903', '0904', '0906',
    '0911', '1000', '1101', '1102', '1103', '1104', '1105', '1106', '1107', '1108', '1109', '1110', '1111', '1113',
    '1114', '1201', '1202', '1203', '1204', '1306', '1307', '1308', '1309', '1320', '1321', '1501', '1502', '1503',
    '1504', '1505', '1506', '1507', '1508', '1509', '1510', '1511', '1513', '1514', '1515', '1516', '1517', '1518',
    '1519', '3011', '3012', '3013', '3014', '3021', '3022', '3023', '3031', '3032', '3033', '3034', '3036', '3041',
    '3042', '3043', '3045', '3046', '3051', '3052', '3053', '3054', '3055', '3061', '3062', '3063', '3064', '3065',
    '3081', '3082', '3083', '3087', '3091', '3092', '3095', '3101', '3102', '3103', '3105', '3112', '3113', '3117',
    '3118', '3121', '3124', '3125', '3131', '3134', '3135', '3138', '3139', '3141', '3142', '3143', '3145', '3151',
    '3152', '3153', '3154', '3155', '3161', '3162', '3163', '3164', '3165', '3181', '3182', '3185', '3186', '3241',
    '3242', '3243', '3331', '5402', '6800', '6810', '7001', '7002', '7003', '7005', '7010', '7015', '7020', '7030',
    '7035', '7040', '7045', '7055', '7065', '7075', '7080', '7085', '7092', '7093', '7105', '7110', '7210', '7220',
    '7230'
    ]
    # Caminho para o chromedriver.exe
    caminho_chromedriver = r'C:\caminho\para\chromedriver.exe'  # Altere para o caminho correto

    # Crie o Service e passe para o Chrome
    service = Service(executable_path=caminho_chromedriver)
    driver = webdriver.Chrome(service=service)
    try:
        driver.get("URL_DA_PAGINA_DO_INDICE_DE_CURSOS")  # Coloque a URL real aqui
        clicar_letra(driver, 'B')
        input("Pressione Enter para sair...")
    finally:
        driver.quit()