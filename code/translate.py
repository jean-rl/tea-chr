# pip install --upgrade translators 

import translators.server as tss
#str: input text
#out_language and in_languaje: in format en,es,it etc
def Tranlate(str,in_language="auto",out_language="es"):
    out= tss.google(str, in_language, out_language)
    return out

