def pyramid(n):  # triangle pattern of n height
    y = 1
    for _ in range(n):
        print(("#" * y).center(n * 2))
        y += 2


pyramid(4)


def zip_it(women, men):
    return "sizes don't match" if len(women) != len(men) else list(zip(women, men))

    # zip_it(["Elise", "Mary"], ["John", "Rick"]) ➞ [("Elise", "John"), ("Mary", "Rick")]


def all_truthy(*args):
    return bool(all(args))


def filter_list(lst):
    return [_ for _ in lst if type(_) != str]


def are_same(a, b):
    return a == b

    # == is for value equality. If two objects have the same value.
    # is is for reference equality. If two references refer to the same object.

are_same2 = lambda a, b: a == b

# print(are_same2(1, 2))


def volume_of_box(sizes):
    w, l, h = sizes.values()
    return w * l * h

    # a = list(sizes.values())
    # return a[0] * a[1] * a[2]

# print(volume_of_box({"width": 2, "length": 5, "height": 1}))


def limit_number(n, low, high):
    return high if n > high else low if n < low else n


def limit_number(num, range_low, range_high):
    if num > range_high:
        return range_high
    elif num < range_low:
        return range_low
    else:
        return num


def compare_to_100(x):
    # if x > 100:
    #     return "greater"
    # elif x < 100:
    #     return "smaller"
    # else:
    #     return "equal"

    # if x > 100:
    #     return "greater"
    # if x < 100:
    #     return "smaller"
    # return "equal"

    return "greater" if x > 100 else "smaller" if x < 100 else "equal"


def equilibrium(x):
    return "positive" if x > 0 else "negative" if x < 0 else True


def hello_world(num):
    # if not num % 3:
    #     if not num % 5:
    #         return "Hello World"
    # if not num % 3:
    #     return "Hello"
    # if not num % 5:
    #     return "World"

    # if not num % 3 and not num % 5:
    #     return "Hello World"
    # if not num % 3:
    #     return "Hello"
    # if not num % 5:
    #     return "World"

    # if not num % 15:
    #     return "Hello World"
    # if not num % 3:
    #     return "Hello"
    # if not num % 5:
    #     return "World"

    lst = []
    if not n % 3:
        lst += ["Hello"]
    if not n % 5:
        lst += ["World"]
    return " ".join(lst)

# print(hello_world(13))


def total_cups(n):
    # every sixth cup is free, how many free ones with n cups, ?floor division
    return int(n / 6) + n

# print(total_cups(24))


def unique_sort(lst):
    # purgedList = []
    # for i in sorted(lst):
    #     if i not in purgedList:
    #         purgedList.append(i)
    # return purgedList

    return sorted(list(set(lst)))

# print(unique_sort([7, 6, 5, 4, 3, 2, 1, 0, 1]))


def count_ones(num):
    return bin(num).count("1")

# print(count_ones(999))


def alphabet_soup(txt):
    return "".join(sorted(txt))

# print(alphabet_soup("credibility"))


import datetime
def time_for_milk_and_cookies(date):
    return date.month == 12 and date.day == 24
    # return datetime.date(2000, 12, 24) == date.replace(2000)

# print(time_for_milk_and_cookies(datetime.date(2032, 12, 24)))


def reverse(txt):
    return txt[::-1]
    # return lst.reverse()

# print(reverse("Think different."))


def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

# print(factorial(6))

    # n = 6
    # # n = int(input())
    # num = 1
    # while n >= 1:
    #     num = num * n
    #     n -= 1
    # print(num)


def reverse_case(txt):
    return txt.swapcase()


def XO(txt):
    # checks if it has the same number of "x"s and "o"s
    # return sum(1 for x in txt.lower() if x in 'o') == sum(1 for x in txt.lower() if x in 'x')
    return txt.lower().count("x") == txt.lower().count("o")

# print(XO("ooxXm"))


def count_vowels(txt):
    # vowels = "aeiou"
    # count = 0
    # for letter in txt.lower():
    #     if letter in vowels:
    #         count += 1
    # return count

    return sum([1 for x in txt.lower() if x in "aeiou"])

# print(count_vowels("Quote"))


def add_nums(nums):
    return sum(int(_) for _ in nums.split(", "))
    # return eval(nums.replace(", ", "+"))

    # sum string of numbers add_nums("2, 5, 1, 8, 4") ➞ 20


def counterpartCharCode(char):
    return ord(char.swapcase())

# print(counterpartCharCode("a"))


def check_ending(str1, str2):
    return str1.endswith(str2)

# print(check_ending("abc", "bc"))


def is_last_character_n(word):
    return word[-1] == "n"


def get_abs_sum(lst):
    return sum(abs(i) for i in lst)

