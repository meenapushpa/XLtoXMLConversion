from lxml import etree
from xml.etree.ElementTree import Element, SubElement, tostring
import xlrd
import json
import ast
import dateutil.parser
import pandas as pd
from xml.dom import minidom

def index_tree():
    global root3,root4,root5,root6,root7,root,tree
    root = etree.Element('ENVELOPE')
    root1 = etree.SubElement(root,'HEADER')
    etree.SubElement(root1, 'TALLYREQUEST').text = 'Import Data'
    etree.SubElement(root1, 'HEADER').text = ''
    root3 = etree.SubElement(root1,'BODY')
    root4 = etree.SubElement(root3,'IMPORTDATA')
    root22= etree.SubElement(root4,'REQUESTDESC')
    root7=etree.SubElement(root22,'REPORTNAME')
    root7.text ='Vouchers'
    root25=etree.SubElement(root22,'STATICVARIABLES')
    root26=etree.SubElement(root25,'SVCURRENTCOMPANY')
    root26.text ='Gayathri Jewellers'
    root25.text = ''
    etree.SubElement(root22, 'REQUESTDESC').text = ''
    root5 = etree.SubElement(root22,'REQUESTDATA')
    root6 = etree.SubElement(root5,'TALLYMESSAGE')
    root6.set("xmlns", "TallyUDF")
    root6.set('isMaster','Yes')
    tree = etree.ElementTree(root)
def unit_values():
    unit1 = etree.SubElement(root6,'UNIT')
    unit1.set('NAME','GMS')
    unit1.set('RESERVEDNAME','')
    root8 = etree.SubElement(unit1,'NAME')
    root8.text ='GMS'
    root8 = etree.SubElement(unit1,'ISUPDATINGTARGETID')
    root8.text ='No'
    root9 = etree.SubElement(unit1,'ASORIGINAL')
    root9.text ='Yes'
    root10 = etree.SubElement(unit1,'ISGSTEXCLUDED')
    root10.text ='No'
    root11 = etree.SubElement(unit1,'ISSIMPLEUNIT')
    root11.text ='Yes'
def stock(arg1,arg2):
    global root12
    root12 = etree.SubElement(root6,'STOCKITEM')
    root12.set('NAME',arg2)
    root12.set('RESERVEDNAME','')
    root13 = etree.SubElement(root12,'GSTAPPLICABLE')
    root13.text='Applicable'
    root14 = etree.SubElement(root12,'GSTTYPEOFSUPPLY')
    root14.text='Goods'
    root15 = etree.SubElement(root12,'GSTDETAILS.LIST')
    root16 = etree.SubElement(root15,'APPLICABLEFROM')
    root16.text=arg1
    root17 = etree.SubElement(root15,'CALCULATIONTYPE')
    root17.text='On Value'
    root18 = etree.SubElement(root15,'TAXABILITY')
    root18.text='Taxable'
    root19 = etree.SubElement(root15,'ISREVERSECHARGEAPPLICABLE')
    root19.text='No'
    root20 = etree.SubElement(root15,'ISNONGSTGOODS')
    root20.text='No'
    root21 = etree.SubElement(root15,'GSTINELIGIBLEITC')
    root21.text='No'
    root22 = etree.SubElement(root15,'STATEWISEDETAILS.LIST')
    root23 = etree.SubElement(root22,'STATENAME')
    root23.text='Any'
    root24 = etree.SubElement(root22,'RATEDETAILS.LIST')
    root25 = etree.SubElement(root24,'GSTRATEDUTYHEAD')
    root25.text='Central Tax'
    root26 = etree.SubElement(root24,'GSTRATEVALUATIONTYPE')
    root26.text='Based on Value'
    root27 = etree.SubElement(root24,'GSTRATE')
    root27.text='0.75'
    root24.text = ''

    state1 = etree.SubElement(root22,'RATEDETAILS.LIST')
    state2 = etree.SubElement(state1,'GSTRATEDUTYHEAD')
    state2.text='State Tax'
    state3 = etree.SubElement(state1,'GSTRATEVALUATIONTYPE')
    state3.text='Based on Value'
    state4 = etree.SubElement(state1,'GSTRATE')
    state4.text='0.75'
    state1.text = ''

    Integrated1 = etree.SubElement(root22,'RATEDETAILS.LIST')
    Integrated2 = etree.SubElement(Integrated1,'GSTRATEDUTYHEAD')
    Integrated2.text='Integrated Tax'
    Integrated3 = etree.SubElement(Integrated1,'GSTRATEVALUATIONTYPE')
    Integrated3.text='Based on Value'
    Integrated4 = etree.SubElement(Integrated1,'GSTRATE')
    Integrated4.text='1.50'
    Integrated1.text = ''

    Cess1 = etree.SubElement(root22,'RATEDETAILS.LIST')
    Cess2 = etree.SubElement(Cess1,'GSTRATEDUTYHEAD')
    Cess2.text='Cess'
    Cess3 = etree.SubElement(Cess1,'GSTRATEVALUATIONTYPE')
    Cess3.text='Based on Value'
    Cess1.text = ''
    root22.text = ''
    root15.text = ''

    audit1 = etree.SubElement(root12,'OLDAUDITENTRYIDS.LIST')
    audit1.set("Type", "Number")
    audit2 = etree.SubElement(audit1,'OLDAUDITENTRYIDS')
    audit2.text='-1'
    audit1.text=''
    base1 = etree.SubElement(root12,'BASEUNITS')
    base1.text='GMS'
    lang(root12,arg2)
    root12.text=''
