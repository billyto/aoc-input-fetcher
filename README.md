# Advent of Code Input Downloader

## Overview

This Python script simplifies downloading input files for Advent of Code challenges. It provides a command-line interface to easily fetch input files for specific days and years.

## Prerequisites

- Python 3.8+
- `uv` (Python package manager)
- Advent of Code account

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/aoc-input-downloader.git
cd aoc-input-downloader
```

2. Create and activate a virtual environment:
```bash
uv venv
source .venv/bin/activate  # On Unix/macOS
# Or on Windows
.venv\Scripts\activate
```

3. Install dependencies:
```bash
uv pip install -r <(uv pip compile pyproject.toml)
```

## Configuration

### Obtaining Your Session Cookie

1. Log in to [Advent of Code](https://adventofcode.com/)
2. Open browser developer tools (F12)
3. Go to the "Application" or "Storage" tab
4. Find the `session` cookie under Cookies for adventofcode.com
5. Copy the cookie value

### Setting Up Environment Variables

Create a `.env` file in the project root:
```
AOC_SESSION_COOKIE=your_session_cookie_here
```

**Important:** Never share your `.env` file or commit it to version control.

## Usage

### Basic Usage

Download input for the current year's day:
```bash
python aoc_downloader.py <day>
```

Example:
```bash
python aoc_downloader.py 1  # Downloads day 1 of the current year
```

### Specifying a Year

Download input for a specific year:
```bash
python aoc_downloader.py <day> -y <year>
# Or
python aoc_downloader.py <day> --year <year>
```

Example:
```bash
python aoc_downloader.py 1 -y 2023  # Downloads day 1 of 2023
```

## Input File Location

Downloaded input files are saved in the `inputs/` directory with the naming convention `dayXX.txt` (e.g., `day01.txt`, `day02.txt`).

## Troubleshooting

- **Invalid Session Cookie:** Ensure your `.env` file contains a valid session cookie
- **Download Errors:** Check your internet connection and Advent of Code account
- **Permission Issues:** Verify you have write permissions in the script directory

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or distribute this software, either in source code form or as a compiled binary, for any purpose, commercial or non-commercial, and by any means.

In jurisdictions that recognize copyright laws, the author or authors of this software dedicate any and all copyright interest in the software to the public domain. We make this dedication for the benefit of the public at large and to the detriment of our heirs and successors. We intend this dedication to be an overt act of relinquishment in perpetuity of all present and future rights to this software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <https://unlicense.org>

## Disclaimer

This script is a community project and is not officially associated with Advent of Code.
