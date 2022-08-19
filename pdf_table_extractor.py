import camelot


tables = camelot.read_pdf(
    'foo.pdf')

print(tables)

tables.export('.pdf', f='csv', compress=True)
tables[0].to_csv('foo.csv')
