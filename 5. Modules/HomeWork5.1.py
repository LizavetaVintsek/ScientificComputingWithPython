import os
find_pdf_size = os.path.getsize('//HW5/ikea.pdf')
print("File size is {} bytes.".format(find_pdf_size))
#var1teacher
def find_pdf_size (top):
    import os
    size = 0
    for root, dirs, files in os.walk(top):
        for name in files:
            if name.endswith(".pdf"):
                fullpath = os.path.join(root, name)
                size = size + os.path.getsize(fullpath)
    return size
print ("Files size is {} bytes.".format(find_pdf_size(".")))

