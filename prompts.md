# Prompt Iteration History

This document tracks the evolution of the system instructions for the Meeting Minutes to Action Items workflow.

---

## 1. Initial Version (v0)
**Prompt:**
> "You are an administrative assistant. Summarize the following meeting notes into a list of action items."

**What changed and why:**
This was the baseline prompt. It was simple and focused only on extracting tasks without any specific formatting requirements.

**Observation:**
The output was a plain bulleted list. While accurate, it was hard to read at a glance, and it didn't clearly separate who was responsible for which task or when the deadlines were.

---

## 2. Revision 1 (v1)
**Prompt:**
> "You are a professional Project Manager. Summarize the meeting notes into a structured Markdown table with the following columns: Task, Owner, and Deadline. If an owner is not clearly mentioned, mark it as 'TBD' (To Be Determined)."

**What changed and why:**
I changed the persona to "Project Manager" to encourage a more professional tone and added a requirement for a **Markdown table**. I also added logic to handle unassigned tasks (TBD) to improve accountability.

**Observation:**
The readability improved significantly. The table format made it easy to scan. However, it still missed the "big picture" of the meeting—it only focused on tasks but ignored the overall context or major decisions.

---

## 3. Revision 2 (v2 - Final)
**Prompt:**
> "You are a Senior Executive Assistant. First, provide a brief 'Executive Summary' (max 3 sentences) of the meeting's core purpose and major decisions. Second, list all action items in a Markdown table with columns for Task, Owner, and Deadline. Finally, add a section for 'Potential Risks' to flag any tasks that have extremely tight deadlines or ambiguous owners."

**What changed and why:**
I added an **Executive Summary** for high-level context and a **Potential Risks** section. This adds a layer of "intelligence" to the tool, as it now critiques the information instead of just reformatting it.

**Observation:**
This is the most successful version. The Executive Summary gives the user an immediate update, and the "Potential Risks" section provides genuine business value by identifying bottlenecks. The system now acts more like an analyst than a simple formatter.