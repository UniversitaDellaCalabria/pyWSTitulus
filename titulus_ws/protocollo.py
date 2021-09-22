import xml.etree.ElementTree as ET

from requests import Session
from requests.auth import HTTPBasicAuth

from zeep import Client, Settings, xsd
from zeep.transports import Transport


class WSTitulusClient(object):
    """ """

    def __init__(self, wsdl_url, username, password, **kwargs):

        self.username = username
        self.password = password
        self.wsdl_url = wsdl_url

        # zeep
        self.client = None
        self.service = None

        # attachments
        self.allegati = []

    def connect(self):
        """ """
        try:
            session = Session()
            settings = Settings(strict=False, xml_huge_tree=True)
            session.auth = HTTPBasicAuth(self.username, self.password)
            transport = Transport(session=session)
            self.client = Client(self.wsdl_url, transport=transport, settings=settings)
            self.service = self.client.bind("Titulus4Service", "Titulus4")
        except Exception as error:
            print(f"Errore connessione: {error}")
        return self.client

    def is_connected(self):
        return True if self.client else False

    def assure_connection(self):
        if not self.is_connected():
            self.connect()

    def protocolla(self, doc, allegati=[]):
        self.assure_connection()

        num_prot = None

        # self.client.namespaces
        # {'xsd': 'http://www.w3.org/2001/XMLSchema',
        #  'ns0': 'https://titulus-unical.pp.cineca.it/titulus_ws/services/Titulus4',
        #  'ns1': 'http://schemas.xmlsoap.org/soap/encoding/',
        #  'ns2': 'http://www.kion.it/titulus'}

        # never used
        # attachmentBean_type = self.client.get_type("ns2:AttachmentBean")
        attachmentBeans_type = self.client.get_type("ns0:ArrayOf_tns1_AttachmentBean")
        saveParams = self.client.get_type("ns2:SaveParams")()
        attachmentBeans = attachmentBeans_type(self.allegati)
        saveParams.pdfConversion = True
        saveParams.sendEMail = False
        saveDocumentResponse = None

        try:
            saveDocumentResponse = self.service.saveDocument(
                doc, attachmentBeans, saveParams
            )
            if saveDocumentResponse:
                root = ET.fromstring(saveDocumentResponse._value_1)
                num_prot = root[1][0].attrib["num_prot"]
                return num_prot
        except Exception as error:
            print(f"Errore durante la protocollazione: {error}")

    def _get_allegato_dict(self):
        return {"content": None, "description": None, "filename": None}
        # force PDF
        # 'mimeType': "application/pdf"}

    def aggiungi_allegato(self, description, filename):
        self.assure_connection()
        content_type = self.client.get_type("ns1:base64Binary")
        content = content_type(open(filename, "rb").read())
        allegato_dict = self._get_allegato_dict()
        allegato_dict["content"] = content
        allegato_dict["description"] = description
        allegato_dict["filename"] = filename
        self.allegati.append(allegato_dict)

    def fascicolaDocumento(self, fascicolo):
        self.assure_connection()
        response = self.service.addInFolder(fascicolo)
        if response:
            return True
            # root = ET.fromstring(response._value_1)

    def cercaDocumento(self, key, value):
        self.assure_connection()
        query = f"[{key}]={value}"
        try:
            return self.service.search(query, xsd.SkipValue, xsd.SkipValue)
        except Exception as error:
            print(f"Errore lettura dati: {error}")


class Protocollo(WSTitulusClient):
    pass
