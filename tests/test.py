
import spacy
from src.sn_gram.sn_gram import SNGramParser
#from root of project run "python -m tests.test"
spacy.require_gpu()

nlp = spacy.load("en_core_web_sm")

test_string = "The quick brown fox jumped over the large lazy dog"

doc = nlp(test_string)

sn_bow = SNGramParser(doc)

sn_bow.extract_sn_grams()

#form list from iterable
print(list(sn_bow.sn_gram_bow()))

#access sn_bow list directly
print(sn_bow.sn_grams)
