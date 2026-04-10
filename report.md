# Report — Meeting Notes to Action Items

## Business Use Case
This prototype converts raw meeting notes into structured summaries with action items, owners, and deadlines. The user is a manager or team lead who needs to quickly share meeting outcomes with their team. The system receives unstructured meeting notes and produces a clean, consistent written summary that can be shared immediately.

## Model Choice
I initially used Google AI Studio since it offered free access. I set up the API key, installed the google-generativeai package, and configured app.py to use the gemini-2.0-flash model. However, I kept running into quota exhaustion errors even on the free tier. I tried switching to gemini-1.5-flash but that model was not found in the API. I also tried gemini-2.0-flash-lite and created a new API key under a new project, but the quota limit remained at zero across all models. After spending time troubleshooting these issues, I decided to switch to OpenAI using the gpt-4.1-mini model with a paid account. This worked immediately and produced reliable, structured output on the first call. If I were starting over, I would begin with OpenAI to avoid the quota issues I experienced with Google AI Studio.

## Baseline vs Final Design

### Baseline Version
The initial prompt was simple. It told the model to convert meeting notes into a summary and action items, not invent information, and write "Not specified" for missing owners or deadlines. The output was usable but had issues. The model changed "end of May" to "May 31" which added specificity that was not in the original notes. It also ignored the unresolved staffing decision entirely and did not flag it anywhere in the output.

### Final Version
After two revisions, the prompt now includes rules to preserve exact date wording from the notes, a Pending Decisions section for unresolved items, and a flag for sensitive topics like legal or compliance issues recommending human review. The final output kept "end of May" as written, listed the staffing decision under Pending Decisions, and added a note recommending human review for budget and staffing decisions.

## Where the Prototype Still Fails
The system can still struggle with very vague or contradictory notes. When multiple people are mentioned without clear task assignments, the model sometimes guesses who owns what. It also cannot verify whether action items are realistic or whether deadlines conflict with other commitments. For sensitive topics like legal disputes, the model now flags human review, but it could still produce wording that sounds more confident than it should. This is not a system I would trust to run without someone reviewing the output before sharing it.

## Deployment Recommendation
This prototype is useful as a first-draft tool. It saves time by turning messy notes into a clean structured format, but every output should be reviewed by a human before being shared with a team. I would recommend deploying this as a draft assistant with mandatory human review, not as a fully automated system. The time saved on formatting alone makes it worth using, as long as the person reviewing it knows the model can still miss things or misinterpret vague notes.
