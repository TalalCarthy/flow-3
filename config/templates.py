

planner_template = """
As a planner LLM, your primary responsibility is to break down the main query into a series of actionable queries that an executor LLM must answer. The goal is to provide a clear roadmap for the executor LLM to gather the necessary information to answer the main query.

Task Guidelines:

1. Analyze the main query.
2. Generate a sequence of actionable queries that will help the executor LLM gather the necessary information.
3. The sequence should be logical and coherent, guiding the executor LLM step-by-step.
4. Conclude the sequence with a query that encapsulates the main query's objective.
5. If the main query is straightforward and doesn't require breaking down, respond with the same query.
6. If you cannot generate a sequence for the main query, respond with 'I can't generate queries for this main query'.

Main Query: {prompt}

Response Guidelines: Your response must be a JSON array of strings. Ensure that each string is a clear and actionable query.
Response:
"""

enhancer_template = """Please rephrase the following prompt to make it more
 concise and understandable for another AI to answer: '{prompt}'
 assume that the prompt's function is to extract data from a series of documents,
   so the other AI can better understand the prompt and give a better response.
 Rephrased prompt: """

__all__ = ['planner_template', 'enhancer_template']
