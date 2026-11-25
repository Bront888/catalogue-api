# catalogue-api
• Build a small FastAPI service with Postgres (Supabase). Reusing what I know from Aegis.

## What it does
- sends get, update, post and delete API requests 

## Setup
```
py -m venv .venv
pip install fastapi[standard]
winget install --id=astral-sh.uv -e
pip freeze > requirements.txt

```
## Run
uv run fastapi dev

## Test
pytest

## What I learned

- Classes & Type Hints: Built BankAccount with explicit type annotations (str, float, bool, None) for attributes, arguments, and return values.

- Custom Exceptions: Created InsufficientFundsError(Exception), triggered it with raise, and handled it with try ... except.

- List & Dict Comprehensions: Filtered account owners (vips) and mapped names to balances (balance_map) in single, readable lines.

- Dunder Methods & @dataclass: Learned how __repr__ replaces memory addresses with readable output, and how @dataclass auto-generates __init__, __repr__, and ==.

- Automated Testing with pytest: Wrote unit tests using assert, pytest.raises, @pytest.fixture for clean setup, and @pytest.mark.parametrize to test multiple inputs at once.

- Production Code Hygiene: Learned how if __name__ == "__main__": prevents demo code from running on import, why input validation (amount <= 0) protects state, and why decimal.Decimal is preferred over float for money.
