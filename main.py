import hashlib
import itertools
from string import ascii_lowercase


def get_md5_hashes_in_target_file(path_to_file):
    """

    Pass the path to local hash_string file in order to read every hash line by line into list.

    Example:
        $ get_md5_hashes_in_target_file("./hash_string")

    Section breaks are created by resuming unindented text. Section breaks
    are also implicitly created anytime a new section starts.

    Attributes:
        path_to_file (string): Path to local hash_string file.

            Every line should contain exactly one single hash.
    """
    content = None
    with open(path_to_file, "r") as file_handler:
        try:
            content = [element.strip() for element in file_handler.readlines()]
        except Exception as e:
            print(f"Something went wrong when reading the file: {e}")

    return content[0].strip()


def get_generator_for_alphabet():
    """

    Yields a generator for alphabet. This list will be iterated for Brute-Force.

    Example:
        $ get_generator_for_alphabet()

    The list of words is generated using the yield-keyword.
    """
    for size in itertools.count(1):
        for s in itertools.product(ascii_lowercase, repeat=size):
            yield "".join(s)


if __name__ == '__main__':
    print("Aylin Yilmaz - Simple Bruteforce & Dictionary Example: ")
    print("v0.1")
    print("")
    print("(0) Start Brute-Force ==")
    print("(1) Start Dictionary-Attack ==")

    user_input = input("Please choose from above list: ")

    # BRUTE-FORCE ATTACK
    if int(user_input) == 0:
        # string to be cracked
        hashed_pw_ba = get_md5_hashes_in_target_file("brute_force_example/hash_string")

        # iterate words generated from alphabet
        for element in get_generator_for_alphabet():
            h = hashlib.md5(element.encode('utf-8')).hexdigest().upper()

            print(f"Checking word {element}: {h} == {hashed_pw_ba}")

            if h == hashed_pw_ba:
                print(3 * "\n" + "======" + 3 * "\n")
                print(f"Found! ==> {element} matches for {h}")
                print(3 * "\n" + "======" + 3 * "\n")
                break

    # DICTIONARY ATTACK
    if int(user_input) == 1:
        hashed_pw_da = get_md5_hashes_in_target_file("dictionary_example/hash_string")

        dictionary = []
        f = open("dictionary_example/rockyou.txt", encoding='utf-8', errors='ignore')
        dictionary = f.read().splitlines()
        f.close()

        for word in dictionary:
            h = hashlib.md5(word.encode('utf-8')).hexdigest().upper()

            print(f"Checking word {word}: {h} == {hashed_pw_da}")

            if h == hashed_pw_da:
                print(3 * "\n" + "======" + 3 * "\n")
                print(f"Found! ==> {word} matches for {h}")
                print(3 * "\n" + "======" + 3 * "\n")
                break
