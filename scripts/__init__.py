#!/usr/bin/env python3
"""Simple prompt optimizer for non-technical users.

This tool takes a rough prompt and transforms it into a clearer,
stronger prompt using a beginner-friendly structure.

Usage:
    python3 scripts/prompt_optimizer.py
    python3 scripts/prompt_optimizer.py "my rough prompt"
    python3 scripts/prompt_optimizer.py < my_prompt.txt
"""

import sys


def improve_prompt(raw_prompt: str) -> str:
    text = raw_prompt.strip()
    if not text:
        return '''Act as a technical mentor for a beginner. I want help with a task in this repository. Context: I am not technical and need clear, simple guidance. Constraints: explain everything in plain English, avoid jargon, prioritize the safest and easiest approach, and give step-by-step instructions. Please provide: 1) a short summary, 2) the best first steps, 3) the key files or areas to inspect, 4) suggested commands or actions, and 5) a quick troubleshooting section.'''

    # Basic heuristics to add helpful structure
    lines = []
    lines.append("Act as a senior technical assistant for a beginner.")
    lines.append("I want to " + text.rstrip(".?") + ".")
    lines.append("Context: I am not highly technical and need plain-English explanations.")
    lines.append("Constraints: keep it clear, structured, actionable, and easy to follow. Avoid unnecessary jargon. Explain the reason behind each step.")
    lines.append("Please provide: 1) a concise summary, 2) the safest next steps, 3) the most important files or areas to inspect, 4) any commands or actions to take, and 5) a quick troubleshooting section if something goes wrong.")
    return "\n".join(lines)


def main():
    if len(sys.argv) > 1:
        # Input provided as an argument
        raw_prompt = " ".join(sys.argv[1:])
    else:
        print("Paste your rough prompt below. Press Ctrl+D (Linux/macOS) or Ctrl+Z then Enter (Windows) when finished.")
        raw_prompt = sys.stdin.read()

    optimized = improve_prompt(raw_prompt)
    print("\n--- Optimized Prompt ---\n")
    print(optimized)


if __name__ == "__main__":
    main()































































































































































