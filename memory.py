class Memory:
    def __init__(self):
        self.documents = []

    def add_document(self, content, time, importance_score):
        self.documents.append({'content': content, 'time': time, 'importance_score': importance_score})

    def get_relevant_documents(self, query):
        relevant_documents = []
        for document in self.documents:
            if query in document['content']:
                relevant_documents.append(document)
        return relevant_documents