def godown():
    loc1 = etree.SubElement(root6,'GODOWN')
    loc1.set("NAME", "Main Location")
    loc1.set("RESERVEDNAME", "")
    lang(loc1,'Main Location')
    loc1.text=''
def lang(arg2,arg3):
    lang1 = etree.SubElement(arg2,'LANGUAGENAME.LIST')
    lang2 = etree.SubElement(lang1,'NAME.LIST')
    lang2.set("Type", "String")
    lang3 = etree.SubElement(lang2,'NAME')
    lang3.text=arg3
    lang2.text=''
    lang4 = etree.SubElement(lang1,'LANGUAGEID')
    lang4.text='1033'
    lang1.text=''
def ledger(arg2):
    ledger1 = etree.SubElement(root6,'LEDGER')
    ledger1.set("NAME",arg2)
    ledger1.set("RESERVEDNAME","")
    ledger2 =etree.SubElement(ledger1,'MAILINGNAME.LIST')
    ledger2.set("TYPE","String")
    ledger2 =etree.SubElement(ledger2,'MAILINGNAME')
    ledger2.text=arg2
    ledger2.text=''
    ledger3 =etree.SubElement(ledger1,'OLDAUDITENTRYIDS.LIST')
    ledger3.set("TYPE","Number")
    ledger4 =etree.SubElement(ledger3,'OLDAUDITENTRYIDS')
    ledger4.text='-1'
    ledger3.text=''
    ledger4 =etree.SubElement(ledger1,'PARENT')
    ledger4.text='Sundry Debtors'
    lang(ledger1,arg2)
    ledger1.text=''
    root6.text=''
def ledger_rate(arg1,arg2):
    ledger1 = etree.SubElement(root6,'LEDGER')
    ledger1.set("NAME",arg1)
    ledger1.set("RESERVEDNAME","")
    ledger3 =etree.SubElement(ledger1,'OLDAUDITENTRYIDS.LIST')
    ledger3.set("TYPE","Number")
    ledger4 =etree.SubElement(ledger3,'OLDAUDITENTRYIDS')
    ledger4.text='-1'
    ledger3.text=''
    if arg1 == 'Sales @ 3%':
        ledger4 =etree.SubElement(ledger1,'PARENT')
        ledger4.text='Sales Accounts'
    else:
        ledger4 =etree.SubElement(ledger1,'PARENT')
        ledger4.text='Duties & Taxes'
    ledger5 =etree.SubElement(ledger1,'GSTAPPLICABLE')
    ledger5.text='Applicable'
    ledger6 =etree.SubElement(ledger1,'TAXTYPE')
    ledger6.text='GST'
    if arg1 != 'Sales @ 3%':
        ledger7 =etree.SubElement(ledger1,'GSTDUTYHEAD')
        ledger7.text=arg2
    ledger8 =etree.SubElement(ledger1,'RATEOFTAXCALCULATION')
    ledger8.text='0.75'
    lang(ledger1,arg2)
    ledger1.text=''
