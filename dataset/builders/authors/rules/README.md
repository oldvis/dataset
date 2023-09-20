# README

This directory stores the heuristic rules for author name processing.

## Project Structure

This directory is structured as:

```
📂rules
 ┣ 📜replace_substring.py   - rules for replacing substrings in the input author names
 ┗ 📜README.md
```

## `replace_substring.py`

Each rule in `replace_substring.py` has the following data structure:

```typescript
interface Entry {
    /** The substring in the author name to be replaced. */
    substring: string
    /** The value to replace. */
    replaceWith: string
} 
```
