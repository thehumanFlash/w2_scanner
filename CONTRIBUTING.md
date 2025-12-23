# Contributing to w2_scanner

Thank you for your interest in contributing to w2_scanner! We welcome contributions from the community.

## How to Contribute

### Reporting Bugs

If you find a bug, please open an issue on GitHub with:
- A clear description of the problem
- Steps to reproduce the issue
- Expected vs actual behavior
- Your environment (OS, Python version, etc.)

### Suggesting Features

We welcome feature suggestions! Please open an issue with:
- A clear description of the feature
- Why it would be useful
- Any implementation ideas you have

### Setting Up Development Environment

1. Install [uv](https://github.com/astral-sh/uv) if you haven't already:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. Clone your fork and set up the environment:
```bash
git clone https://github.com/YOUR_USERNAME/w2_scanner.git
cd w2_scanner
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv pip install -e ".[dev]"
```

This installs the package in editable mode with all development dependencies.

### Submitting Pull Requests

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature-name`)
3. Make your changes
4. Write or update tests if applicable
5. Ensure all tests pass
6. Commit your changes (`git commit -am 'Add some feature'`)
7. Push to the branch (`git push origin feature/your-feature-name`)
8. Open a Pull Request

### Code Style

- Follow PEP 8 guidelines for Python code
- Write clear, descriptive commit messages
- Add comments for complex logic
- Update documentation as needed

### Testing

- Add tests for new features in the `tests/` directory
- Ensure existing tests pass before submitting PR
- Run tests:
```bash
pytest
```

### Code Quality

Run code formatting with Black:
```bash
black src/ tests/
```

Run type checking with mypy:
```bash
mypy src/
```

Run linting with flake8:
```bash
flake8 src/ tests/
```

## Questions?

Feel free to open an issue for any questions about contributing.

