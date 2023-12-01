def parse1(text:str) -> int:

    nums = [str(r) for r in range(1,10)]
    vals = [t for t in text if t in nums]
    return int(vals[0] + vals[-1])

def parse2(text:str) -> int:

    num_list = [str(r) for r in range(1,10)]
    num_map = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }

    nums = list()
    new_start = 0
    for i,t in enumerate(text):

        tmp_text = text[new_start:i+1]

        if t in num_list:
            nums.append(t)

        for k,v in num_map.items():
            if k in tmp_text:
                new_start = i-1
                nums.append(v)

    return int(nums[0] + nums[-1])


if __name__=="__main__":

    # example for 1st section
    input_values = [
        "1abc2",
        "pqr3stu8vwx",
        "a1b2c3d4e5f",
        "treb7uchet"
    ]

    # example for 2nd portion
    input_values = [
        "two1nine",
        "eightwothree",
        "abcone2threexyz",
        "xtwone3four",
        "4nineeightseven2",
        "zoneight234",
        "7pqrstsixteen"
    ]

    input_file = "input_1.txt"
    input_file = "input_2.txt"
    with open(input_file, 'r') as f:
        lines = f.read()
        input_values = [l.strip() for l in lines.split() if l != '']

    vals = [parse2(i) for i in input_values]

    # not 55330
    print(f"Answer: {sum(vals)}")

