STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file.""" 
    # open file 
    with open(file) as file:
        open_file = file.read() 
    
    import string
    # remove punctuation
    tr = str.maketrans('', '', string.punctuation)
    remove_punc = open_file.translate(tr)

    # normalize all words to lowercase
    lower = remove_punc.lower()
    words = lower.split(' ')

    # remove "stop words" -- words used so frequently they are ignored
    new_words = [word for word in words if word not in STOP_WORDS]
    
    # go through the file word by word and keep a count of how often each word is used
    d = {}
    for word in new_words: 
        # Check if the word is already in dictionary 
        if word in d: 
            # Increment count of word by 1 
            d[word] = d[word] + 1
        else: 
            # Add the word to dictionary with count 1 
            d[word] = 1
  
# Print the contents of dictionary 
    for key in list(d.keys()): 
        print(key, ":", d[key]) 

    
        


if __name__ == "__main__": # this is for calling file name 
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.') 
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
