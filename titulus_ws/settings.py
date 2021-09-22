import os


PROT_DOC_ENCODING = "utf-8"

BASE_ROOT = os.path.dirname(os.path.abspath(__file__))

# test use
PROT_URL_TEST = "https://titulus-YOURORG.pp.cineca.it/titulus_ws/services/Titulus4"
PROT_URL_WSDL_TEST = (
    "https://titulus-YOURORG.pp.cineca.it/titulus_ws/services/Titulus4?wsdl"
)

PROT_LOGIN_TEST = "THAT-USER"
PROT_PASSW_TEST = "THAT-PASSWORD"
# END test use

# production use
PROT_URL = "prot_url"
PROT_URL_WSDL = f"{PROT_URL}?wsdl"
# END production use

PROT_LOGIN = "ws_user_login"
PROT_PASSW = "ws_user_password"

PATH_ROOT = "titulus_ws"
PATH_XML_TEMPLATES = f"{BASE_ROOT}/xml_templates"

DOCUMENTO_ENTRATA_XML = "documento_entrata.xml"
FASCICOLO_XML = "fascicolo.xml"

DOCUMENTO_ENTRATA_PATH = f"{PATH_XML_TEMPLATES}/{DOCUMENTO_ENTRATA_XML}"
FASCICOLO_PATH = f"{PATH_XML_TEMPLATES}/{FASCICOLO_XML}"
