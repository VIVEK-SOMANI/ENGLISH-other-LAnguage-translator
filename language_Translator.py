'''
My projects are available in the given link:
https://drive.google.com/drive/folders/1DBdPv-WAyHpYsv4AvVGUROOcA2qZn57H?usp=sharing
'''

# Language Translation (English - any language)

from googletrans import Translator , LANGUAGES

def translate_lang(text,lang):
## traslation of the given text
     try:
        for item in lang:
             print("Translation in Language Number {}".format(item))
             trans=Translator().translate(text, dest = language_dict[item])
             print (trans.text)
             print("")     
     except:
        print("Language index was not correct{} \n{}".format(lang,text))
            
def display_languages():
    lang_indexes={}
    i=0
    for Language in LANGUAGES.keys():
        lang_indexes[str(i)]=Language
        print("{:<3} : {:<10}".format(str(i),LANGUAGES[Language]))
        i+=1
    print("")
    return lang_indexes
 
     
def index_lang():
## taking the input for the language no.
    lang_index=input("Write language index seperated by space for ex: 10 2 6 5...\n").strip().split(" ")
    return lang_index

def inputt():
     print("WRITE :q or exit() to finish writing")
     text=""
     while(True):
         z=input()
         if(z==":q" or z=="exit()" or z==":Q" or z=="EXIT()"):
             break
         if(z[-1] in ('.,!?:;')):
              text= text+z+'\n'
         else:
              text = text+z+'.\n'
     return text
          
          

if __name__=="__main__":
        language_dict=display_languages()
        sample_text=inputt()
        language_no=index_lang()
        translate_lang(sample_text,language_no)
