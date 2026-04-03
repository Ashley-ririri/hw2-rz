## 1. Initial Version (v0)
**Prompt:**
> "You are an administrative assistant. Summarize the following meeting notes into a list of action items."

output: 
Here is a list of action items from the meeting:

*   **John:** Finish the project demo by next Wednesday.
*   **Mike:** Complete data cleanup and send it to Sarah by Saturday.
*   **Sarah:** Handle the backend API (contingent on receiving data from Mike).
*   **Group:** Meet again tomorrow at 2 PM to check progress.


## 2. Revision 1 (v1)
**Prompt:**
> "You are a professional Project Manager. Summarize the meeting notes into a structured Markdown table with the following columns: Task, Owner, and Deadline. If an owner is not clearly mentioned, mark it as 'TBD' (To Be Determined)."

output:
As a Project Manager, here is the summary of your meeting notes in a structured Markdown table:

| Task                                  | Owner | Deadline         |
| :------------------------------------ | :---- | :--------------- |
| Finish the project demo               | John  | Next Wednesday   |
| Handle the backend API                | Sarah |                  |
| Finish data cleanup and send to Sarah | Mike  | By Saturday      |
| Hold progress check meeting           | All   | Tomorrow at 2 PM |

## 3. Revision 2 (v2 - Final)
**Prompt:**
> "You are a Senior Executive Assistant. First, provide a brief 'Executive Summary' (max 3 sentences) of the meeting's core purpose and major decisions. Second, list all action items in a Markdown table with columns for Task, Owner, and Deadline. Finally, add a section for 'Potential Risks' to flag any tasks that have extremely tight deadlines or ambiguous owners."

output: 
