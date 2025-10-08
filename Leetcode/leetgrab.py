#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
LeetCode URL -> starter Python file generator.

Usage examples:
  python3 leetgrab.py https://leetcode.com/problems/two-sum/
  python3 leetgrab.py --clipboard --open
  python3 leetgrab.py <url> --force --open

Optional shell helper (add to ~/.zshrc):
  lc() { python3 /Users/duyha/Code/Leetcode/leetgrab.py "$@" --dir /Users/duyha/Code/Leetcode; }
Then run: lc https://leetcode.com/problems/two-sum/
"""

import argparse
import datetime as dt
import json
import os
import re
import subprocess
import sys
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from typing import Optional

LEETCODE_GRAPHQL = "https://leetcode.com/graphql"

GRAPHQL_QUERY = """
query questionData($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    questionId
    title
    titleSlug
    difficulty
    content
    codeSnippets { lang langSlug code }
    topicTags { name slug }
  }
}
"""

# Default output directory (can be overridden with --dir)
DEFAULT_DIR = "/Users/duyha/Code/Leetcode"


def slug_from_url(url: str) -> str:
    m = re.search(r"leetcode\.com/problems/([^/]+)/?", url)
    if not m:
        raise ValueError("Could not extract slug from URL.")
    return m.group(1)


def html_to_text(html: str) -> str:
    if not html:
        return ""
    soup = BeautifulSoup(html, "html.parser")
    for br in soup.find_all("br"):
        br.replace_with("\n")
    text = soup.get_text("\n")
    text = re.sub(r"\n{3,}", "\n\n", text).strip()
    return text


def to_camel(name: str) -> str:
    parts = re.split(r"[^a-zA-Z0-9]+", name)
    parts = [p for p in parts if p]
    if not parts:
        return "solve"
    first = parts[0].lower()
    rest = [p.capitalize() for p in parts[1:]]
    return first + "".join(rest)


def fetch_question(slug: str) -> dict:
    headers = {
        "Content-Type": "application/json",
        "Referer": f"https://leetcode.com/problems/{slug}/",
        "User-Agent": "Mozilla/5.0",
    }
    payload = {"query": GRAPHQL_QUERY, "variables": {"titleSlug": slug}}
    r = requests.post(LEETCODE_GRAPHQL, headers=headers, data=json.dumps(payload))
    r.raise_for_status()
    data = r.json()
    q = data.get("data", {}).get("question")
    if not q:
        raise RuntimeError(f"LeetCode returned no question for slug '{slug}'.")
    return q


def pick_python_stub(code_snippets) -> Optional[str]:
    if not code_snippets:
        return None
    for pref in ("python3", "python"):
        for snip in code_snippets:
            if (snip.get("langSlug") or "").lower() == pref:
                return snip.get("code")
    return None


def ensure_dir(dirpath: Path):
    dirpath.mkdir(parents=True, exist_ok=True)


def write_file(path: Path, header: str, code: str, force: bool):
    if path.exists() and not force:
        raise FileExistsError(f"File exists: {path} (use --force to overwrite)")
    with open(path, "w", encoding="utf-8") as f:
        f.write(header)
        if not header.endswith("\n"):
            f.write("\n")
        f.write("\n")
        f.write("from typing import *\n\n")
        f.write(code.rstrip() + "\n\n")
        f.write('if __name__ == "__main__":\n')
        f.write("    pass\n")


def main():
    ap = argparse.ArgumentParser(
        description="Generate a LeetCode Python starter file from a problem URL.",
    )
    ap.add_argument("url", nargs="?", help="LeetCode problem URL. If omitted and --clipboard, read from clipboard.")
    ap.add_argument("--dir", default=DEFAULT_DIR, help="Output directory (default: %(default)s)")
    ap.add_argument("--force", action="store_true", help="Overwrite if file exists.")
    ap.add_argument("--open", action="store_true", dest="open_file", help="Open the file in VS Code (or macOS default editor).")
    ap.add_argument("--clipboard", action="store_true", help="Read the URL from clipboard (macOS pbpaste).")
    ap.add_argument(
        "--fallback-sig",
        default=None,
        help="Fallback method signature (e.g. 'def solve(self, nums: List[int]) -> int:').",
    )
    args = ap.parse_args()

    url = args.url
    if args.clipboard:
        try:
            url = subprocess.check_output(["pbpaste"]).decode("utf-8").strip()
        except Exception:
            print("Failed to read from clipboard; provide a URL.", file=sys.stderr)
            sys.exit(2)

    if not url:
        ap.print_help()
        sys.exit(2)

    slug = slug_from_url(url)
    q = fetch_question(slug)

    title = q.get("title") or slug.replace("-", " ").title()
    difficulty = q.get("difficulty") or "Unknown"
    content_html = q.get("content") or ""
    desc_text = html_to_text(content_html)
    code_snip = pick_python_stub(q.get("codeSnippets"))

    # If LeetCode doesn't expose a Python stub, manufacture a minimal one.
    if not code_snip:
        method = to_camel(title)
        sig = args.fallback_sig or f"def {method}(self, nums: List[int]) -> int:"
        code_snip = f"class Solution:\n    {sig}\n        pass"

    timestamp = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    header = f'''""" 
LeetCode: {title}
URL: https://leetcode.com/problems/{slug}/
Difficulty: {difficulty}
Fetched: {timestamp}

Description:
{desc_text}
"""'''

    outdir = Path(args.dir).expanduser()
    ensure_dir(outdir)
    outfile = outdir / f"{slug}.py"

    write_file(outfile, header, code_snip, args.force)

    print(f"✓ Wrote {outfile}")
    if args.open_file:
        # Try VS Code 'code' first, then macOS 'open' fallback
        try:
            subprocess.run(["code", str(outfile)], check=False)
        except Exception:
            subprocess.run(["open", str(outfile)], check=False)


if __name__ == "__main__":
    try:
        main()
    except requests.HTTPError as e:
        print(f"HTTP error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
