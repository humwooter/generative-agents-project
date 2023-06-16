from logic import Reflection, Planning, Reaction, Interview, Summarization
from memory import Memory
import traceback


class Agent:
    def __init__(self, name, description, traits, occupation, feelings, language_model):
        self.name = name
        self.description = description
        self.traits = traits  # Should be a dictionary
        self.occupation = occupation
        self.feelings = feelings
        self.goals = []  # Initialize with a list of dictionaries
        self.plan = ""  # Initialize with an empty string
        self.stimuli = []  # Initialize with a list of dictionaries
        self.behavior = ""  # Initialize with an empty string
        self.language_model = language_model

        try:
            self.memory = Memory()
            self.reflection = Reflection()
            self.planning = Planning()
            self.reaction = Reaction()
            self.interview = Interview(self)
            self.summarization = Summarization(self)
        except Exception as e:
            print(f"Failed to initialize components: {e}")
            traceback.print_exc()

        
    def __str__(self):
        """
        Returns a string representation of the Agent with all its attributes.
        """
        return (
            f"Agent(\n"
            f"\tname={self.name},\n"
            f"\tdescription={self.description},\n"
            f"\ttraits={self.traits},\n"
            f"\toccupation={self.occupation},\n"
            f"\tfeelings={self.feelings},\n"
            f"\tgoals={self.goals},\n"
            f"\tplan={self.plan},\n"
            f"\tstimuli={self.stimuli},\n"
            f"\tbehavior={self.behavior},\n"
            f"\tmemories={self.memory.documents},\n"  # Assuming the Memory object has a `documents` attribute
            f")"
        )
    def add_memory(self, content, time, importance_score):
        try:
            self.memory.add_document(content, time, importance_score)
        except Exception as e:
            print(f"Failed to add memory: {e}")

    def get_relevant_memories(self, query):
        try:
            return self.memory.get_relevant_documents(query)
        except Exception as e:
            print(f"Failed to get relevant memories: {e}")

    def update_summary(self):
        try:
            if self.summarization.needs_update(self):  # pass self as an argument
                self.summarization.run_characteristics(self)
                self.summarization.run_occupation(self)
                self.summarization.run_feeling(self)
                self.summarization.combine_outputs()
        except Exception as e:
            print(f"Failed to update summary: {e}")


    def engage_in_dialogue(self, query):
        try:
            response = self.interview.generate_response(query)
            return response
        except Exception as e:
            print(f"Failed to engage in dialogue: {e}")

    def remember(self, content, time, importance_score):
        self.add_memory(content, time, importance_score)

    def reflect(self):
        try:
            self.reflection.run(self)
        except Exception as e:
            print(f"Failed to reflect: {e}")

    def plan_next_action(self):
        try:
            self.planning.run(self)
        except Exception as e:
            print(f"Failed to plan: {e}")

    def react(self):
        try:
            self.reaction.run(self)
        except Exception as e:
            print(f"Failed to react: {e}")

    def participate_in_interview(self):
        try:
            self.interview.run(self)
        except Exception as e:
            print(f"Failed to participate in interview: {e}")


    def summarize(self):
        try:
            self.summarization.run(self)  # Run the summarization
            self.summary = self.summarization.summary
        except Exception as e:
            print(f"Failed to summarize: {e}")
