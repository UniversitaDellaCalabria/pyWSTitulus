import os

BASE_ROOT = os.path.dirname(os.path.abspath(__file__))

# test use
PROT_URL = 'https://titulus-unical.pp.cineca.it/titulus_ws/services/Titulus4'
PROT_URL_WSDL = 'https://titulus-unical.pp.cineca.it/titulus_ws/services/Titulus4?wsdl'

PROT_LOGIN = 'test-ws'
PROT_PASSW = 'Menadit0!'
# END test use

PATH_ROOT = 'titulus_ws'
PATH_XML_TEMPLATES = f'{BASE_ROOT}/xml_templates'

DOCUMENTO_ENTRATA_XML ="documento_entrata.xml"
FASCICOLO_XML ="fascicolo.xml"

DOCUMENTO_ENTRATA_PATH = f'{PATH_XML_TEMPLATES}/{DOCUMENTO_ENTRATA_XML}'
FASCICOLO_PATH = f'{PATH_XML_TEMPLATES}/{FASCICOLO_XML}'

PATH_ALLEGATI = f'{BASE_ROOT}/attachments'
