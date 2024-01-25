import re
with open("input.txt", "r") as fil:
    words = fil.readlines()

all_numbers = [re.findall(r"\d", word.rstrip()) for word in words]
two_digits_numbers = [int(f"{d[0]}{d[-1]}") for d in all_numbers if d]

print(f"Part 1 answer: {sum(two_digits_numbers)}")

## alphabet digits
spelled_numbers = {
    "one": 1,
    "two": 2,
    "three":3,
    "four":4,
    "five":5,
    "six":6,
    "seven":7,
    "eight":8,
    "nine":9
    }

## fuck sevenine lol
reversed_nums = {k[::-1]:v for (k,v) in spelled_numbers.items()}

nums_to_sub =  ["one"]

re_match = "|".join(list(spelled_numbers.keys()))
re_match = f"(\d)|({re_match})"

re_match_reversed = "|".join(list(reversed_nums.keys()))
re_match_reversed = f"(\d)|({re_match_reversed})"

all_numbers_forward = [re.findall(re_match, word.rstrip()) for word in words]
all_numbers_reversed = [re.findall(re_match_reversed, word.rstrip()[::-1]) for word in words]

nums = []
for match,rmatch  in zip(all_numbers_forward,all_numbers_reversed):
    flat_digit_list = [item for t in match for item in t if item]
    flat_digit_list = [int(num) if num.isdigit() else spelled_numbers[num] for num in flat_digit_list]

    flat_digit_list_reversed = [item for t in rmatch for item in t if item]
    flat_digit_list_reversed = [int(num) if num.isdigit() else reversed_nums[num] for num in flat_digit_list_reversed]
    nums.append(int(f"{flat_digit_list[0]}{flat_digit_list_reversed[0]}"))

print(f"Part 2 answer is: {sum(nums)}")
