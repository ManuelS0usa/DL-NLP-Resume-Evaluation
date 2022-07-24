# !pip install langdetect transformers pipeline

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
# from transformers import MBartForConditionalGeneration, MBart50TokenizerFast
from langdetect import detect
# import torch

class Language():
    def __init__(self, text):
        self.text = text
    
    def detect(self):
        lang = detect(self.text)
        return lang
    
    def language_detected(self, language):
        models = {
            'pt': "unicamp-dl/translation-en-pt-t5",
            'es': 'Helsinki-NLP/opus-mt-es-en',
            'de': 'um modelo',
            'fr': 'um modelo',
            'it': 'um modelo'            
        }
        return models[language]
    
    def translate_to_en(self):
        lang = self.detect()           
        lang_model = self.language_detected(lang)
        
        tokenizer = AutoTokenizer.from_pretrained(lang_model)
        model = AutoModelForSeq2SeqLM.from_pretrained(lang_model)
                
        pten_pipeline = pipeline('translation_pt_to_en', model=model, tokenizer=tokenizer)
        output = pten_pipeline(self.text)
        return output    