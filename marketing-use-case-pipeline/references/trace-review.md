# Trace Review

Use traces to review what the agent actually did.

A useful compact trace should show:

- visible prompt;
- model/provider;
- final answer;
- ordered tool calls;
- tool inputs;
- tool-result previews;
- failed tools;
- referenced paths;
- written paths;
- search queries.

Screenshots and videos are useful for marketing clarity, but they are not a substitute for reviewing agent behavior.

Do not pass multi-megabyte traces to reviewers by default. Create a compact summary first, then inspect full tool calls only when needed.
