from agent.agentic_workflow import GraphBuilder
import json
import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
def evaluate_response(question, answer,max_attempts=2):
            for attempt in range(max_attempts):
                print(f"\n Attempt {attempt+1}: Generating response...")
                graph = GraphBuilder(model_provider="openai")
                react_app=graph()
                evaluation_prompt = f"""
                You are an evaluator. Rate the AI's response for the following metrics (0–1 scale):

                1️⃣ Faithfulness – factual accuracy and no hallucinations  
                2️⃣ Relevance – how well it answers the question  
                3️⃣ Conciseness – clear and non-repetitive  

                Question: {question}
                Answer: {answer}

                Output JSON  only:
                {{
                    "faithfulness": <0-1>,
                    "relevance": <0-1>,
                    "conciseness": <0-1>
                }}
                """
                eval_response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[{"role": "user", "content": evaluation_prompt}],
                    temperature=0
                )
                text = eval_response.choices[0].message.content.strip()
                try:
                    scores = json.loads(text)
                except json.JSONDecodeError:
                    scores = {"faithfulness": 0.0, "relevance": 0.0, "conciseness": 0.0}
                print(f"Evaluation scores: {scores}")
                #threshold check
                thresholds = {"faithfulness": 0.8, "relevance": 0.75, "conciseness": 0.65}
                low_scores = {m: v for m, v in scores.items() if m in thresholds and v < thresholds[m]}

                #Retry only if needed
                if low_scores:
                    print(f"⚠️ Low metrics detected: {low_scores}")
                    refined_query = (
                        f"{question}\n"
                                            "Before finalizing your response, double-check each fact. "
                                            "For every place, time, or activity you mention, confirm it exists in the tool outputs. "
                                            "If not, remove or mark it as unavailable. "
                                            "Output only verified, grounded details."
                                    )
                    output = react_app.invoke({"messages": [refined_query]})
                    # If result is dict with messages:
                    if isinstance(output, dict) and "messages" in output:
                        answer = output["messages"][-1].content  # Last AI response
                    else:
                        answer = str(output)
                else:
                    return answer
                    
            return answer



def evaluation(output, question: str, max_attempts=2):

    score = evaluate_response(question, output)
    return score
