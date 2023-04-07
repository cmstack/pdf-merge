from PyPDF2 import PdfMerger

#Create an instance of PdfFileMerger() class
merger = PdfMerger()

#Create a list with the file paths
pdf_files = ['pdf_files/1.pdf', 
             'pdf_files/2.pdf'
             ]

#Iterate over the list of the file paths
for pdf_file in pdf_files:
    #Append PDF files
    merger.append(pdf_file)

#Write out the merged PDF file
merger.write("merged_pages.pdf")
merger.close()
