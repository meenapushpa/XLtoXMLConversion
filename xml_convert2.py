import pandas as pd
import xlrd
import xlsxwriter

pop = pd.read_excel(r'Test//TallySalestest.xlsx',delimiter=r"\s+", names=['Invoice Date','Invoice No','Voucher Type','Bill Ref No'])
def func(row):
    xml = ['<item>']
    for field in row.index:
        xml.append('  <field name="{0}">{1}</field>'.format(field, row[field]))
    xml.append('</item>')
    return '\n'.join(xml)
with open('outputsales.xml','w') as f:
    f.write('\n'.join(pop.apply(func, axis=1)))