# print(get_abs_sum([2, -1, -3, 4, 8]))


def is_avg_whole(arr):
    return (sum(arr) / len(arr)).is_integer()

# print(is_avg_whole([1, 1, 1]))


def cap_me(lst):
    return [name.capitalize() for name in lst]

# print(cap_me(["mavis", "senaida", "letty"]))


def add_up(num):
    return sum(list(range(num + 1)))

# print(add_up(4))


def find_index(lst, txt):
    return lst.index(txt)


import calendar
def month_name(num):
    return calendar.month_name[num]

# print(month_name(2))


def MultiplyByLength(arr):
    return [num * len(arr) for num in arr]

# print(MultiplyByLength([2, 6, 4, 9]))


def noOdds(lst):
    return [num for num in lst if num % 2 == 0]

# print(noOdds([43, 65, 23, 89, 53, 9, 6]))


def isFourLetters(lst):
    return [slovo for slovo in lst if len(slovo) == 4]

# print(isFourLetters(["Ryan", "Kieran", "Jason", "Matt"]))


def mean(lst):
    return round(sum(lst) / len(lst), 2)

# print(mean([324, 543, 654, 9876]))


def sortNumsAscending(lst):
    return sorted(lst)

# print(sortNumsAscending([80, 29, 4, -95, -24, 85]))


def minMaxLengthAverage(lst):
    return [min(lst), max(lst), len(lst), sum(lst) / len(lst)]

# print(minMaxLengthAverage([30, 43, 20, 92, 3, 74]))


def count_words(txt):
    return len(txt.split(" "))

# print(count_words("It's high noon"))


def number_syllables(word):
    # return len(word.split("-"))
    return word.count("-") + 1

# print(number_syllables("on-o-mat-o-poe-ia"))


def find_digit_amount(num):
    return len(str(num))

# print(find_digit_amount(1234))


def minMax(nums):
    return [min(nums), max(nums)]

# print(type(minMax([14, 35, 6, 1, 34, 54])))


def char_count(txt1, txt2):
    # return str.count(txt2, txt1)
    return txt2.count(txt1)

# print(char_count("a", "caar"))


def count_true(lst):
    # return lst.count(True)
    return sum(lst)

    # True - 1, False - 0 period


def check(lst, el):
    return el in lst


def say_hello_bye(name, num):
    return "{} {}".format("Hello" if num else "Bye", name.capitalize())


def concat_name(first_name, last_name):
    return "{}, {}".format(last_name, first_name)
    # return last_name + ", " + first_name


def first_last(lst):
    return [lst[0], lst[-1]]
    # return [lst.pop(0), lst.pop()]

# print(first_last([5, 10, 15, 20, 25]))


def how_many_times(num):
    # return "Ed{}bit".format("a" * num)
    # return "Ed" + "a" * num + "bit"
    return f"Bu{'r' * 5}p"


def reverse_list(num):
    return [int(n) for n in str(num)[::-1]]

# print(reverse_list(1485979))


def isEvenOrOdd(num):
    if num & 1:
        return "odd"
    else:
        return "even"


def parity(n):
    # return "even" if not n % 2 else "odd"
    # return "even" if n % 2 == 0 else "odd"
    return "odd" if n % 2 else "even"


def flip_bool(b):
    return not b


def is_empty(dictionary):
    return not dictionary


def check_equality(a, b):
    return a is b

    # == is for value equality. If two objects have the same value.
    # is is for reference equality. If two references refer to the same object.


def is_safe_bridge(s):
    return not " " in s

    # is_safe_bridge("####") ➞ True
    # is_safe_bridge("## ####") ➞ False


def modify_last(txt, n):
    return txt[:-1] + txt[-1] * n

# print(modify_last("on", 2))


def wumbo(words):
    return words.replace("M", "W")
    # return ''.join([_ if _ != 'M' else 'W' for _ in words])

# print(wumbo("WHAT DO YOU MEAN WE'RE OUT OF MONEY"))


def roger_shots(lst):
    return lst.count("Bang!")

# print(roger_shots(["Bang!", "BangBangBang!", "Boom!", "Bang!", "BangBang!"]))


def add_odd_to_n(n):
    return sum(_ for _ in range(n + 1) if _ % 2)

# print(add_odd_to_n(13))


def yeah_nope(b):
    return "yeah" if b else "nope"

    # ternary operator/conditional expression, if/else alternative
    # condition_if_true if condition else condition_if_false
    # yeah_nope(True) ➞ "yeah"
    # yeah_nope(False) ➞ "nope"


def get_filename(path):  # gets filename form path
    return path.split("/")[-1]

# print(get_filename("C:/Projects/pil_tests/ascii/edabit.txt"))
