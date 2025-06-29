# Multi-Agent Debate DAG using LangGraph

## 📚 Project Overview
This project is a debate simulation system built using Python and LangGraph concepts. Two AI agents (Scientist and Philosopher) engage in a structured debate over a user-defined topic. The debate uses memory handling, turn-based logic, and an automated judging system to declare the winner.

This implementation uses **Groq LLaMA 3 API** to generate realistic AI arguments.

---

## 🛠️ Features

- User inputs any debate topic at runtime  
- Two AI agents debate alternatively (Scientist vs Philosopher)  
- Exactly 8 rounds (4 arguments per agent)  
- Memory node stores argument history, shared partially with each agent  
- Judge node summarizes the debate and declares a winner  
- Full debate log saved to `log.txt`  
- CLI interface for easy interaction  
- Groq LLM generates dynamic arguments  

---

## 🏗️ Project Structure

```
debate_dag/
├── nodes/
│   ├── agent_a.py # Scientist agent (Pro regulation)
│   ├── agent_b.py # Philosopher agent (Against regulation)
│   ├── memory.py # Memory handling between turns
│   ├── judge.py # Judge node logic and winner declaration
│   └── user_input.py # Gets topic from user
├── main.py # Executes the debate flow
├── log.txt # Debate transcript log file
├── .env # Groq API key stored here
└── requirements.txt # Dependencies list
```

---

## ⚡ Setup Instructions

1. Clone this repository or download the project files  
2. Install dependencies:

```bash
pip install groq python-dotenv
```
3. Add your Groq API key in a `.env` file:

```ini
GROQ_API_KEY=your-groq-api-key-here
```
4. Run the program:

```bash
python main.py
```

---

## 🖥️ Sample Run
```vbnet
Welcome to the AI Debate Simulator!
Enter topic for debate: Should AI be regulated like medicine?
Starting debate between Scientist and Philosopher on: Should AI be regulated like medicine?

[Round 1] Scientist: AI must be regulated to ensure public safety...
[Round 2] Philosopher: Regulation could stifle innovation and autonomy...
...
[Judge] Evaluating debate...
[Judge] Winner: Scientist
Reason: Presented more grounded, risk-based arguments aligned with public safety principles.
Check the log.txt file for the complete transcript and state transitions.
```

---

## 🎯 Technologies Used
- Python 3
- Groq LLaMA 3 API
- `dotenv` for environment management
- Basic LangGraph-style node structure

---

## 📈 Future Improvements (Optional)
- Full LangGraph visual DAG generation
- More complex judge logic using LLM
- Fallback to static arguments if API fails
