# Prompt Strategy & Templates

This document records the prompt strategy and user-facing prompt templates used while developing and operating the AI Resume Analyzer project. It also contains the session prompts the developer used during this work (for traceability and reproducibility).

NOTE: This file does not include any internal system prompts or hidden assistant instruction templates.

---

## Purpose

- Document how to interact with the assistant to perform common developer tasks (edits, deploy fixes, debugging).  
- Provide reusable prompt templates for contributors and maintainers.  
- Preserve the session prompts used during development for reproducibility and auditing.

---

## Prompt Strategy (high level)

- Be explicit about the file paths and exact edits required.  
- For deployments/debugging, paste full error blocks and screenshots when possible.  
- For CLI operations, copy-paste terminal outputs (not screenshots) for easier parsing.  
- Prefer small, atomic changes with clear commit messages.  
- When asking the assistant to run commands or edit files in the repo, include the repository path and target branch.

---

## Reusable Prompt Templates

Use these templates when asking the assistant to perform common tasks.

- Patch & commit

  "Edit `path/to/file` to change X into Y, commit with message 'MSG', and push to `main`."

- Add documentation

  "Create `docs/NAME.md` that explains X, include examples and usage, commit and push."

- Debug deploy

  "Check Railway deploy logs for project `<project-name>` and identify any package build errors; suggest minimal changes to `requirements.txt` or `runtime.txt` and push fixes." 

- CLI help

  "Give exact Railway CLI commands to link the repo and stream logs, and explain expected outputs and where to paste them back." 

- Feature implementation

  "Implement feature `<short-description>`: modify backend, templates, and add tests. Provide a small example and commit with message 'feat: <short-description>'."

---

## Example Prompts Used During This Project

The following are the user prompts that were used in this development session (developer-supplied inputs). They are recorded here for reproducibility and context.

1. you push the change
2. yes
3. guide
4. ok i grant railway cli access
5. option a
6. where i can find railway api key
7. cannot find
8. option a
9. Paste your Railway API key here and I’ll login and stream the build logs. (developer supplied CLI feedback instead of key)
10. cannot find
11. ok i grant railway cli access
12. option a
13. where i can find railway api key
14. cannot find
15. this happened (attached Railway 404 screenshot)
16. again failed (attached build error screenshot)
17. yes
18. B
19. ok i grant railway cli access
20. option a
21. where i can find railway api key
22. cannot find
23. ok
24. what to do next
25. omawasthi@Oms-MacBook-Air ~ % npm i -g @railway/cli (terminal output pasted)
26. screenshot showing `npx @railway/cli@latest link`
27. what to do next
28. omawasthi@Oms-MacBook-Air ~ % npx @railway/cli@latest logs -f (error output pasted)
29. this happened (attached build logs screenshot)
30. again failed
31. this (Python runtime error screenshot)
32. what to do next
33. npx @railway/cli@latest logs -f --service web (error pasted)
34. this is showing (deploy logs showing Gunicorn boot)
35. but i thought the name of the website will come as ai humananalyxer
36. ok
37. no i want Prompt Template used and prompts used for this project
38. yes
39. no i want Prompt Template used and prompts used for this project (repeat)
40. yes (confirm show session prompts)
41. does my repo include the following items
42. ok add

---

## How to Reuse

- Copy any template above and fill in the placeholders (paths, messages).  
- When collaborating, include the branch name and intended commit message.  
- For troubleshooting, include CLI outputs and screenshots in the issue or chat.

---

## Security & Privacy

- Do not store or publish API keys, secrets, or private data in prompts or repository files.  
- Review logs and screenshots for sensitive information before pasting them into public channels.  
- If an API key must be provided for CLI automation, use a short-lived project-scoped token and rotate it immediately afterwards.

---

If you want this file adjusted (more examples, different wording, or removal of any prompts), tell me what to change and I will update it and push a new commit.
