import logging
import time
from nodes.user_input import get_debate_topic
from nodes.agent_scientist import agent_a_response
from nodes.agent_philosopher import agent_b_response
from nodes.memory import initialize_memory, update_memory, summarize_memory
from nodes.judge import judge_debate

logging.basicConfig(filename="log.txt", level=logging.INFO, filemode='w')

def main():
    print("Welcome to the AI Debate Simulator!")
    topic = get_debate_topic()
    print(f"Starting debate between Scientist and Philosopher on: {topic}\n")
    logging.info(f"Debate Topic: {topic}")

    memory = initialize_memory()

    for round_num in range(8):
        if round_num % 2 == 0:
            speaker = "Scientist"
            summary = summarize_memory(memory, speaker)
            argument = agent_a_response(round_num//2, summary, topic)

        else:
            speaker = "Philosopher"
            summary = summarize_memory(memory, speaker)
            argument = agent_b_response(round_num//2, summary, topic)


        print(f"[Round {round_num+1}] {speaker}: {argument}")
        update_memory(memory, speaker, argument)
        logging.info(f"Round {round_num+1} - {speaker}: {argument}")

        time.sleep(1)

    print("\n[Judge] Evaluating debate...\n")
    summary, winner, reason = judge_debate(memory)
    print("[Judge] Summary of debate:")
    print(summary)
    print(f"\n[Judge] Winner: {winner}")
    print(f"Reason: {reason}")

    logging.info("\n--- FINAL JUDGMENT ---")
    logging.info(summary)
    logging.info(f"Winner: {winner}")
    logging.info(f"Reason: {reason}")

if __name__ == "__main__":
    main()
