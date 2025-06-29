def initialize_memory():
    return {"Scientist": [], "Philosopher": []}

def update_memory(memory, speaker, argument):
    memory[speaker].append(argument)

def summarize_memory(memory, speaker):
    opponent = "Philosopher" if speaker == "Scientist" else "Scientist"
    return memory[opponent][-2:] if len(memory[opponent]) >= 2 else memory[opponent]
