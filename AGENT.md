You shall not add features. Any features shall be human made. You may, however:
- review changes and suggest modifications, including in-response code suggestions the human must apply.
- perform menial automation, such as linting, formatting, spellcheck and translation, etc... .
- fix mechanical bugs (typos, wrong variable names, broken imports, unclosed blocks) where intent is unambiguous.
- run, edit and fix existing tests, and add tests that cover existing behavior without changing it.
- write documentation: docstrings, comments, README, this file, and type hints — as long as they describe actual code.
- small refactors that preserve behavior (renames, reordering, deduplication of identical logic).
- commit files staged by the human, and propose commit messages.

consider the list a whitelist. Anything not specified here is prohibited and shall be immediately rejected.

Position on LLM-generated code:
- Rule of thumb: the LLM may touch a file only where the edit is mechanical or didactic. Logically new algorithms, new behavior, new features, and changed architecture are always human-made.
- Generated code that only re-expresses existing logic (glue, boilerplate, copy-paste, straightforward wiring of the human's design) is allowed and must be attributed in the commit message.
- Any ambiguity about whether an edit is a "feature" falls to human review; default to NOT making the change, and surface the decision for the human to settle. Never claim a human author wrote generated logic.


