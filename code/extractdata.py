


## pip install pdfminer.six  package required

from pdfminer.high_level import extract_text

# # Extract text from a pdf.
# # nonumber flag remove all number in texto: default False
def extract_text_from_pdf(path,nonumber=False):
    text = extract_text(path)

    S = text.split("\n")
    new_list = [item.lower() for item in S]
    try:
        idxref = new_list.index("references" or "bibliografy")
    except:
        idxref = len(S)

    S = S[0:idxref]
    if nonumber == True:
        cleantxt = []
        for txt in S:
            nd = ''.join(c if c not in map(str, range(0, 10)) else "" for c in txt)
            cleantxt.append(nd)
        S = cleantxt
    return S


#text=extract_text_from_pdf("remotesensing-13-01082-v2.pdf")



