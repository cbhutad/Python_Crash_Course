def count_words(filename):

    try:
        with open(filename,encoding="utf-8") as file_obj:
            contents = file_obj.read()
    except FileNotFoundError:
        pass
    else:
        result = contents.lower().count("the ")
        print(result)

files = ["..\Examples\input_files\odyssey.txt", "..\Examples\input_files\pi_million_digits.txt", "..\Examples\input_files\\alice.txt"]
for file in files:
    count_words(file)