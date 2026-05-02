#!/usr/bin/env python3
"""
Merge-Konflikte in docs/3reinforce_learn auflösen (HEAD behalten).
Lauf von Repo-Root: python3 docs/3reinforce_learn/resolve_merge_conflicts.py
"""

import os
import re

# <<<<<<< HEAD ... ======= ... >>>>>>> <any branch>
pattern = re.compile(r"<<<<<<< HEAD\n(.*?)=======.*?>>>>>>> [^\n]+\n", re.DOTALL)

base = os.path.dirname(os.path.abspath(__file__))
fixed = False
for name in os.listdir(base):
    if name == "resolve_merge_conflicts.py":
        continue
    path = os.path.join(base, name)
    if not os.path.isfile(path):
        continue
    try:
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
    except Exception as e:
        print(f"Reading error {path}: {e}")
        continue
    resolved = pattern.sub(r"\1", text)
    if resolved != text:
        n = len(pattern.findall(text))
        with open(path, "w", encoding="utf-8") as f:
            f.write(resolved)
        print(f"Resolved: {n} conflict(s) in {path}")
        fixed = True
if not fixed:
    print("No merge markers found in docs/3reinforce_learn (or already resolved).")
