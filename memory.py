import spacy

nlp = spacy.load('en_core_web_md')  # Loading a pre-trained model


class Memory:
    def __init__(self):
        self.documents = []

    def get_similarity_score(self, text1, text2):  # computes cosine similarity between two documents
        doc1 = nlp(text1)
        doc2 = nlp(text2)
        return doc1.similarity(doc2)

    def add_document(self, content, time, importance_score):
        self.documents.append({'content': content, 'time': time, 'importance_score': importance_score})

    def get_relevant_documents(self, query):
        relevant_documents = []
        for document in self.documents:
            if query in document['content']:
                relevant_documents.append(document)
        return relevant_documents

    def get_relevant_documents_with_scores(self, query):
        relevant_documents = self.get_relevant_documents(query)
        for document in relevant_documents:
            document['score'] = self.get_similarity_score(query, document['content'])
        # Sort the documents based on the score
        relevant_documents.sort(key=lambda doc: doc['score'], reverse=True)
        return relevant_documents

    def get_latest_memory(self):
        """
        Retrieves the latest memory based on time.
        """
        if self.documents:  # Make sure the memory is not empty
            latest_memory = max(self.documents, key=lambda doc: doc['time'])
            return latest_memory
        else:
            print("no memories")
            return None  # Return None if the memory is empty
