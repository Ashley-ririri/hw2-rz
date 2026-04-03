import os
import google.generativeai as genai
from dotenv import load_dotenv

# 1. Setup: Load API Key from .env file
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("❌ Error: GEMINI_API_KEY not found in .env file.")
    exit()

# Configure the SDK
genai.configure(api_key=api_key)

def run_genai_workflow(input_text, system_instruction):
    """
    Sends the meeting notes to Gemini and returns a structured action plan.
    """
    try:
        # We use 'gemini-2.5-flash' which is fast and free for most users.
        # If you still get a 404, you can try changing it to 'gemini-1.5-pro'
        model_name = 'gemini-2.5-flash' 
        model = genai.GenerativeModel(model_name)
        
        # Combine the instruction and the notes
        full_prompt = f"{system_instruction}\n\nMeeting Notes:\n{input_text}"
        
        # Generate content
        response = model.generate_content(full_prompt)
        
        # Check if response has text (to avoid errors with blocked content)
        if response.text:
            return response.text
        else:
            return "⚠️ Warning: The model returned an empty response."
            
    except Exception as e:
        return f"❌ API Error: {str(e)}"

def main():
    # --- CONFIGURATION (Iterate on this for Step 5 of your assignment) ---
    # Initial Version of System Instruction
    system_instruction = (
        "You are a professional administrative assistant. "
        "Please summarize the following meeting notes into a clear, "
        "structured list of action items, identifying who is responsible for what."
    )
    
    # Sample Input (From your Eval Set)
    test_input = """
    John: We need to finish the project demo by next Wednesday.
    Sarah: I'll handle the backend API, but I'm waiting for Mike's data.
    Mike: I'll finish the data cleanup and send it to Sarah by Saturday.
    Group: We agree to meet again tomorrow at 2 PM to check progress.
    """
    
    print(f"🚀 Sending request to Gemini...")
    
    # Execute workflow
    result = run_genai_workflow(test_input, system_instruction)
    
    # 2. Print Output to Terminal for immediate feedback
    print("\n--- AI Generated Output ---")
    print(result)
    
    # 3. Save Output to a File (Required by your assignment)
    # Using 'utf-8' encoding to ensure Chinese/special characters work
    with open("output.txt", "w", encoding="utf-8") as f:
        f.write(result)
    
    print("\n✅ Success: Results saved to output.txt")

if __name__ == "__main__":
    main()