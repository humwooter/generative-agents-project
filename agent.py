from memory import TimeWeightedVectorStoreRetrieverModified
from logic import Reflection, Planning, Reaction, Interview, Summarization

class Agent:
    def __init__(self, name, description, traits, occupation, feelings):
        self.name = name
        self.description = description
        self.traits = traits
        self.occupation = occupation
        self.feelings = feelings
        self.memory = TimeWeightedVectorStoreRetrieverModified()
        self.reflection = Reflection()
        self.planning = Planning()
        self.reaction = Reaction()
        self.interview = Interview()
        self.summarization = Summarization()

    def add_memory(self, content, time, importance_score):
        self.memory.add_document(content, time, importance_score)

    def get_relevant_memories(self, query):
        return self.memory.get_relevant_documents(query)

    def update_summary(self):
        if self.summarization.needs_update():
            self.summarization.run_characteristics(self)
            self.summarization.run_occupation(self)
            self.summarization.run_feeling(self)
            self.summarization.combine_outputs()

    def engage_in_dialogue(self, query):
        response = self.interview.generate_response(query)
        return response

    def remember(self, content, time, importance_score):
        self.add_memory(content, time, importance_score)

    def reflect(self):
        self.reflection.run(self)

    def plan(self):
        self.planning.run(self)

    def react(self):
        self.reaction.run(self)

    def participate_in_interview(self):
        self.interview.run(self)

    def summarize(self):
        self.update_summary()
        return self.summarization.summary
