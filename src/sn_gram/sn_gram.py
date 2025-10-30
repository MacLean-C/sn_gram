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
        
        seen = set()
        vp_chunks_final = []
        for sn_gram in vp_chunks:
            if sn_gram not in seen:
                seen.add(sn_gram)
                vp_chunks_final.append(sn_gram)
        
        
        
        return vp_chunks_final


    def extract_np_chunks(self):
        doc = self.doc
        np_chunks = []
        for chunk in doc.noun_chunks:
            root_noun = [chunk.root]
            np_chunks.append(" ".join([t.lemma_ for t in root_noun if not t.is_stop]))
            
            #this skips over all others
            if len(chunk) <=2:
                chunk = list(chunk)
                np_chunks.append(" ".join([t.lemma_ for t in chunk if not t.is_stop]))
            
            else:
                #addition of full_phrase variable in order to get entire noun phrase
                #before we only extracted noun + complement 1, noun + comp 2, etc
                #now we can get noun + comp 1, comp 2, comp ... in the case of words
                #such as renewable energy goals or greenhouse gas emissions
                full_phrase = [chunk.root]
                for token in chunk:
                    intermediate = [chunk.root]
                    
                    if token!=chunk.root and token.is_stop == False:
                        
                        intermediate.append(token)
                        intermediate = sorted(intermediate, key=lambda x: x.i)
                        
                        full_phrase.append(token)
                        full_phrase = sorted(full_phrase, key=lambda x: x.i)
                        
                        #lemmatizer here 
                        #note : lemma = int, lemma_ = str
                        np_chunks.append(" ".join([t.lemma_ for t in intermediate]))
                        np_chunks.append(" ".join([t.lemma_ for t in full_phrase]))
                    elif token.is_stop == False:
                        np_chunks.append(" ".join([t.lemma_ for t in intermediate]))
                        
                        np_chunks.append(" ".join([t.lemma_ for t in full_phrase]))
        
        seen = set()
        np_chunks_final = []
        for sn_gram in np_chunks:
            if sn_gram not in seen:
                seen.add(sn_gram)
                np_chunks_final.append(sn_gram)
        
        
        return np_chunks_final