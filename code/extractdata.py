from pdfminer.high_level import extract_text

# Extract text from a pdf.
# nonumber flag remove all number in text: default False
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

    # Separate into paragraphs
    paragraphs = []
    paragraph = ""
    for t in S:
        # Delete white spaces
        t = t.strip()

        # If the line is not empty, add it to the paragraph
        if t == "":
            paragraphs.append(paragraph)
            paragraph = ""
        else:
            paragraph += t + " "

    # Delete paragraphs with less than 25 words
    paragraphs = [p for p in paragraphs if len(p.split()) > 30]

    # Join paragraphs with a new line
    text = "\n".join(paragraphs)

    return text

print(extract_text_from_pdf("../data/nejmoa2007764.pdf"))
