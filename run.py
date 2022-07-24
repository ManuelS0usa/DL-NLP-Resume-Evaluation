import shutil, os
from default_settings import *
from src.reader import Files, Folders, PDFfiles, TXTfiles
from src.nlp import NLP
from src.cv import Image
from src.console import _Print, clear_console

    
def main():
    _print = _Print()
    running = True
    cv_folder = Folders(DEFAULT_FOLDER)
    results_folder = Folders(DEFAULT_RESULTS)
    job_descr = TXTfiles(DEFAULT_FILE)
    opencv_folder = Folders(DEFAULT_OPENCV_FOLDER)
    
    # check if necessary file & folders exist otherwise create
    cv_folder.verify()
    job_descr.verify()  
    results_folder.verify()    
    opencv_folder.verify()
       
#     _print.clear_console()    
    # prints some text in console
    _print.header()    
    _print.instructions()
        
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
            if l2 == 'q' or l2 == 'Q':
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
        
        # clear folders
        results_folder.remove_all_files() 
        opencv_folder.remove_all_files() 
             
        # copy best resumes to results folder, print results and detect candidates face on CV
        print("\n## RESULTS ##")    
        i = 1       
        for res in best_results:
            
            # Copy best resumes to /results folder
            shutil.copyfile(DEFAULT_FOLDER + "/" + res['filename'], DEFAULT_RESULTS + "/" + res['filename'])              
            
            imageName = res['filename'].replace(".pdf", "") + ".jpg"            
            # PDF crop photo image
            PDFfiles(DEFAULT_FOLDER + "/" + res['filename']).save_photo_image(imageName)            
            # Face detect and save    
            Image(imageName).detect()
            
            # Show results on console
            _print.results(i, res['filename'], res['score'], res['keywords'])            
            i+=1       
            
        print("\nExecution completed. The " + str(DEFAULT_SCORE) + " best matching CVs are available in /results directory.\n\n")      
        break
    
    
if __name__ == "__main__":
    main()
