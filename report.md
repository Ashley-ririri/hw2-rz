## 0. Sample Input (Raw Meeting Notes)
> "John mentioned he needs to finish the project demo by next Wednesday. Mike said he can get the data cleanup done and sent to Sarah by Saturday. Sarah noted she'll handle the backend API once she gets that data from Mike. We all agreed to meet again tomorrow at 2 PM to check in on everyone's progress."

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
Here is a summary and action plan based on the meeting notes:

### Executive Summary

The primary objective of the meeting was to ensure the project demo is completed by next Wednesday. Key decisions include Mike completing data cleanup and delivering it to Sarah by Saturday for her backend API work. A follow-up progress check meeting is scheduled for tomorrow at 2 PM to maintain momentum.

### Action Items

| Task                                  | Owner | Deadline       |
| :------------------------------------ | :---- | :------------- |
| Finish data cleanup and send to Sarah | Mike  | This Saturday  |
| Handle backend API                    | Sarah | Before next Wednesday (dependent on Mike) |
| Follow-up meeting for progress check  | Group | Tomorrow 2 PM  |
| Finalize Project Demo                 | Group | Next Wednesday |

### Potential Risks

*   **Tight Deadline Dependency:** Mike's deadline of "This Saturday" for data cleanup is critical. Any delay will directly impact Sarah's ability to complete the backend API in time, subsequently jeopardizing the final demo deadline of "Next Wednesday."
*   **Ambiguous Ownership for Demo Assembly:** While "Finalize Project Demo" is assigned to the "Group," specific tasks for overall demo assembly, front-end integration, and testing are not explicitly assigned to individuals, which could lead to overlooked components.

## 4. Prompting Strategy Analysis
To improve the quality of the meeting minutes, I applied several key Prompt Engineering techniques:

* **Role Prompting:** By assigning the persona of a "Senior Executive Assistant," the AI adopted a more formal tone and prioritized high-level overviews.
* **Structured Output (Markdown):** Explicitly requesting a Markdown table transformed unstructured text into a scannable, project-management-ready format.
* **Reasoning & Risk Assessment:** In the final version, I tasked the AI with identifying "Potential Risks." This forced the model to perform basic logical reasoning regarding task dependencies and deadlines.
* **Negative Constraints:** Using phrases like "max 3 sentences" ensured the Executive Summary remained concise and avoided "AI hallucinations" or wordiness.

## 5. Limitations & Future Enhancements

### Limitations
* **Relative Time Parsing:** The AI currently struggles with relative dates (e.g., "next Wednesday"). Without a reference date, these deadlines remain ambiguous.
* **Speaker Identification:** In more complex, multi-speaker transcripts, the model may occasionally misattribute tasks if the dialogue overlaps.

### Future Enhancements
* **Date Normalization:** Future iterations will include a system prompt to convert all relative dates into a standard YYYY-MM-DD format.
* **Automated Email Drafting:** I plan to add a step where the AI automatically generates a follow-up email draft addressed to each task owner.