from titulus_ws.settings import *


def format_xml_doc(oggetto,
                   classificazione,
                   cod_classif,
                   autore,
                   nome_riferimento_interno,
                   ufficio_riferimento_interno,
                   numero_allegati,
                   tipo="arrivo",
                   cod_amm_aoo="", # può essere vuoto se unica AOO
                   xml_doc=DOCUMENTO_ENTRATA_PATH,
                   nome_riferimento_esterno="",
                   codice_fiscale_riferimento_esterno="",
                   email_riferimento_esterno=""):

    xml = open(xml_doc, "r").read()
    xml = xml.format(tipo=tipo,
                     cod_amm_aoo=cod_amm_aoo,
                     autore=autore,
                     oggetto=oggetto,  #almeno 20 caratteri
                     classif=classificazione,
                     cod_classif=cod_classif,
                     nome_rif_interno=nome_riferimento_interno, # PER FASCICOLARE è NECESSARIA CONCORDANZA CON RESP FASCICOLO
                     ufficio_rif_interno=ufficio_riferimento_interno,
                     allegato=numero_allegati, # stringa: '0 - nessun allegato'
                     nome_rif_esterno=nome_riferimento_esterno,
                     codice_fiscale_rif_esterno=codice_fiscale_riferimento_esterno,
                     email_rif_esterno=email_riferimento_esterno,
                     fax_rif_esterno="",
                     tel_rif_esterno="",
                     indirizzo="",
                     cod_nome_rif_esterno=codice_fiscale_riferimento_esterno)
    return xml


def format_xml_fascicolo(fascicolo_physdoc,
                         fascicolo_nrecord,
                         fascicolo_numero,
                         doc_physdoc,
                         doc_nrecord,
                         doc_num_prot,
                         doc_minuta):

    fasc = open(FASCICOLO_PATH, "r").read()
    fasc = fasc.format(fascicolo_physdoc=fascicolo_physdoc,
                       fascicolo_nrecord=fascicolo_nrecord,
                       fascicolo_numero=fascicolo_numero,
                       doc_physdoc=doc_physdoc,
                       doc_nrecord=doc_nrecord,
                       doc_num_prot=doc_num_prot,
                       doc_minuta=doc_minuta)
    return fasc
