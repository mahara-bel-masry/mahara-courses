"""lesson0_selfcheck.py - Lesson 0 self-check: prove the lab works.

Prints the Python version, then the installed version of every library
the diploma uses, then one tiny real operation (tiktoken encode), then a
single verdict line. Run it after installing the environment:

    uv run python lesson0_selfcheck.py

Expected ending: SELF-CHECK: PASS
Keep the output: it is your versions log, the diploma's first habit.
"""
import platform
import sys
from importlib.metadata import version

LIBS = [
    "tiktoken",
    "sentence-transformers",
    "openai",
    "langchain",
    "langgraph",
    "pydantic",
    "mcp",
    "faiss-cpu",
    "peft",
    "openai-whisper",
    "llama-cpp-python",
    "datasets",
    "torch",
    "transformers",
]

print("== lesson 0 self-check ==")
print(f"python: {sys.version.split()[0]} | platform: {platform.machine()}")

missing = []
for lib in LIBS:
    try:
        print(f"  {lib}: {version(lib)}")
    except Exception:
        missing.append(lib)
        print(f"  {lib}: MISSING")

try:
    import tiktoken

    n = len(tiktoken.get_encoding("cl100k_base").encode("hello world!"))
    print(f"tiktoken encode check: {n} tokens")
    op_ok = n == 3
except Exception:
    op_ok = False
    print("tiktoken encode check: FAILED")

print("SELF-CHECK: " + ("PASS" if not missing and op_ok else "FAIL - missing: " + ", ".join(missing)))
