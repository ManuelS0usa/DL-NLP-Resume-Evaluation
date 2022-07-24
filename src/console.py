import os
from default_settings import *

        
def clear_console():
    os.system("clear")


class _Print():
    """ Some larger prints to show on console """
    
    def header(self):
        print("\n##########################################################")
        print("##\t\tCurriculum Vitae Evaluator Tool\t\t##")
        print("##########################################################")
    
    def instructions(self):
        print("\nPlease, follow the instructions below...\n")
        print("\t1. Write job description into job_description.txt file;")
        print("\t2. Import resumes(CVs) pdf files into /" + DEFAULT_FOLDER + " directory;")    
        print("\t3. Press Enter key to continue or [q] key to exit.")
            
    def results(self, n_resume, image_name, score, keywords):    
        print("\n\n RESUME #" + str(n_resume))
        print("\nFILE NAME:", image_name)
        print("SCORE:", score)
        print("KEYWORDS:", keywords)