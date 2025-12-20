def get_num_words(book_text):
    print("----------- Word Count ----------")
    print(f"Found {word_count(book_text)} total words")

def get_book_text (filePath):
    with open(filePath) as fileData:
        fileContents = fileData.read()
    print(f'Analyzing book found at {filePath}...')
    return fileContents

def word_count(book_text):
      word_list = book_text.split()
      return len(word_list)


"""
Take in a string, count the number of appearances of each character
Case insensitve, returns a dictionary with the count for each
"""
def char_count(book_text):
    # use lower() to convert the string to all lower case
    book_text = book_text.lower()
    # create a dictionary
    char_dict = {} 
    # Iterate thorugh each 
    for x in book_text:
        if x in char_dict and x.isalpha():
            char_dict[x] = char_dict[x]+1
        else:    
            char_dict.update({x:1})
    return char_dict


#dictionary is sorted by most to least character occurences
def sort_dict(input_dict):
    sorted_list = []
    for x in input_dict:
        sorted_list.append({"char":x, "num":input_dict[x]})
    
    sorted_list.sort(reverse=True, key =sort_on)
    return sorted_list
    
def sort_on(items):
    return items["num"]

def print_char_list(sorted_char_list):
    print("--------- Character Count -------")
    for x in sorted_char_list:
        print(f'{x['char']}: {x['num']}')


def book_report(filePath):
    print("============ BOOKBOT ============")
    book_text = get_book_text(filePath)
    get_num_words(book_text)
    unsorted_dict = char_count(book_text)
    sorted_list = sort_dict(unsorted_dict)
    print_char_list(sorted_list)
    print("============= END ===============")
