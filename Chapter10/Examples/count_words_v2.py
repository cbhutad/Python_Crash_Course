def count_words(filename):

    try:
        with open(filename,encoding="utf-8") as file_obj:
            contents = file_obj.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        print(f"The {filename} has : {len(words)}")

files = ["input_files\odyssey.txt", "input_files\pi_million_digits.txt", "input_files\\alice.txt"]
for file in files:
    count_words(file)