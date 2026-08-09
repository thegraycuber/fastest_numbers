import math

one_names = [
    [["ноль", 1], ["нулевых", 3]],
    [["один", 2], ["первых", 2]],
    [["два", 1, 1], ["вторых", 2]],
    [["три", 1], ["третьих", 2]],
    [["четыре", 3], ["четвёртых", 3]],
    [["пять", 1], ["пятых", 2]],
    [["шесть", 1], ["шестых", 2]],
    [["семь", 1], ["седьмых", 2]],
    [["восемь", 2], ["восьмых", 2]],
    [["девять", 2], ["девятых", 3]],
    [["десять", 2], ["десятых", 3]],
    [["одиннадцать", 4], ["одиннадцатых", 5]],
    [["двенадцать", 3], ["двенадцатых", 4]],
    [["тринадцать", 3], ["тринадцатых", 4]],
    [["четырнадцать", 4], ["четырнадцатых", 5]],
    [["пятнадцать", 3], ["пятнадцатых", 4]],
    [["шестнадцать", 3], ["шестнадцатых", 4]],
    [["семнадцать", 3], ["семнадцатых", 4]],
    [["восемнадцать", 4], ["восемнадцатых", 5]],
    [["девятнадцать", 4], ["девятнадцатых", 5]],
]

ten_names = [
    [[]],
    [[]],
    [["двадцать", 2], ["двадцатых", 3]],
    [["тридцать", 2], ["тридцатых", 3]],
    [["сорок", 2], ["сороковых", 4]],
    [["пятьдесят", 3], ["пятидесятых", 5]],
    [["шестьдесят", 3], ["шестидесятых", 5]],
    [["семьдесят", 3], ["семидесятых", 5]],
    [["восемьдесят", 4], ["восьмидесятых", 5]],
    [["девяносто", 4], ["девяностых", 4]],
]

hundred_names = [
    [[]], # 0
    [["сто", 1], ["сотых", 2]],
    [["двести", 2], ["двухсотых", 3]],
    [["триста", 2], ["трехсотых", 3]],
    [["четыреста", 4], ["четырехсотых", 5]],
    [["пятьсот", 2], ["пятисотых", 4]],
    [["шестьсот", 2], ["шестисотых", 4]],
    [["семьсот", 2], ["семисотых", 4]],
    [["восемьсот", 3], ["восьмисотых", 4]],
    [["девятьсот", 3], ["девятисотых", 5]],
]

large_names = [
    ["тысяча", "тысячи", "тысяч", 3, 1000, 3, 'f'],
    ["миллион", "миллиона", "миллионов", 3, 1000000, 6, 'm'],
    ["миллиард", "миллиарда", "миллиардов", 3, 1000000000, 9, 'm'],
]

superscripts = ['⁰', '¹', '²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹',
                '¹⁰', '¹¹', '¹²', '¹³', '¹⁴', '¹⁵', '¹⁶', '¹⁷', '¹⁸', '¹⁹',
                '²⁰', '²¹', '²²', '²³']

number_names = []
pemdas_count = 6

def get_plural_form(number):
    mod10 = number % 10
    mod100 = number % 100
    if 11 <= mod100 <= 14:
        return 2
    if mod10 == 1:
        return 0
    if 2 <= mod10 <= 4:
        return 1
    return 2

def base_syllables(n):
    if n < 20:
        return one_names[n][0][1], one_names[n][0][0], one_names[n][1][1], one_names[n][1][0], 0, 1
    elif n < 100:
        n_mod = n % 10
        n_div = n // 10
        if n % 10 == 0:
            return ten_names[n_div][0][1], ten_names[n_div][0][0], ten_names[n_div][1][1], ten_names[n_div][1][0], 1, 2

        return (
            ten_names[n_div][0][1] + number_names[n_mod]["syllables"][1],
            ten_names[n_div][0][0] + " " + number_names[n_mod]["names"][1],
            ten_names[n_div][0][1] + number_names[n_mod]["syllables"][0],
            ten_names[n_div][0][0] + " " + number_names[n_mod]["names"][0],
            0,
            2
        )

    elif n < 1000:
        n_mod = n % 100
        n_div = n // 100
        if n_mod == 0:
            return (
                hundred_names[n_div][0][1], hundred_names[n_div][0][0],
                hundred_names[n_div][1][1], hundred_names[n_div][1][0],
                2, 3
            )
        return (
            hundred_names[n_div][0][1] + number_names[n_mod]["syllables"][1],
            hundred_names[n_div][0][0] + " " + number_names[n_mod]["names"][1],
            hundred_names[n_div][0][1] + number_names[n_mod]["syllables"][0],
            hundred_names[n_div][0][0] + " " + number_names[n_mod]["names"][0],
            0, 3
        )

    large_index = 0
    while (large_names[large_index + 1][4] <= n):
        large_index += 1

    n_mod = n % large_names[large_index][4]
    n_div = n // large_names[large_index][4]

    plural_idx = get_plural_form(n_div)
    magnitude_word = large_names[large_index][plural_idx]
    magnitude_sylls = large_names[large_index][3]

    n_div_name_cardinal = number_names[n_div]["names"][1]
    if large_names[large_index][6] == 'f':
        if n_div_name_cardinal.endswith("один"):
            n_div_name_cardinal = n_div_name_cardinal[:-4] + "одна"
        elif n_div_name_cardinal.endswith("два"):
            n_div_name_cardinal = n_div_name_cardinal[:-3] + "две"

    if n_mod == 0:
        return (
            number_names[n_div]["syllables"][1] + magnitude_sylls,
            n_div_name_cardinal + " " + magnitude_word,
            number_names[n_div]["syllables"][1] + magnitude_sylls,
            n_div_name_cardinal + " " + magnitude_word,
            large_names[large_index][5] + number_names[n_div]["zeroes"],
            large_names[large_index][5] + number_names[n_div]["digits"]
        )

    return (
        number_names[n_div]["syllables"][1] + magnitude_sylls + number_names[n_mod]["syllables"][1],
        n_div_name_cardinal + " " + magnitude_word + " " + number_names[n_mod]["names"][1],
        number_names[n_div]["syllables"][1] + magnitude_sylls + number_names[n_mod]["syllables"][0],
        n_div_name_cardinal + " " + magnitude_word + " " + number_names[n_mod]["names"][0],
        number_names[n_mod]["zeroes"],
        large_names[large_index][5] + number_names[n_div]["digits"]
    )


