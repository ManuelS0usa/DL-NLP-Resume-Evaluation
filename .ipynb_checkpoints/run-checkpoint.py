import shutil, os
from default_settings import *
from src.reader import Files, Folders, PDFfiles, TXTfiles
from src.nlp import NLP


def header():
    print("\n##########################################################")
    print("##\t\tCurriculum Vitae Evaluator Tool\t\t##")
    print("##########################################################")

    
def instructions():
    print("\nPlease, follow the instructions below...\n")
    print("\t1. Write job description into job_description.txt file;")
    print("\t2. Import resumes(CVs) pdf files into /cv directory;")    
    print("\t3. Press Enter key to continue or [q] key to exit.")
    
    
def clear_console():
    os.system("clear")

    
def main():
    running = True
    cv_folder = Folders(DEFAULT_FOLDER)
    results_folder = Folders(DEFAULT_RESULTS)
    job_descr = TXTfiles(DEFAULT_FILE)
    
    # check if necessary file & folders exist otherwise create
    cv_folder.verify()
    job_descr.verify()  
    results_folder.verify()    
        
#     clear_console()    
    # prints some text in console
    header()    
    instructions()
        
    while running:
        
        # check if file is empty and request to fill it
        file_empty = job_descr.is_empty()
        if file_empty:
            l = input("\nPlease, write job description into job_description.txt file and press enter to continue...") 
            if l == 'q' or l == 'Q':
                break
            else:
                continue
        
        # check if folder is empty and request to fill it                    
        folder_empty = cv_folder.is_empty()           
        if folder_empty:
            l2 = input("\nPlease, import resumes(CVs) pdf files into /cv directory and press enter to continue...") 
            if l2 == 'q' or l == 'Q':
                break
            else:
                continue
        
        # on key pressed continues execution
        inp = input("\nPress enter to run...")
        if inp == 'q' or inp == 'Q':
            break
        
        # get txt file text as string
        job_descr_context = job_descr.read()
        
        results = []
        # get all cv pdf files and iterate individually
        resumes_list = cv_folder.get_all_pdf_files() 
        for resume_file in resumes_list:          
            # get pdf file text as string
            resume_context = PDFfiles(DEFAULT_FOLDER + "/" + resume_file).read()
            
            # apply nlp model and get resulting score
            m = NLP(job_descr_context, resume_context)
            score = m.get_fit_score()
            # apply keyword tool to get keywords from cv            
            keywords = m.get_keywords(resume_context)
            
            # store results 
            results.append({'filename': resume_file, 'score': score, 'keywords': keywords})
                
        # sort list according to best to worst score
        results.sort(key=lambda item: item.get("score"), reverse=True)        
        best_results = results[:DEFAULT_SCORE]
#         print(best_results)
        
        # clear results folder
        results_folder.remove_all_files()        
        # copy best resumes to results folder
        for res in best_results:
            shutil.copyfile(DEFAULT_FOLDER + "/" + res['filename'], DEFAULT_RESULTS + "/" + res['filename'])    
         
        print("\nExecution completed. The " + str(DEFAULT_SCORE) + " best matching CVs are available in /results directory.\n\n")      
        break
    
    
if __name__ == "__main__":
    main()
