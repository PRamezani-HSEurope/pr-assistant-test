# PR Assistant code review instructions

Review every changed pull request for variable naming violations.

- Require `snake_case` for every variable name in Python and JavaScript/TypeScript code.
- In JavaScript/TypeScript, apply `snake_case` to local variables and object properties. Preserve framework-required names and public APIs unless the repository explicitly uses a different convention.
- Do not report acronyms, constants, function names, class names, imports, or string values unless they are variable names.
- For each violation, identify the exact file and line, show the offending name, and recommend the snake_case replacement.