def street(arg1):
    global newroot,newroot1
    newroot = etree.SubElement(root5,'TALLYMESSAGE')
    newroot.set("xmlns", "TallyUDF")
    newroot1 = etree.SubElement(newroot,'VOUCHER')
    newroot1.set("REMOTEID", "")
    newroot1.set("VCHKEY", "")
    newroot1.set("VCHTYPE", "Sales")
    newroot1.set("ACTION", "Create")
    newroot1.set("OBJVIEW", "Invoice Voucher View")
    newroot2 = etree.SubElement(newroot1,'ADDRESS.LIST')
    newroot2.set("TYPE", "String")
    newroot3 = etree.SubElement(newroot2,'ADDRESS')
    newroot3.text=arg1
    newroot2.text=''
    newroot4 = etree.SubElement(newroot1,'BASICBUYERADDRESS.LIST')
    newroot4.set("TYPE", "String")
    newroot5 = etree.SubElement(newroot4,'BASICBUYERADDRESS')
    newroot5.text=arg1
    newroot4.text=''
    newroot6 = etree.SubElement(newroot1,'OLDAUDITENTRYIDS.LIST')
    newroot6.set("TYPE", "Number")
    newroot7 = etree.SubElement(newroot6,'OLDAUDITENTRYIDS')
    newroot7.text='-1'
    newroot6.text=''
def excel_values(arg2,arg3,arg5,arg6,arg7,arg8,arg9,arg10):
    newval6 = etree.SubElement(newroot1,'DATE')
    newval6.text=arg2
    newval7 = etree.SubElement(newroot1,'STATENAME')
    newval7.text=arg3
    newroot8 = etree.SubElement(newroot1,'GSTREGISTRATIONTYPE')
    newroot8.text='Consumer'
    newroot9 = etree.SubElement(newroot1,'NARRATION')
    newroot9.text=arg5
    newroot10 = etree.SubElement(newroot1,'COUNTRYOFRESIDENCE')
    newroot10.text=arg6
    newroot11 = etree.SubElement(newroot1,'PARTYNAME')
    newroot11.text=arg7
    newroot12 = etree.SubElement(newroot1,'VOUCHERTYPENAME')
    newroot12.text=arg8
    newroot13 = etree.SubElement(newroot1,'VOUCHERNUMBER')
    newroot13.text=arg9
    newroot14 = etree.SubElement(newroot1,'PARTYLEDGERNAME')
    newroot14.text=arg7
    newroot15 = etree.SubElement(newroot1,'BASICBASEPARTYNAME')
    newroot15.text=arg7
    newroot16 = etree.SubElement(newroot1,'PERSISTEDVIEW')
    newroot16.text=arg10
    newroot17 = etree.SubElement(newroot1,'PLACEOFSUPPLY')
    newroot17.text=arg3
    newroot18 = etree.SubElement(newroot1,'BASICBUYERNAME')
    newroot18.text=arg7
    newroot19 = etree.SubElement(newroot1,'GSTREGISTRATIONTYPE')
    newroot19.text='Consumer'
    newroot20 = etree.SubElement(newroot1,'BASICDATETIMEOFREMOVAL')
    newroot20.text=arg2
    newroot21 = etree.SubElement(newroot1,'CONSIGNEESTATENAME')
    newroot21.text=arg3
    newroot22 = etree.SubElement(newroot1,'DIFFACTUALQTY')
    newroot22.text='No'
