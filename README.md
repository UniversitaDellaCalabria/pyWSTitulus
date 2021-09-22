# pyWSTitulus
Protocollazioni e recupero Documenti da Titulus 5 con Python 3.

## Installazione
````
pip install git+https://github.com/UniversitaDellaCalabria/pyWSTitulus
````

## Esempio protocollo
````
from titulus_ws.protocollo import Protocollo
from titulus_ws.settings import *
from titulus_ws.utils import *


num_prot = None
PATH_ALLEGATI = f'{BASE_ROOT}/attachments'
allegati = []

# creazione istanza client
titulus = Protocollo(wsdl_url=PROT_URL_TEST,
                     username=PROT_LOGIN,
                     password=PROT_PASSW)

# START costruzione array allegati del Documento
# documento principale
allegato = {'description':'Documento principale',
            'filename': 'test1.pdf'}
allegati.append(allegato)

# allegato
allegato ={'description':'Allegato 2',
           'filename': 'test2.pdf'}
allegati.append(allegato)

for allegato in allegati:
    titulus.aggiungi_allegato(allegato['description'],
                              f"{PATH_ALLEGATI}/{allegato['filename']}")
# END costruzione array allegati del Documento

# parametri protocollazione del Documento
oggetto = 'Oggetti protocollo di test con oggetto di test'
classificazione = ''
cod_classif = '09/01'
autore = 'pyWSTitulus'
nome_riferimento_interno = 'UTENTE WEBSERVICE'
ufficio_riferimento_interno = 'DIREZIONE GENERALE'
numero_allegati = len(allegati)
nome_riferimento_esterno = 'Francesco Filicetti'
codice_fiscale_riferimento_esterno = 'CODICE_FISCALE'
email_riferimento_esterno = 'francesco.filicetti@unical.it'

doc = format_xml_doc(oggetto=oggetto,
                     classificazione=classificazione,
                     cod_classif=cod_classif,
                     autore=autore,
                     nome_riferimento_interno=nome_riferimento_interno,
                     ufficio_riferimento_interno=ufficio_riferimento_interno,
                     numero_allegati=numero_allegati,
                     nome_riferimento_esterno=nome_riferimento_esterno,
                     codice_fiscale_riferimento_esterno=codice_fiscale_riferimento_esterno,
                     email_riferimento_esterno=email_riferimento_esterno)

# protocollazione
num_prot = titulus.protocolla(doc, allegati)

print(f'Protocollo: {num_prot}')
````

## Esempio fascicolazione
````
# fascicolazione
fascicolo_physdoc = ''
fascicolo_nrecord = ''
fascicolo_numero ='2021-XXXX-09/01.00003'
doc_physdoc = ''
doc_nrecord = ''
doc_num_prot = num_prot
doc_minuta='no' #si/no

fas = format_xml_fascicolo(fascicolo_physdoc,
                           fascicolo_nrecord,
                           fascicolo_numero,
                           doc_physdoc,
                           doc_nrecord,
                           doc_num_prot,
                           doc_minuta)
fascicolazione = titulus.fascicolaDocumento(fas)

print(f'Fascicolazione: {fascicolazione}')
````

## Esempio ricerca documento
````
# cerca documento protocollato
print(f'Ricerca protocollo: {num_prot}')
response = titulus.cercaDocumento("docnumprot", num_prot)
print(response.__dict__['__values__']['_value_1'])
````
