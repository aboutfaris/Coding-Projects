# Password Application Suite

A Python command-line password generator. `pass_gen.py` asks how many letters, symbols, and numbers you want, picks random characters, shuffles them, and prints the password.

## What you'll use

- Python 3 (standard library `random` only)
- A terminal opened in this repository folder

## Steps

1. Run the script.

   ```bash
   python3 pass_gen.py
   ```

   Expected result: it prints `Welcome to the PyPassword Generator!` and asks the first question.

2. Answer the three prompts with whole numbers:
   - How many letters would you like in your password?
   - How many symbols would you like?
   - How many numbers would you like?

3. Read the output.

   Expected result: the script prints the list of chosen characters, the same list after shuffling, and then `Your Password Is <password>`. Letters come from a to z and A to Z, symbols from `! # $ % & ( ) * +`, and numbers from 0 to 9.

4. Note the known quirk: all three loops use the letter count, so the symbol and number answers are ignored. For example, answering 2, 5, and 5 gives a 6-character password with 2 letters, 2 symbols, and 2 numbers.

## What I learned

- Picking random items with `random.choice()` and mixing them with `random.shuffle()`.
- Building a string from a list of characters.
- Testing a script with different inputs is how you catch bugs like a loop using the wrong variable.