def other_values(arg1):
    value2 = etree.SubElement(newroot1,'ISMSTFROMSYNC')
    value2.text='No'
    value3 = etree.SubElement(newroot1,'ASORIGINAL')
    value3.text='No'
    value4 = etree.SubElement(newroot1,'AUDITED')
    value4.text='No'
    value5 = etree.SubElement(newroot1,'FORJOBCOSTING')
    value5.text='No'
    value6 = etree.SubElement(newroot1,'ISOPTIONAL')
    value6.text='No'
    value7 = etree.SubElement(newroot1,'EFFECTIVEDATE')
    value7.text=arg1
    value8 = etree.SubElement(newroot1,'USEFOREXCISE')
    value8.text='No'
    value9 = etree.SubElement(newroot1,'ISFORJOBWORKIN')
    value9.text='No'
    value10 = etree.SubElement(newroot1,'ALLOWCONSUMPTION')
    value10.text='No'
    value11 = etree.SubElement(newroot1,'USEFORINTEREST')
    value11.text='No'
    value12 = etree.SubElement(newroot1,'USEFORGAINLOSS')
    value12.text='No'
    value13 = etree.SubElement(newroot1,'USEFORGODOWNTRANSFER')
    value13.text='No'
    value14 = etree.SubElement(newroot1,'USEFORCOMPOUND')
    value14.text='No'
    value15 = etree.SubElement(newroot1,'USEFORSERVICETAX')
    value15.text='No'
    value16 = etree.SubElement(newroot1,'ISEXCISEVOUCHER')
    value16.text='No'
    value17 = etree.SubElement(newroot1,'EXCISETAXOVERRIDE')
    value17.text='No'
    value18 = etree.SubElement(newroot1,'USEFORTAXUNITTRANSFER')
    value18.text='No'
    value19 = etree.SubElement(newroot1,'EXCISEOPENING')
    value19.text='No'
    value20 = etree.SubElement(newroot1,'USEFORFINALPRODUCTION')
    value20.text='No'
    value21 = etree.SubElement(newroot1,'ISTDSOVERRIDDEN')
    value21.text='No'
    value22 = etree.SubElement(newroot1,'ISTCSOVERRIDDEN')
    value22.text='No'
    value23 = etree.SubElement(newroot1,'ISTDSTCSCASHVCH')
    value23.text='No'
    value24 = etree.SubElement(newroot1,'INCLUDEADVPYMTVCH')
    value24.text='No'
    value25 = etree.SubElement(newroot1,'ISSUBWORKSCONTRACT')
    value25.text='No'
    value26 = etree.SubElement(newroot1,'ISVATOVERRIDDEN')
    value26.text='No'
    value27 = etree.SubElement(newroot1,'IGNOREORIGVCHDATE')
    value27.text='No'
    value28 = etree.SubElement(newroot1,'ISSERVICETAXOVERRIDDEN')
    value28.text='No'
    value29 = etree.SubElement(newroot1,'ISISDVOUCHER')
    value29.text='No'
    value30 = etree.SubElement(newroot1,'ISEXCISEOVERRIDDEN')
    value30.text='No'
    value31 = etree.SubElement(newroot1,'ISEXCISESUPPLYVCH')
    value31.text='No'
    value32 = etree.SubElement(newroot1,'ISGSTOVERRIDDEN')
    value32.text='No'
    value33 = etree.SubElement(newroot1,'GSTNOTEXPORTED')
    value33.text='No'
    value34 = etree.SubElement(newroot1,'ISVATPRINCIPALACCOUNT')
    value34.text='No'
    value35 = etree.SubElement(newroot1,'ISSHIPPINGWITHINSTATE')
    value35.text='No'
    value36 = etree.SubElement(newroot1,'ISCANCELLED')
    value36.text='No'
