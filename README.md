# Claude for Non-Tech People

This repository is a simple, beginner-friendly guide to help you use Claude more effectively without knowing coding.

The goal is to turn your rough ideas into clear prompts, improve the quality of answers, and teach you how to navigate tasks in a clean and structured way.

## What this repo helps you do

- Turn vague thoughts into strong prompts
- Improve grammar and clarity before sending a request to Claude
- Structure tasks into clear steps
- Get better output for coding, research, writing, debugging, and planning
- Learn quick, practical ways to work with repositories and commands without deep technical knowledge

## Core idea

A strong prompt has five parts:

1. Role: tell Claude who it should act like
2. Goal: say exactly what you want
3. Context: give the needed background
4. Constraints: define limits, style, or requirements
5. Output format: tell it how the result should look

When you follow this pattern, Claude gives much better answers.

## Quick start

Use this formula for almost everything:

"Act as [role]. I want to [goal]. Context: [background]. Constraints: [rules]. Please provide [format]."

### Example

"Act as a senior software engineer and project manager. I want to improve the performance of this repository. Context: I am a beginner and need simple, clear guidance. Constraints: explain in plain English, avoid jargon, and suggest the best next steps. Please provide a step-by-step plan and a list of practical commands with explanations."

## Use the prompt optimizer

This repo includes a simple script that helps improve your prompt automatically.

### Run it

```bash
python3 scripts/prompt_optimizer.py
```

Then paste your rough prompt when asked.

It will turn your input into a cleaner, stronger prompt with better instructions.

## Recommended prompt pattern

Use this when working on repo tasks:

"Act as a senior technical assistant for a beginner. I want to [task]. Context: I am not technical and need simple instructions. I am working in this repository: [repo name]. Constraints: explain everything in plain English, suggest safe steps, prioritize the easiest route, and ask questions only if needed. Please give me: 1) a clear summary, 2) exact steps, 3) commands to run, 4) what to check if something fails, and 5) a final suggested output format."

## How to navigate tasks better

When a task feels confusing, break it into these steps:

1. Understand the goal
2. List the important context
3. Decide what the final result should look like
4. Ask Claude to plan before doing work
5. Ask for commands and explanations in simple language
6. Validate the result before accepting it

This keeps you from getting lost in technical details.

## Beginner command guide

Use the file `docs/repo-command-map.md` for practical repo commands without heavy technical language.

Common tasks include:

- inspect repo files
- explain project structure
- fix a bug
- optimize code
- summarize changes
- review pull requests
- prepare a clean answer for a task

## Repo structure

```text
README.md
prompt-playbook.md
workflow-guide.md
docs/
  repo-command-map.md
scripts/
  prompt_optimizer.py
```

## A few ready-made templates

### Template 1: Explain a project

"Act as a technical mentor for a beginner. Explain this repository in plain English. Focus on: purpose, structure, key files, and how a new user should begin. Keep it simple and avoid unnecessary jargon."

### Template 2: Fix a problem

"Act as a debugging assistant for a beginner. I need help fixing [issue]. Context: [what happened]. Constraints: explain the cause in simple terms, suggest the safest fix, and provide step-by-step instructions. Please also tell me what to check if the issue still remains."

### Template 3: Optimize a prompt

"Act as a prompt engineer for non-technical users. Improve this prompt for clarity and better output quality. Keep the original intent but make it stronger and easier for an AI assistant to follow. Add structure, constraints, and an output format."

## Best practices

- Be specific about the goal
- Mention your level of expertise
- Ask for plain English explanations
- Request step-by-step instructions
- Ask for reasons, not just commands
- Ask for a safe fallback if something fails

## Important note

This repo is designed to act like a guide and prompt assistant. It does not replace a full coding environment, but it helps you ask better questions, understand repo tasks, and work more confidently with AI tools.

## Suggested next step

Start with `prompt-playbook.md` to learn the prompt structure and then use the optimizer script to improve your own requests.

---

This repository is meant to make Claude easier for everyday users: less confusion, clearer prompts, better results, and a smoother way to navigate technical tasks.





























































































































































































