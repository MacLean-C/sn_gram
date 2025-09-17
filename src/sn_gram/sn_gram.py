
class SNGramParser:
    def __init__(self, doc):
        self.doc = doc  
        self.sn_grams = []
        
    def __iter__(self):
        return iter(self.sn_grams)
    
    def sn_gram_bow(self):
         return iter(self.sn_grams)
       
    def extract_sn_grams(self):
            vp_list = self.extract_vp_chunks()
            np_list = self.extract_np_chunks()

            np_processed = [chunk.replace(' ','_').lower() for chunk in np_list]
            vp_processed = [chunk.replace(' ','_').lower() for chunk in vp_list]
            
            bow_sn_grams = vp_processed+np_processed
            self.sn_grams.extend(bow_sn_grams)
            
    def extract_vp_chunks(self):
        doc = self.doc
        vp_chunks = []
        for token in doc:
            if token.pos_ == "VERB":
                # Start a new VP chunk with the verb
                chunk = [token]
                #ensures all verbs are added individually
                vp_chunks.append(" ".join([t.lemma_ for t in chunk]))

                # Add children tokens to the VP chunk
                for child in token.children:
                    #test with other chunk lengths for examining discourse + verbs with multiple complements
                    if child.dep_ in ("aux", "auxpass", "neg", "advmod", "prep", "prt", "dobj", "attr", "prep", "nsubj", "dobj", "pobj") and len(chunk)<=1:
                        chunk.append(child)
                # Sort the chunk tokens by their positions in the sentence
                
                chunk = sorted(chunk, key=lambda x: x.i)
                
                # Join the chunk tokens into a single string
                #lemmatizer here
                #for text replace with .text
                vp_chunks.append(" ".join([t.lemma_ for t in chunk]))
        return vp_chunks


    def extract_np_chunks(self):
        doc = self.doc
        np_chunks = []
        for chunk in doc.noun_chunks:
            root_noun = [chunk.root]
            #ensures all nouns are added individually
            np_chunks.append(" ".join([t.lemma_ for t in root_noun if not t.is_stop]))
            #this skips over all others
            if len(chunk) <=2:
                chunk = list(chunk)
                np_chunks.append(" ".join([t.lemma_ for t in chunk if not t.is_stop]))
            
            else:
                for token in chunk:
                    
                    intermediate = [chunk.root]
                    if token!=chunk.root and token.is_stop == False:
                        
                        intermediate.append(token)
                        intermediate = sorted(intermediate, key=lambda x: x.i)
                        
                        #lemmatizer here 
                        #note : lemma = int, lemma_ = str
                        np_chunks.append(" ".join([t.lemma_ for t in intermediate]))
                    elif token.is_stop == False:
                        np_chunks.append(" ".join([t.lemma_ for t in intermediate]))
        #remove duplicates
        return list(set(np_chunks))

    

