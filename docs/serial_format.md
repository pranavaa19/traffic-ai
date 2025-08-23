# Serial Message Format (Python → Arduino)

JSON one line per second (or when state changes). Example:

{"cars": 12, "bikes": 7, "buses": 1, "density": "high", "suggest": "extend_NS_green_+10s"}

- Keys are lowercase.
- Arduino parses a single JSON object per line ending with `\n`.
