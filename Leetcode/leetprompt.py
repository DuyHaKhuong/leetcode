#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Generate and print a standard prompt for creating a LeetCode Python file from a URI.

This script does not create files or open any IDE. It only prints
the standardized prompt text for downstream tooling.

Usage:
  python3 leetprompt.py <leetcode-problem-url>
"""

import argparse
import sys


TEMPLATE = """The goal is generate the Python file for Leetcode problems given URI from users. The Python file has description,
starter code (similar to what Leetcode gives user), and tests from examples in description.

Task:
Given the following raw problem description (extracted from LeetCode, possibly poorly formatted):

{{raw_description}}
{{templte code}}
{{code to run examples (not test)}}

If the file exists, ask user again if they want to overwrite it or open it in IDE. Please generate a single Python file
with the following structure:

0. You can run python3 leetgrab.py to generate most of the content (possibly in poor format) before step 1

1. A clean top-level docstring:
   - Title, URL, Difficulty, Fetched date
   - A well-formatted description in paragraphs
   - Clearly formatted "Examples" section:
     * Each example should show Input, Output, and Explanation
   - A clearly formatted "Constraints" section as a bulleted list

2. A code template:
   - class Solution with the correct method signature inferred from the problem, similar to the one in URI
   - The method body should contain only `pass`

3. Add code run examples
these examples are from the description in the URI, add the code to run the end. Note it is not the tests. 
All code are under the same def check_examples(self) functions, one line for one example (make it early to commend it
out)
if name == "__main__":
  sol = Solution()
  print(sol....<input>)  
Then open the new file with Intellij IDEA CE. DO NOT ADD ANY HINTS, NO MORE TEXT OTHER THAN THE DESCRIPTION  URI ={uri}"""


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description="Print the standardized LeetCode prompt for a given URI.")
    ap.add_argument("uri", help="LeetCode problem URL")
    args = ap.parse_args(argv)

    print(TEMPLATE.format(uri=args.uri))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
