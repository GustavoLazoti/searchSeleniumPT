from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from bs4 import BeautifulSoup
import re
import csv

COD_FACULDADE = sorted(['0140','0150','0160','0170','0201','0203','0204','0206','0300','0400','0501','0502','0503','0504','0505','0506','0507','0508','0520','0602','0603','0604','0605','0901','0902','0903','0904','0906','0911','1000','1101','1102','1103','1104','1105','1106','1107','1108','1109','1110','1111','1113','1114','1201','1202','1203','1204','1306','1307','1308','1309','1320','1321','1501','1502','1503','1504','1505','1506','1507','1508','1509','1510','1511','1513','1514','1515','1516','1517','1518','1519','3011','3012','3013','3014','3021','3022','3023','3031','3032','3033','3034','3036','3041','3042','3043','3045','3046','3051','3052','3053','3054','3055','3061','3062','3063','3064','3065','3081','3082','3083','3087','3091','3092','3095','3101','3102','3103','3105','3112','3113','3117','3118','3121','3124','3125','3131','3134','3135','3138','3139','3141','3142','3143','3145','3151','3152','3153','3154','3155','3161','3162','3163','3164','3165','3181','3182','3185','3186','3241','3242','3243','3331','5402','6800','6810','7001','7002','7003','7005','7010','7015','7020','7030','7035','7040','7045','7055','7065','7075','7080','7085','7092','7093','7105','7110','7210','7220','7230'])
COD_CURSOS = sorted(['8031','8086','9022','L344','9135','9181','9219','9238','9240','9652','9853','L041','8083','8524','8571','9011','9185','9081','9147','9254','8509','9204','9817','9821','L252','8258','9003','9013','9015','9016','9119','9210','9494','9540','L123','9152','9351','9002','9012','9041','9069','9089','9096','9099','9104','9113','9123','9125','9141','9146','9194','9196','9209','9223','9252','9455','9813','L187','L202','L209','L217','L221','L223','L254','L298','8184','9020','9023','9025','9048','9071','9074','9075','9105','9112','9139','9205','9225','9257','9707','9740','9835','9918','L205','L227','L258','L295','L303','L331','8408','9126','9348','9448','9891','L192','L285','8067','9078','9229','9819','9832','8393','9006','9132','9133','9143','9182','9694','9773','9779','L109','9548','9026','9751','9752','9760','9818','9847','9910','L090','9243','9347','8251','9787','L047','L173','9841','L256','9554','8109','9040','9046','9145','9917','8036','9116','9129','9224','L167','L231','L286','8259','9155','L188','8183','8358','8427','8494','9019','9056','9098','9127','9134','9192','9195','9229','9353','9379','9381','9397','9499','9688','9785','L078','L112','L147','L215','L218','L229','9385','9687','9696','9709','L096','L224','L236','9720','L150','9107','L208','9736','9500','9076','8399','9070','9072','9754','9790','9904','L010','9212','9226','L079','L204','L214','8413','8458','9131','9914','L097','L288','9556','9791','9068','9162','L040','8411','8377','9087','8014','8102','8111','8363','8364','9157','A001','A006','A013','9121','9345','9474','L162','L233','L239','9912','8005','9140','9869','9888','8405','9235','L021','L140','L194','L346','9504','9890','L066','L138','L299','9010','9563','9152','9242','9994','8015','9759','9990','9991','8311','8409','8417','L181','9074','9470','9873','L260','8156','8341','9173','9085','L029','8323','8374','9082','9084','9898','9933','L088','L175','9186','A004','L069','8309','9165','9188','9213','9078','8397','9485','9850','8463','9111','L275','L251','9725','9726','L158','L003','L009','L015','L024','L178','8093','8114','8342','9054','9668','9675','9717','9731','9774','9894','L095','8029','8519','9061','9722','9801','L023','L056','L310','9770','9885','L155','L226','9058','9895','L305','8337','9070','9148','9178','9207','9848','L131','8307','9876','L134','8438','8439','9191','9222','9231','9476','9870','9889','L035','9108','9109','L052','L085','L117','L119','L213','9773','9670','L308','L309','9130','8002','8264','9807','9878','9879','L246','L272','8009','9043','9053','9205','9227','9716','9829','9866','9867','L070','8316','9110','9117','9936','L089','8097','8288','8398','9045','L030','L091','8442','9164','9921','L130','L179','9156','9498','9730','9763','9808','L008','L034','9633','8515','9092','9862','L124','9157','9628','9629','9630','9993','9090','L100','L164','9473','L122','L284','8407','9723','9727','9743','L153','L261','8464','8516','9491','9709','9122','9168','9179','L116','9640','L207','9380','9644','9645','L142','L186','L143','L211','L297','9713','L071','8366','9156','9157','9189','9240','9257','9885','9927','L189','L273','L274','L277','L278','L280','L281','L282','L311','L321','L329','8138','8149','9501','9549','9833','L068','L067','L101','L136','L304','8011','9076','9163','9177','9183','9217','9875','9995','9996','8141','8152','9861','L161','8143','9890'])

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

