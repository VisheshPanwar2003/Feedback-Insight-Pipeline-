import os
from google import genai
import pandas as pd
from dotenv import load_dotenv

# Load environment variables from the .env file at the project root
load_dotenv()

def generate_executive_summary(critical_issues: pd.DataFrame, cluster_reps: pd.DataFrame) -> str:
    """Generates an LLM summary combining SQL metrics and NLP centroids."""
    
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key or api_key == "your_actual_api_key_here":
        return (
            "⚠️ Valid GEMINI_API_KEY not found in .env.\n"
            "[MOCK LLM RESPONSE]: Based on the data, the most critical issue is a 1.0 "
            "average rating related to late deliveries, backed by the semantic cluster "
            "highlighting 'Delivery was 3 days late'. Meanwhile, UI updates are performing well."
        )

    print("Calling Gemini API for synthesis...")
    # Initialize the modern Google GenAI Client
    client = genai.Client(api_key=api_key)
    
    # Construct the prompt using our pipeline data
    prompt = f"""
    Act as a Product Manager analyzing customer feedback.
    
    Here are the critical quantitative issues (Avg Rating < 3.0) from our SQL database:
    {critical_issues.to_string(index=False)}
    
    Here are the core semantic themes extracted via NLP K-Means clustering:
    {cluster_reps.to_string(index=False)}
    
    Write a concise, 3-sentence executive summary explaining what is going wrong and what is going right. 
    Do not mention SQL, NLP, or K-Means. Just state the business insights.
    """
    
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt
        )
        return response.text.strip()
    except Exception as e:
        return f"LLM Generation Failed: {e}"

if __name__ == "__main__":
    # Quick local test with dummy data
    mock_issues = pd.DataFrame({'category': ['bugs'], 'avg_rating': [2.0]})
    mock_reps = pd.DataFrame({'Representative_Comment': ['App crashes on upload']})
    print(generate_executive_summary(mock_issues, mock_reps))