def sub_other():
    a1 = etree.SubElement(newroot1,'HASCASHFLOW')
    a1.text='No'
    a2 = etree.SubElement(newroot1,'ISPOSTDATED')
    a2.text='No'
    a3 = etree.SubElement(newroot1,'USETRACKINGNUMBER')
    a3.text='No'
    a4 = etree.SubElement(newroot1,'ISINVOICE')
    a4.text='Yes'
    a5 = etree.SubElement(newroot1,'MFGJOURNAL')
    a5.text='No'
    a6 = etree.SubElement(newroot1,'HASDISCOUNTS')
    a6.text='No'
    a7 = etree.SubElement(newroot1,'ASPAYSLIP')
    a7.text='No'
    a8 = etree.SubElement(newroot1,'ISCOSTCENTRE')
    a8.text='Yes'
    a9 = etree.SubElement(newroot1,'ISSTXNONREALIZEDVCH')
    a9.text='No'
    a10 = etree.SubElement(newroot1,'ISEXCISEMANUFACTURERON')
    a10.text='No'
    a11 = etree.SubElement(newroot1,'ISBLANKCHEQUE')
    a11.text='No'
    a12 = etree.SubElement(newroot1,'ISVOID')
    a12.text='No'
    a13 = etree.SubElement(newroot1,'ISONHOLD')
    a13.text='No'
    a14 = etree.SubElement(newroot1,'ORDERLINESTATUS')
    a14.text='No'
    a15 = etree.SubElement(newroot1,'VATISAGNSTCANCSALES')
    a15.text='No'
    a16 = etree.SubElement(newroot1,'VATISPURCEXEMPTED')
    a16.text='No'
    a17 = etree.SubElement(newroot1,'ISVATRESTAXINVOICE')
    a17.text='No'
    a18 = etree.SubElement(newroot1,'VATISASSESABLECALCVCH')
    a18.text='Yes'
    a19 = etree.SubElement(newroot1,'ISVATDUTYPAID')
    a19.text='Yes'
    a20 = etree.SubElement(newroot1,'ISDELIVERYSAMEASCONSIGNEE')
    a20.text='No'
    a21 = etree.SubElement(newroot1,'ISDISPATCHSAMEASCONSIGNOR')
    a21.text='No'
    a22 = etree.SubElement(newroot1,'ISDELETED')
    a22.text='No'
    a23 = etree.SubElement(newroot1,'CHANGEVCHMODE')
    a23.text='No'
def ledger_other(arg3):
    global b1
    b1 = etree.SubElement(newroot1,'LEDGERENTRIES.LIST')
    b1.set("Type",arg3)
    b2 = etree.SubElement(b1,'OLDAUDITENTRYIDS.LIST')
    b2.set("Type","Number")
    b3 = etree.SubElement(b2,'OLDAUDITENTRYIDS')
    b3.text='-1'
    b2.text=''
def ledger_voucher(arg1,arg2):
    b4 = etree.SubElement(b1,'LEDGERNAME')
    b4.text=arg1
    b5 = etree.SubElement(b1,'ISDEEMEDPOSITIVE')
    b5.text='Yes'
    b6 = etree.SubElement(b1,'LEDGERFROMITEM')
    b6.text='No'
    b7 = etree.SubElement(b1,'REMOVEZEROENTRIES')
    b7.text='No'
    b8 = etree.SubElement(b1,'ISPARTYLEDGER')
    b8.text='Yes'
    b9 = etree.SubElement(b1,'ISLASTDEEMEDPOSITIVE')
    b9.text='Yes'
    b10 = etree.SubElement(b1,'AMOUNT')
    b10.text=arg2
def ledger_invoice():
    in2 = etree.SubElement(b1,'BASICRATEOFINVOICETAX.LIST')
    in2.set("Type","Number")
    in3 = etree.SubElement(in2,'BASICRATEOFINVOICETAX')
    in3.text='1.5'
    in2.text=''
def ledger_gst(arg1,arg2,arg3,arg4):
    ledger_other(arg3)
    ledger_invoice()
    ledger_voucher(arg1,arg2)
    rate_gst(arg4)
def rate_gst(arg4):
    b10 = etree.SubElement(b1,'VATEXPAMOUNT')
    b10.text=arg4
    c1 = etree.SubElement(b1,'RATEDETAILS.LIST')
    c2 = etree.SubElement(c1,'GSTRATEDUTYHEAD')
    c2.text='Central Tax'
    c3 = etree.SubElement(c1,'GSTRATEVALUATIONTYPE')
    c3.text='Based on Value'
    c1.text=''
    s1 = etree.SubElement(b1,'RATEDETAILS.LIST')
    s2 = etree.SubElement(s1,'GSTRATEDUTYHEAD')
    s2.text='State Tax'
    s3 = etree.SubElement(s1,'GSTRATEVALUATIONTYPE')
    s3.text='Based on Value'
    s1.text=''
    I1 = etree.SubElement(b1,'RATEDETAILS.LIST')
    I2 = etree.SubElement(I1,'GSTRATEDUTYHEAD')
    I2.text='Integrated Tax'
    I3 = etree.SubElement(I1,'GSTRATEVALUATIONTYPE')
    I3.text='Based on Value'
    I1.text=''
    cc1 = etree.SubElement(b1,'RATEDETAILS.LIST')
    cc2 = etree.SubElement(cc1,'GSTRATEDUTYHEAD')
    cc2.text='Cess'
    cc3 = etree.SubElement(cc1,'GSTRATEVALUATIONTYPE')
    cc3.text='Based on Value'
    cc1.text=''
    b1.text=''