def extrair_blocos(driver):
    """
    Extrai os textos entre os h2:
    - Provas de Ingresso -> próximo h2
    - Classificações Mínimas -> próximo h2
    - Fórmula de Cálculo -> próximo h2
    Retorna uma tupla com as três strings.
    """
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    titulos = [
        "Provas de Ingresso",
        "Classificações Mínimas",
        "Fórmula de Cálculo"
    ]
    blocos = []
    h2s = soup.find_all("h2")
    # Para cada título, encontra o h2 correspondente e pega tudo até o próximo h2
    for titulo in titulos:
        bloco = ""
        for idx, h2 in enumerate(h2s):
            if h2.get_text(strip=True) == titulo:
                content = []
                for sib in h2.next_siblings:
                    if getattr(sib, "name", None) == "h2":
                        break
                    if getattr(sib, 'get_text', None):
                        content.append(sib.get_text(" ", strip=True))
                    elif isinstance(sib, str):
                        content.append(sib.strip())
                bloco = " ".join([c for c in content if c])
                break
        blocos.append(bloco)
    return tuple(blocos)

def pagina_nao_encontrada(driver, timeout=3):
    """
    Verifica se a página contém a mensagem de par instituição/curso não encontrado.
    :param driver: Instância do Selenium WebDriver.
    :param timeout: Tempo máximo de espera pelo elemento.
    :return: True se a mensagem for encontrada, False caso contrário.
    """
    try:
        elemento = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="cab1" and contains(text(), "Par instituição/curso não encontrado")]'))
        )
        return True
    except:
        return False


def main():
    caminho_chromedriver = r'C:/Users/Gustavo/Downloads/chromedriver-win64/chromedriver.exe'  # Altere para o caminho correto
    service = Service(executable_path=caminho_chromedriver)
    driver = webdriver.Chrome(service=service)
    cont = 0
    try:
        base_url = "https://www.dges.gov.pt/guias/detcursopi.asp?codc={}&code={}"
        arquivo_csv = "dados.csv"
        cabecalho = ['Código Faculdade', 'Código Curso', 'Provas de ingresso', 'Nota candidatura', 'Pontos provas de ingresso', 'Média do secundário', 'Provas de ingresso']
        primeira_vez = True

        for cod_faculdade in COD_FACULDADE:
            for cod_curso in COD_CURSOS:
                url = base_url.format(cod_curso, cod_faculdade)
                driver.get(url)
                WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
                if pagina_nao_encontrada(driver): continue
                provas, minimos, formula = extrair_blocos(driver)
                print(provas)
                print(minimos)
                print(formula)

                provas = provas.replace("\n", " ").replace("  ", " ").strip()
                minimos_valor = re.search(r"(\d+\s*pontos)", minimos)
                minimos_valor = minimos_valor.group(1) if minimos_valor else ""
                formula_valor = re.search(r"(\d+%)", formula)
                formula_valor = formula_valor.group(1) if formula_valor else ""
                linha = [
                    cod_faculdade,
                    cod_curso,
                    provas,
                    minimos_valor,
                    minimos_valor,
                    formula_valor,
                    formula_valor
                ]
                print(linha)
                # Escreve o cabeçalho só na primeira vez, depois só adiciona linhas
                with open(arquivo_csv, mode="a", newline="", encoding="utf-8") as arquivo:
                    escritor = csv.writer(arquivo, delimiter=";")
                    if primeira_vez:
                        escritor.writerow(cabecalho)
                        primeira_vez = False
                    escritor.writerow(linha)

    finally:
        driver.quit()
main()