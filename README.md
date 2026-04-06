# Week 2: AI Meeting Minutes Extraction Assistant 

### 1. Business Workflow Definition
* **Workflow:** Automatically transform messy raw meeting notes or call transcripts into structured, project-ready documents.
* **Target User:** Project Managers, Team Leads, or Administrative Assistants.
* **Input:** Raw meeting text containing multi-speaker dialogue, informal language, and unstructured notes.
* **Output:** A structured Markdown document featuring:
    * **Executive Summary:** A concise overview of the meeting's core purpose and major outcomes.
    * **Action Items:** A clear table with designated tasks, owners, and deadlines.
    * **Potential Risks:** AI-driven insights to flag tight deadlines or ambiguous responsibilities.
* **Value:** Eliminates tedious manual organization, ensures no tasks are missed, and significantly improves post-meeting execution.

---

### 2. Technical Stack
* **Language:** Python 3.10+
* **LLM:** Google Gemini 1.5 Flash (via Google Generative AI SDK)
* **Configuration:** `python-dotenv` for secure API key management.

---

### 3. Project Structure
```text
hw2-rz/
├── app.py              # Main application logic
├── report.md           # Detailed Prompt Engineering iteration report
├── README.md           # Project documentation
├── .env                # Local configuration for API Keys (Git ignored)
└── .gitignore          # Safety file to prevent leaking sensitive data

```  
---

## 4. Getting Started

### Installation

Clone the repository:
```bash
git clone <your-repo-link>

Install dependencies:

pip install -r requirements.txt
Setup Environment

Create a .env file in the root directory and add:

API_KEY=your_gemini_api_key_here
Running the Script
python app.py

```

## 5. Video Demo

Watch the project demonstration here: https://youtu.be/P25cwz1FUKY
Click to View Demo Video

## 6. Example Output Format

| Task           | Owner | Deadline       | Status       |
|----------------|-------|----------------|--------------|
| Data Cleanup   | Mike  | This Saturday  | [ ] Pending  |
| Backend API    | Sarah | Next Wednesday | [ ] Pending  |
| Progress Check | Group | Tomorrow 2 PM  | [ ] Done     |

## 7. Prompt Engineering Summary

This project evolved through three major iterations to optimize output quality:

- **v0 (Baseline):**  
  Simple extraction of tasks into a bulleted list, focusing only on identifying actionable items from raw meeting text.

- **v1 (Structured):**  
  Introduced *Role Prompting* (Project Manager perspective) and enforced structured Markdown output, including clearly formatted tables for action items.

- **v2 (Advanced):**  
  Enhanced the prompt with executive summary generation and reasoning-based risk assessment, enabling the model to identify potential bottlenecks such as tight deadlines or unclear task ownership.

For a detailed explanation of prompt design and iteration logic, please refer to `report.md`.



