# pip install -r requirements.txt
import os
from default_settings import *
from reader import Files, Folders, PDFfiles, TXTfiles
# from nlp import NLP


def header():
    print("\n##########################################################")
    print("##\t\tCurriculum Vitae Evaluator Tool\t\t##")
    print("##########################################################")

    
def instructions():
    print("\nPlease, follow the instructions below...\n")
    print("\t1. Write job description into job_description.txt file;")
    print("\t2. Import resumes(CVs) pdf files into /cv directory;")    
    print("\t3. Press Enter key to continue or [Crtl + c] to exit.")
    
    
def clear_console():
    os.system("clear")

    
def main():
    running = True
    cv_folder = Folders(DEFAULT_FOLDER)
    job_descr = TXTfiles(DEFAULT_FILE)
    
    # check if necessary file & folder exists otherwise creates
    cv_folder.verify()
    job_descr.verify()  
        
#     clear_console()    
    # prints some text in console
    header()    
    instructions()
        
    while running:
        
        # check if file is empty and requests to fill it
        file_empty = job_descr.is_empty()
        if file_empty:
            input("\nPlease, write job description into job_description.txt file and press enter to continue...") 
            continue
        
        # check if folder is empty and requests to fill it                    
        folder_empty = cv_folder.is_empty()           
        if folder_empty:
            input("\nPlease, import resumes(CVs) pdf files into /cv directory and press enter to continue...") 
            continue
        
        # on enter continues execution
        input("\nPress enter to run...")
        
        # get txt file text as string
        job_descr_context = job_descr.read()
        print(job_descr_context)
        
        # get all cv pdf files and iterate individually
        resumes_list = cv_folder.get_all_pdf_files() 
        for resume_file in resumes_list:
            
            # get pdf file text as string
            resume_context = PDFfiles(DEFAULT_FOLDER + "/" + resume_file).read()
            print("\n ------------------------------------- \n")
            print(resume_context)
            
#             m = SimilarityNLP(job_descr_context, resume_context)
#             score = m.get_fit_score()
#             keywords = m.get_keywords(resume_context)
#             save_results(score, keywords)
      
    
if __name__ == "__main__":
    main()