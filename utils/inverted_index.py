

class InvertedIndex:
    def __init__(self):
        
        self.index = {}
        self.documents = {}

    def add_document(self, doc_id, text):
        if doc_id in self.documents:
            self.remove_document(doc_id)

        self.documents[doc_id] = text
        tokens = text.lower().split()  
        for token in tokens:
            if token not in self.index:
                self.index[token] = set()
            self.index[token].add(doc_id)

    def remove_document(self, doc_id):
        if doc_id not in self.documents:
            return
        text = self.documents[doc_id]
        tokens = text.lower().split()
        for token in tokens:
            if token in self.index:
                self.index[token].discard(doc_id)
                if not self.index[token]:
                    del self.index[token]
        del self.documents[doc_id]

    def search(self, query, mode="union"):
        tokens = query.lower().split()
        results = None

        for token in tokens:
            docs = self.index.get(token, set())
            if results is None:
                results = docs.copy()  
            else:
                if mode == "intersection":
                    results = results.intersection(docs)
                else:  
                    results = results.union(docs)

        
        if results is None:
            results = set()
        return [(doc_id, self.documents[doc_id]) for doc_id in results]
