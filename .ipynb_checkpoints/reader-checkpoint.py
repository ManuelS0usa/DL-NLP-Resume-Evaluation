import os
import PyPDF2


class Folders():
    """ class to handle folders """
    
    def __init__(self, folderName):
        self.folderName = folderName
    
    def verify(self):
        """ Creating a Directory if It Doesn't Exist """
        if not os.path.exists(self.folderName):
            os.mkdir(self.folderName)  
            
    def is_empty(self):        
        if len(os.listdir(self.folderName)) == 0:
            folder_empty_flag = True
        else:
            folder_empty_flag = False
        return folder_empty_flag   
    
    def get_all_files(self):
        return os.listdir(self.folderName)
            
    def get_all_pdf_files(self):
        list = self.get_all_files()
        for file in list:
            if not file.endswith(".pdf"):
                list.remove(file)        
        return list
    
    def remove_file(self, filename):
        os.remove(filename)
        
    def remove_all_files(self):
        list = self.get_all_files()
        for f in list:
            if f.endswith(".pdf"):
                self.remove_file(self.folderName + "/" + f)
            
        
class Files():
    """ class to handle files """
    
    def __init__(self, fileName):
        self.fileName = fileName
        
    def verify(self):
        """ Creating file if It Doesn't Exist """
        if not os.path.exists(self.fileName):
            open(self.fileName, 'w')  
            
    def is_empty(self):
        """ checking if size of file is 0 """
        if os.path.getsize(self.fileName) == 0: 
            file_empty_flag = True
        else:
            file_empty_flag = False
        return file_empty_flag
    
    
class TXTfiles(Files):
    """ child class to handle .txt files """
    
    def __init__(self, fileName):
        super().__init__(fileName)
    
    def read(self):
        with open(self.fileName, 'r') as f:
            lines = f.readlines()  # .replace('\n', '')
            context = ' '.join(lines)
        return context

    
class PDFfiles(Files):
    """ child class to handle .pdf files """

    def __init__(self, fileName):
        super().__init__(fileName)
    
    def read(self):
        pdfFileObj = open(self.fileName, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        pageObj = pdfReader.getPage(0)
        context = pageObj.extractText()
        return context

            