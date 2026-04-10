# /// script
# dependencies = ["openai"]
# ///

# app.py
# Homework 2 — Meeting Notes to Structured Summary
# Uses the OpenAI API to convert raw meeting notes into a structured summary and action items.
# Run with: uv run app.py

import os
from openai import OpenAI

# ─────────────────────────────────────────────
# 1. Load API key from environment variable
# ─────────────────────────────────────────────
api_key = os.environ.get("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY environment variable is not set. Please set it before running.")

client = OpenAI(api_key=api_key)

# ─────────────────────────────────────────────
# 2. System prompt — tells the model what to do
# ─────────────────────────────────────────────
SYSTEM_PROMPT = """You are a professional business assistant that converts raw meeting notes into structured summaries and action items.

Rules:
- Do NOT invent information that is not present in the notes.
- Do NOT change or reinterpret dates or deadlines. Use the exact wording from the notes.
- If owner or deadline is missing, write: Not specified
- Include unresolved or pending decisions as a separate section.
- If the notes involve legal, compliance, or sensitive topics, add a note that human review is recommended.
- Keep the tone professional and concise.

Always respond in exactly this format:

Meeting Summary:
- bullet points

Action Items:
1. Task:
   Owner:
   Deadline:

Pending Decisions:
- items where no decision was made
"""

# ─────────────────────────────────────────────
# 3. Sample meeting notes input
# ─────────────────────────────────────────────
MEETING_NOTES = """
Discussed Q3 product launch timeline.
Marketing team to prepare campaign assets by end of May.
John to coordinate with the design team on visuals.
Launch is planned for June 15.
Budget for ads still needs approval from finance.
Sarah will follow up with the finance team next week.
No decision made yet on post-launch support staffing.
"""

# ─────────────────────────────────────────────
# 4. Print the input
# ─────────────────────────────────────────────
print("=" * 40)
print("=== INPUT ===")
print("=" * 40)
print(MEETING_NOTES.strip())

# ─────────────────────────────────────────────
# 5. Make the API call
# ─────────────────────────────────────────────
response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": MEETING_NOTES}
    ]
)

output_text = response.choices[0].message.content

# ─────────────────────────────────────────────
# 6. Print the output
# ─────────────────────────────────────────────
print("\n" + "=" * 40)
print("=== OUTPUT ===")
print("=" * 40)
print(output_text)

# ─────────────────────────────────────────────
# 7. Save the output to a file
# ─────────────────────────────────────────────
with open("output.txt", "w") as f:
    f.write("=== INPUT ===\n")
    f.write(MEETING_NOTES.strip() + "\n\n")
    f.write("=== OUTPUT ===\n")
    f.write(output_text)

print("\n✅ Output saved to output.txt")
