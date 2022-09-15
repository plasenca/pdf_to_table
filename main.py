import tabula

df = tabula.read_pdf("table.pdf",pages="all")[0]

tabula.convert_into("table.pdf", "data.csv", output_format="csv", pages='all')
print(df)

