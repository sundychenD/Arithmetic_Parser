# Arithmetic Parser
---
A basic arithmetic parser written in Python. Parsing the string into Abstract Syntax Tree then evaluate.
---
Evaluating Process:
String => Lexical Analyzer => Build AST => Recursive Evaluate

Operator Supported
`+, -, *, /`

Example
```
3 + 2
>>> 5

1 * 2 + 9 / 3 / 3
>>> 3.0

1 / 2 + 9 / 3 / 3
>>> -2.6666666666666665
```
