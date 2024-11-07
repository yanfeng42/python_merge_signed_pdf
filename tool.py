import pymupdf

doc = pymupdf.open("./tmp_files/ori.pdf")
doc.delete_page(-1)

signed_page = pymupdf.open("./tmp_files/signed_page.pdf")
doc.insert_pdf(signed_page) 

doc.save("./tmp_files/out.pdf")
