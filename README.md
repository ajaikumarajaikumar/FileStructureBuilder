# File Structure Parser & Manager

A desktop utility that interprets a custom mini-language to define and create file and folder structures on your system. It features:

- **Custom DSL** for directory trees
- **Parser** with syntax validation
- **Interactive GUI** for real-time feedback
- **Error handling** (unbalanced parentheses, unexpected tokens)
- **Advanced rules**: 
  - Dot-prefixed names (`.gitignore`, `.config`)
  - Escaped characters (`my\,file.txt`)
  - Redundancy detection with prompts

## Installation

No external Python packages required (uses standard library).

```bash
# Clone the repo
git clone https://github.com/yourusername/FileStructureParser.git
cd FileStructureParser
```

## Usage

### GUI
```bash
python gui_app.py
```
- Enter your structure script in the text box.
- Click **Create** to generate folders/files under `output/`.

### CLI
```bash
python main.py "project(src(main.py),README.md)"
```

## Test Cases

Refer to `test_cases.txt` for 10 important test inputs covering valid, warning, and error scenarios.

## Files

- `fs_parser.py` – Parser implementation
- `gui_app.py` – GUI application
- `main.py` – CLI entry and file creation logic
- `test_cases.txt` – Sample test inputs
- `LICENSE` – Project license (e.g., GPL v3.0)
- `.gitignore` – Recommended ignore patterns

## License

Distributed under the **GNU GPL v3.0** license. See `LICENSE` for details.
