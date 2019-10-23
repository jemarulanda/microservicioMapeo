'''Clase con la lógica implementada, identifica si cumple indicador o no'''
from json import loads
import json

class Transform:
    '''Clase principal'''
    @classmethod
    def toIon(cls, source):      
        data_header = source.get('IMI','')
        data_detail = source.get('ID','')
        new_data =  '<PurchaseOrder>\n'+ \
                    '   <PurchaseOrderHeader>\n'+ \
                    '      <DocumentID>\n'+ \
                    '         <ID accountingEntity="WHSE1">'+data_header.get('eaoid_ordersce','').strip()+'</ID>\n'+ \
                    '      </DocumentID>\n'+ \
                    '      <Note>'+data_header.get('eaoim_comme01','').strip()+data_header.get('eaoim_comme02','').strip()+ \
                        data_header.get('eaoim_comme03','').strip()+data_header.get('eaoim_comme04','').strip()+ \
                        data_header.get('eaoim_comme05','').strip()+'</Note>\n'+ \
                    '      <DocumentDateTime>'+data_header.get('eaoim_dtorder','').strip()+'</DocumentDateTime>\n'+ \
                    '      <ExpectedrReceiptDate>'+data_header.get('eaoim_dtreq','').strip()+'</ExpectedrReceiptDate>\n'+ \
                    '      <Status>\n'+ \
                    '         <Code>Open</Code>\n'+ \
                    '         <ArchiveIndicator>false</ArchiveIndicator>\n'+ \
                    '      </Status>\n'+ \
                    '      <SupplierParty>\n'+ \
                    '         <PartyIDs>\n'+ \
                    '            <ID>'+data_header.get('eaoim_owner','').strip()+'</ID>\n'+ \
                    '         </PartyIDs>\n'+ \
                    '      </SupplierParty>\n'+ \
                    '      <ShipToParty>\n'+ \
                    '         <Location type="Warehouse">\n'+ \
                    '            <ID accountingEntity="">'+data_header.get('eaoim_dummy6401','').strip()+'</ID>\n'+ \
                    '         </Location>\n'+ \
                    '      </ShipToParty>\n'+ \
                    '      <SUSR1>'+data_header.get('eaoim_ordtyp','').strip()+'</SUSR1>\n'+ \
                    '      <SUSR2>'+data_header.get('eaoim_grpcod1','').strip()+'</SUSR2>\n'+ \
                    '      <SUSR3>'+data_header.get('eaoim_grpcod2','').strip()+'</SUSR3>\n'+ \
                    '      <SUSR4>'+data_header.get('eaoim_grpcod3','').strip()+'</SUSR4>\n'+ \
                    '      <TOTALORDERLINES>'+data_header.get('eaoim_totalid','').strip()+'</TOTALORDERLINES>\n'+ \
                    '   </PurchaseOrderHeader>\n'
        for detail in data_detail:
            new_data = new_data + '   <PurchaseOrderLine>\n'+ \
                    '      <LineNumber>'+detail.get('eaoid_lineitm','').strip()+'</LineNumber>\n'+ \
                    '      <Note>'+detail.get('eaoid_comme01','').strip()+detail.get('eaoid_comme02','').strip()+ \
                        detail.get('eaoid_comme03','').strip()+detail.get('eaoid_comme04','').strip()+ \
                        detail.get('eaoid_comme05','').strip()+'</Note>\n'+ \
                    '      <Status>\n'+ \
                    '         <Code>Open</Code>\n'+ \
                    '         <ArchiveIndicator>false</ArchiveIndicator>\n'+ \
                    '      </Status>\n'+ \
                    '      <Item>\n'+ \
                    '         <ItemID>\n'+ \
                    '            <ID accountingEntity="EXITO">'+detail.get('eaoid_part','').strip()+'</ID>\n'+ \
                    '         </ItemID>\n'+ \
                    '         <ServiceIndicator>false</ServiceIndicator>\n'+ \
                    '      </Item>\n'+ \
                    '      <Quantity unitCode="pza">'+detail.get('eaoid_ordqty','').strip()+'</Quantity>\n'+ \
                    '      <BaseUOMQuantity unitCode="pza">'+detail.get('eaoid_ordqty','').strip()+'</BaseUOMQuantity>\n'+ \
                    '      <ShipToParty>\n'+ \
                    '         <Location type="Warehouse">\n'+ \
                    '            <ID accountingEntity="">'+detail.get('eaoid_wareh','').strip()+'</ID>\n'+ \
                    '         </Location>\n'+ \
                    '      </ShipToParty>\n'+ \
                    '      <SUSR1>'+detail.get('eaoid_vuser1','').strip()+'</SUSR1>\n'+ \
                    '      <SUSR2>'+detail.get('eaoid_vuser3','').strip()+'</SUSR2>\n'+ \
                    '      <SUSR3>'+detail.get('eaoid_dummy6403','').strip()+'</SUSR3>\n'+ \
                    '   </PurchaseOrderLine>\n'
                
        new_data = new_data + '</PurchaseOrder>'
       
        return new_data

    @classmethod
    def transformacion(cls, source):
        response = cls.toIon(source)       
        return response

    