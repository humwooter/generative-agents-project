from agent import Agent
from logic import Reflection, Planning, Reaction, Interview, Summarization
from llm import OpenAILanguageModel
from info import api_key


# Instantiate the language model
language_model = OpenAILanguageModel(api_key=api_key)

# Instantiate a new agent
agent = Agent(name="Bob", 
              description="A friendly AI", 
              traits={"kindness": 5, "intelligence": 7}, 
              occupation="Chatbot", 
              feelings={"happiness": 7, "stress": 2},
              language_model=language_model)


# Add some memories
agent.add_memory(content="Bob helped a user solve a complex problem.", time="2023-06-15 10:00", importance_score=8)
agent.add_memory(content="Bob made a mistake in a calculation.", time="2023-06-15 11:00", importance_score=5)

# Add some goals and stimuli for the agent
agent.goals = [{"priority": 6, "action": "Learn more about AI."}, {"priority": 4, "action": "Chat with users."}]
agent.stimuli = [{"intensity": 6, "response": "React to a system error."}, {"intensity": 4, "response": "Engage with a new user."}]

# Get the agent to reflect on its behavior
agent.reflect()

# Get the agent to plan its next action
agent.plan_next_action()
print(agent.plan)
print(agent)

# Get the agent to react to stimuli
agent.react()  # Now we have stimuli to react to
print(agent.behavior)

# Get the agent to participate in an interview
agent.engage_in_dialogue("what is your main purpose?")
# print(agent.engage_in_dialogue("What is your main purpose?"))

# Get the agent to summarize its current state
print(agent.summarize())

