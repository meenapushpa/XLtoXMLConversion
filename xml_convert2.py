import pandas as pd
import xlrd
import xlsxwriter

pop = pd.read_excel(r'Test//TallySales.xlsx',delimiter=r"\s+", names=['INVOICEDATE','INVOICENO','VOUCHERTYPE','CUSTOMERNAME','ITEMNAME','ITEMDESCRIPTION','TAXRATE','QTY','UOM','RATE','ADDRESS1','STATE','PLACEOFSUPPLY','COUNTRY','GSTRegistrationType','Amount','SalesLedger','Other Charges_1 Ledger','Other Charges_1 Amount','CGST_LEDGER','CGST_AMOUNT','SGST_LEDGER','SGST_AMOUNT','ROUNDOFF_LEDGER','ROUNDOFF_AMOUNT','GODOWN','NARRATION'])
def func(row):
    xml = ['<BODY>']
    for field in row.index:
        xml.append('  <{0}>{1}</{0}>'.format(field, row[field]))
    xml.append('</BODY>')
    return '\n'.join(xml)
with open('outputsales.xml','w') as f:
    f.write('\n'.join(pop.apply(func, axis=1)))
