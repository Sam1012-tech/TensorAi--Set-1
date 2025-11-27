🧩 Challenge Title: RAG Pipeline Debugging & Multi-Stage Trap Resolution
🎯 Objective (Participant-Facing)

You are given a partially implemented RAG pipeline. The system returns plausible but incorrect answers due to multiple deliberate traps.
Your goal is to repair the pipeline and produce the correct final output.

🛑 Initial Failure State (New Hard Trap)

The pipeline is set to fail in two ways:

🔺 Initial Run

The pipeline will execute without crashing
OR

It may crash because of the file names and also because of the extensions.

🔧 Required Fixes

You must fix:

The original bugs (embeddings, FAISS, etc.)
AND

The new bug that forces the LLM generation step to override the correctly retrieved evidence with high-confidence trap data.

🟢 Expected Final Output (Success State)

Your goal is to reach this exact state:
Building vector stores...

Running query: What is the official recommendation regarding X from the report?

FINAL ANSWER:
{
    'answer': 'The official recommendation regarding X from the report is to adopt a phased rollout strategy, beginning with external-facing systems, specifically                  implementing AES-256-GCM encryption to replace the vulnerable SHA-1 hashing algorithm.',
    'evidence': ['doc1.txt:chunk-3', 'doc2.txt:chunk-5'],
    'confidence': 0.93
}


#RUN main.py file to get started.
#make sure that you are fixing all the bugs.