def number_names_generator(leave_point, max_number):
    max_syllables = 0

    for n in range(0, max_number + 1):
        n_syllables, n_name, frac_syllables, frac_name, zeroes, digits = base_syllables(n)
        adj_zeroes = zeroes
        if zeroes > 3:
            adj_zeroes = (zeroes // 3) * 3

        number_names.append(
            {
                "value": n,
                "syllables": [frac_syllables] + [n_syllables] * (pemdas_count - 1),
                "names": [frac_name] + [n_name] * (pemdas_count - 1),
                "equations": [str(n)] * pemdas_count,
                "original": n_syllables,
                "zeroes": adj_zeroes,
                "digits": digits,
                "nonzero": digits - zeroes,
                "auto pass": (n % 100 < 20 and n % 100 > 0) or zeroes < 1 or digits < 3,
            }
        )
        max_syllables = max(max_syllables, n_syllables)

    syllable_key = [[]]
    for u in range(pemdas_count):
        syllable_key[0].append([])

    unary = [
        {"id": "²", "syllables": 2, "text": " квадрат", "value": 2, "pemdas_input": 2, "pemdas_result": 2},
        {"id": "³", "syllables": 1, "text": " куб", "value": 3, "pemdas_input": 2, "pemdas_result": 2},
    ]

    binary = [
        {"id": "+", "syllables": 1, "text": " плюс ", "suffix": "", "pemdas_left": 5, "pemdas_right": 5,
         "pemdas_result": 5},
        {"id": "*", "syllables": 1, "text": " на ", "suffix": "", "pemdas_left": 3, "pemdas_right": 4,
         "pemdas_result": 4},
        {"id": "-", "syllables": 2, "text": " минус ", "suffix": "", "pemdas_left": 5, "pemdas_right": 4,
         "pemdas_result": 5},
        {"id": "/", "syllables": 3, "text": " делить на ", "suffix": "", "pemdas_left": 3, "pemdas_right": 2,
         "pemdas_result": 4},
        {"id": "fraction", "syllables": 0, "text": " ", "suffix": "", "pemdas_left": 2, "pemdas_right": 0,
         "pemdas_result": 2},
        {"id": "^", "syllables": 2, "text": " в степени ", "suffix": "", "pemdas_left": 2, "pemdas_right": 0,
         "pemdas_result": 2},
    ]

    min_missing = 1
    for s in range(1, max_syllables + 1):
        print("searching", s, "syllables, at", min_missing)

        syllable_key.append([])
        for u in range(pemdas_count):
            syllable_key[s].append([])

        for n in range(min_missing, max_number + 1):
            for u in range(pemdas_count):
                if number_names[n]["syllables"][u] < s:
                    break
                if number_names[n]["syllables"][u] == s:
                    syllable_key[s][u].append(number_names[n]["value"])
                elif u > 0:
                    break

        for op in binary:
            # print(op)

            min_left, max_left = get_first_extremes(op, min_missing, max_number)
            for left_syllables in range(s - op["syllables"]):
                for left_value in syllable_key[left_syllables][op["pemdas_left"]]:
                    if left_value < min_left:
                        continue
                    if left_value > max_left:
                        break

                    min_right, max_right = get_second_extremes(op, min_missing, max_number, left_value)

                    for right_value in syllable_key[s - op["syllables"] - left_syllables][op["pemdas_right"]]:
                        if right_value < min_right:
                            continue
                        if right_value > max_right:
                            break
                        if (op["id"] == "fraction"
                                and not number_names[left_value]["auto pass"]
                                and right_value != 2
                                and number_names[left_value]["zeroes"] >= number_names[right_value]["digits"]
                                and (number_names[left_value]["nonzero"] > 1 or number_names[right_value][
                                    "nonzero"] > 1)
                                and number_names[left_value]["names"][1] == number_names[left_value]["names"][2]):
                            continue

                        op_output, valid_output = get_output(op, left_value, right_value)
                        if not valid_output:
                            continue

                        new_name = (number_names[left_value]["names"][op["pemdas_left"]]
                                    + op["text"]
                                    + number_names[right_value]["names"][op["pemdas_right"]]
                                    + op["suffix"])

                        new_equation = number_names[left_value]["equations"][op["pemdas_left"]]
                        if op["id"] == "^" and new_equation == number_names[left_value]["equations"][1]:
                            new_equation = new_equation + " " + superscripts[right_value]
                        elif op["id"] == "^":
                            new_equation = "(" + new_equation + ") " + superscripts[right_value]

                        else:
                            if op["id"] == "fraction":
                                new_equation += " / "
                            else:
                                new_equation += " " + op["id"] + " "
                            new_equation += number_names[right_value]["equations"][op["pemdas_right"]]

                        for u in range(op["pemdas_result"], pemdas_count):

                            if number_names[op_output]["syllables"][u] >= s:
                                number_names[op_output]["names"][u] = new_name
                                number_names[op_output]["equations"][u] = new_equation

                                if number_names[op_output]["syllables"][u] > s:
                                    number_names[op_output]["syllables"][u] = s
                                    syllable_key[s][u].append(op_output)

        for op in unary:
            # print(op)
            if s <= op["syllables"]:
                continue

            min_value, max_value = get_first_extremes(op, min_missing, max_number)
            for input_value in syllable_key[s - op["syllables"]][op["pemdas_input"]]:
                if input_value < min_value:
                    continue
                if input_value > max_value:
                    break

                op_output, valid_output = get_output(op, input_value)
                if not valid_output:
                    continue

                new_name = number_names[input_value]["names"][op["pemdas_input"]] + op["text"]
                new_equation = number_names[input_value]["equations"][op["pemdas_input"]]
                if new_equation == number_names[input_value]["equations"][1]:
                    new_equation = new_equation + " " + op["id"]
                else:
                    new_equation = "(" + new_equation + ") " + op["id"]

                for u in range(op["pemdas_result"], pemdas_count):
                    if number_names[op_output]["syllables"][u] >= s:
                        number_names[op_output]["names"][u] = new_name
                        number_names[op_output]["equations"][u] = new_equation

                        if number_names[op_output]["syllables"][u] > s:
                            number_names[op_output]["syllables"][u] = s
                            syllable_key[s][u].append(op_output)

        for i in range(pemdas_count):
            syllable_key[s][i].sort()
        while number_names[min_missing]["syllables"][-1] <= s:
            min_missing += 1
            if min_missing > leave_point:
                break
        if min_missing > leave_point:
            break

    return number_names[0:leave_point + 1]


def get_first_extremes(op, min_missing, max_number):
    if op["id"] == "²":
        return min_missing ** (1 / 2), max_number ** (1 / 2)
    elif op["id"] == "³":
        return min_missing ** (1 / 3), max_number ** (1 / 3)
    elif op["id"] == "+":
        return 6, max_number - 1
    elif op["id"] == "*":
        return 2, max_number ** 0.5
    elif op["id"] == "-":
        return min_missing + 1, max_number
    elif op["id"] == "/" or op["id"] == "fraction":
        return min_missing * 2, max_number
    elif op["id"] == "^":
        return 2, max_number ** 0.2


def get_second_extremes(op, min_missing, max_number, left_value):
    if op["id"] == "+":
        return 1, min(left_value, max_number - left_value)
    elif op["id"] == "*":
        return max(left_value, min_missing / left_value), max_number / left_value
    elif op["id"] == "-":
        return 1, left_value - min_missing
    elif op["id"] == "/" or op["id"] == "fraction":
        return 2, left_value / 2
    elif op["id"] == "^":
        return 5, math.log(max_number) / math.log(left_value)


def get_output(op, left_value, right_value=0):
    if op["id"] == "²":
        return left_value ** 2, True
    if op["id"] == "³":
        return left_value ** 3, True
    elif op["id"] == "^":
        return left_value ** right_value, True
    elif op["id"] == "+":
        return left_value + right_value, True
    elif op["id"] == "*":
        return left_value * right_value, True
    elif op["id"] == "-":
        return left_value - right_value, True
    elif op["id"] == "/" or op["id"] == "fraction":
        if left_value % right_value == 0:
            return left_value // right_value, True
        return 0, False


def numbers_out(number_names, file_name):
    with open(file_name, "w", encoding="utf-8") as f:
        for l in number_names:
            f.write(str(l["value"]) + "," + l["names"][-1] + "," + l["equations"][-1] + "," + str(
                l["syllables"][-1]) + "\n")


fast_numbers = number_names_generator(1000000, 2000000)
numbers_out(fast_numbers, 'fastest_numbers_ru.csv')
