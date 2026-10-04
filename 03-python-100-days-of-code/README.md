# Python 100 Days of Code (Angela Yu)

My learning diary from the "100 Days of Code: The Complete Python Pro Bootcamp" course by Angela Yu, covering days 1 to 8. The `Day N` files hold my notes and exercise answers, and the `.py` files are the small projects you can run.

## What you'll use

- Python 3 (no extra packages; the scripts only use the standard library)
- A terminal opened in this folder (`03-python-100-days-of-code`)

## Steps

### Part 1: Read the notes

1. Open the `Day N` files in order. Each one is a plain-text page of exercises separated by `---` lines:
   - `Day 1`: empty placeholder.
   - `Day 2`: data types, adding the digits of a two-digit number, a BMI calculator, f-strings, and the tip calculator.
   - `Day 3`: `if`/`elif`/`else` with the roller coaster, odd or even, BMI Calculator 2.0, and leap year exercises.
   - `Day 4`: the pizza order bill calculator.
   - `Day 5`: the love calculator and a random name picker.
   - `Day 6`: the treasure map (nested lists) and rock, paper, scissors.
   - `Day 7`: `for` loops with the average height, highest score, and even or odd number sums.
   - `Day 8`: FizzBuzz and the password generator.
2. Open `Important notes, interview question` for the FizzBuzz answer, which is a common interview question.

### Part 2: Run the projects

3. Run the tip calculator. Enter the bill as a whole number, the tip percentage (10, 12, or 15), and the number of people.

   ```bash
   python3 tip_calculator.py
   ```

   Expected result: for a bill of 150, a 12% tip, and 5 people, it prints `Each person should pay: $33.60`.

4. Run the love calculator. Type your name, press Enter, then type the other person's name.

   ```bash
   python3 love_calculator.py
   ```

   Expected result: it counts the letters of TRUE and LOVE in both names and prints a two-digit score, with a comment for scores under 10 or over 90 and for scores from 40 to 50.

5. Run rock, paper, scissors and type 0 (rock), 1 (paper), or 2 (scissors).

   ```bash
   python3 rock-paper-scissors-game.py
   ```

   Expected result: it prints the ASCII art for your choice and the computer's random choice, then a result line. The win or lose logic is a beginner draft and is not always right, and a number outside 0 to 2 ends with an error after the "invalid number" message.

6. Run the password generator and answer the three prompts (letters, symbols, numbers).

   ```bash
   python3 "Password Generator.py"
   ```

   Expected result: it prints the character list, the shuffled list, and then `Your Password Is <password>`. The script uses the letter count for all three loops, so the password has that many letters, symbols, and numbers each.

7. Read `BMI Calculator.py`, `Leap Year Calculator.py`, and `Tip Calculator.py` as notes rather than programs. The first two are wrapped in markdown backticks, so Python reports a syntax error, and `Tip Calculator.py` holds two attempts joined by the word `OR`, so it stops with a NameError after the first attempt.

## What I learned

- Reading input, converting types, and formatting output with f-strings.
- Writing `if`/`elif`/`else` logic, including nested conditions like the leap year rule.
- Using lists, `random`, and `for` loops to build small games and generators.