def description(arg1,arg2,arg3,arg4,arg5):
    global d1
    d1 = etree.SubElement(newroot1,'ALLINVENTORYENTRIES.LIST')
    d2 = etree.SubElement(d1,'BASICUSERDESCRIPTION.LIST')
    d2.set("Type","String")
    d3 = etree.SubElement(d2,'BASICUSERDESCRIPTION')
    d3.text=arg1
    d2.text=''
    d4 = etree.SubElement(d1,'STOCKITEMNAME')
    d4.text='Gold Ornaments'
    d5 = etree.SubElement(d1,'ISDEEMEDPOSITIVE')
    d5.text='No'
    d6 = etree.SubElement(d1,'ISLASTDEEMEDPOSITIVE')
    d6.text='No'
    d7 = etree.SubElement(d1,'ISAUTONEGATE')
    d7.text='No'
    d8 = etree.SubElement(d1,'ISCUSTOMSCLEARANCE')
    d8.text='No'
    d9 = etree.SubElement(d1,'ISTRACKCOMPONENT')
    d9.text='No'
    d10 = etree.SubElement(d1,'ISTRACKPRODUCTION')
    d10.text='No'
    d11 = etree.SubElement(d1,'ISPRIMARYITEM')
    d11.text='No'
    d12 = etree.SubElement(d1,'ISSCRAP')
    d12.text='No'
    d13 = etree.SubElement(d1,'RATE')
    d13.text=arg2
    d14 = etree.SubElement(d1,'AMOUNT')
    d14.text=arg3
    d15 = etree.SubElement(d1,'VATASSBLVALUE')
    d15.text=arg4
    d16 = etree.SubElement(d1,'ACTUALQTY')
    d16.text=arg5
    d17 = etree.SubElement(d1,'BILLEDQTY')
    d17.text=arg5
def batch_list(arg1,arg2):
    ba1 = etree.SubElement(d1,'BATCHALLOCATIONS.LIST')
    ba2 = etree.SubElement(ba1,'GODOWNNAME')
    ba2.text='Main location'
    ba3 = etree.SubElement(ba1,'DESTINATIONGODOWNNAME')
    ba3.text='Main location'
    ba4 = etree.SubElement(ba1,'DYNAMICCSTISCLEARED')
    ba4.text='No'
    ba5 = etree.SubElement(ba1,'AMOUNT')
    ba5.text=arg1
    ba6 = etree.SubElement(ba1,'ACTUALQTY')
    ba6.text=arg2
    ba7 = etree.SubElement(ba1,'BILLEDQTY')
    ba7.text=arg2
    ba1.text=''
def account_list(arg1,arg2):
    aa1 = etree.SubElement(d1,'ACCOUNTINGALLOCATIONS.LIST')
    aa2 = etree.SubElement(aa1,'OLDAUDITENTRYIDS.LIST')
    aa2.set("Type","Number")
    aa3 = etree.SubElement(aa2,'OLDAUDITENTRYIDS')
    aa3.text='-1'
    aa2.text=''
    aa4 = etree.SubElement(aa1,'LEDGERNAME')
    aa4.text=arg1
    aa5 = etree.SubElement(aa1,'ISDEEMEDPOSITIVE')
    aa5.text='No'
    aa6 = etree.SubElement(aa1,'LEDGERFROMITEM')
    aa6.text='No'
    aa7 = etree.SubElement(aa1,'REMOVEZEROENTRIES')
    aa7.text='No'
    aa8 = etree.SubElement(aa1,'ISPARTYLEDGER')
    aa8.text='No'
    aa9 = etree.SubElement(aa1,'ISLASTDEEMEDPOSITIVE')
    aa9.text='No'
    aa10 = etree.SubElement(aa1,'AMOUNT')
    aa10.text=arg2
    aa1.text=''
    d1.text=''
    newroot1.text=''
    newroot.text=''
def prettify(xmlStr):
    INDENT = "  "
    rough_string = etree.tostring(xmlStr)
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent=INDENT)
def fileoperations():
    excel=pd.read_excel('Test\\TallySales.xlsx')
    jsonobj = excel.to_json('Outputlist.json', orient='records',date_format='iso')
    with open('Outputlist.json', 'r', encoding='utf-8') as infile:
        data=infile.read()
        data=data.replace("null", '" "')
        dictdata = ast.literal_eval(data)
        customernamelist,newlist,invoicelist=[],[],[]
        for item in dictdata:
            newlist.append(item)
        for index in range(len(dictdata)):
            for item,value in dictdata[index].items():
                if item == 'Customer Name':
                    individuallist=value
                    customernamelist.append(individuallist)
                if item == 'Invoice No':
                    inlist=value
                    invoicelist.append(inlist)
    return customernamelist,newlist,invoicelist

def main():
    global tree
    customernamelist,newlist,invoicelist=fileoperations()
    index_tree()
    unit_values()
    stock('20170701','Gold Ornaments')
    stock('20170701','Silver Ornaments')
    godown()
    uniqueinvoicelist=[]
    for i in invoicelist:
        if i not in uniqueinvoicelist:
            uniqueinvoicelist.append(i)

    uniquenamelist=[]
    for i in customernamelist:
        if i not in uniquenamelist:
            uniquenamelist.append(i)
    for j in uniquenamelist:
        ledger(j)
    ledger_rate('CGST','Central Tax')
    ledger_rate('SGST','State Tax')
    ledger_rate('Sales @ 3%',None)
    for values in newlist:
        #for k in uniqueinvoicelist:
        strdate = dateutil.parser.parse(values['Invoice Date'])
        newdate=strdate.strftime("%Y%m%d")
        street(values['Address 1'])
        excel_values(newdate,values['State'],values['Narration'],values['Country'],values['Customer Name'],'Sales',values['Invoice No'],'Invoice Voucher View')
        other_values(newdate)
        sub_other()
        ledger_other('Ledger_Party')
        stramount=str(values['Amount'])
        strcgstamount=str(values['CGST Amount'])
        strsgstamount=str(values['SGST Amount'])
        strroundamount=str(values['Round off Amount'])
        otherchargesamount=str(values['Other Charges_1 Amount'])
        strqty=str(values['QTY']) + (values['UOM'])
        strrate=str(values['Rate']) + '/' + (values['UOM'])
        ledger_voucher(values['Customer Name'],stramount)
        b1.text=''
        if values['Other Charges_1 Amount'] != 0 :
            ledger_other('Ledger_Other1')
            ledger_voucher(values['Other Charges_1 Ledger'],otherchargesamount)
            rate_gst(otherchargesamount)
        ledger_gst('CGST',strcgstamount,'Ledger_CGST',strcgstamount)
        ledger_gst('SGST',strsgstamount,'Ledger_SGST',strsgstamount)
        ledger_other('Ledger_Round')
        ledger_voucher(values['Round off Ledger'],strroundamount)
        rate_gst(strroundamount)
        description(values['Item Description'],strrate,stramount,stramount,strqty)
        batch_list(stramount,strqty)
        account_list(values['Sales Ledger'],stramount)
    root5.text=''
    root4.text=''
    root3.text=''
    #etree.tostring(root, method="c14n")
    #tree = etree.ElementTree(root)
    tree.write("filename3.xml", encoding="utf-8", pretty_print=True, xml_declaration = None)
    prettified_xmlStr = prettify(tree)
    output_file = open("filename3.xml", "w")
    output_file.write(prettified_xmlStr)
    output_file.close()

if __name__ == "__main__":
    main()
