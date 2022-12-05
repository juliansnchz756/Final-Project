# Function opens txt file of users choice through input if txt file does not exist File not found is printed
def open_file(): 
    while True:
        filename = input('\nType file name: ')
        try:
            file = open(filename, 'r', encoding = 'utf-8').readlines()
            print('\nFile found.\n')
            break
        except:
            print('\nFile not found.\n')
    return file

# function creates dictionary and reads txt file from open_file() while giving each line a number 
def read_data(fp):
    file = [line.lower().split(' ') for line in fp]
    data_dict = {}
    for (ind1, line) in enumerate(file):
        for word in line:
            if word.isalpha() == True and len(word) > 1:
                try:
                    data_dict[word].add(ind1 + 1)
                except:
                    data_dict[word] = {ind1 + 1}
            else:
                new_word = ''
                for char in word:
                    if char.isalpha() == True:
                        new_word += char
                if len(new_word) > 1:
                    try:
                        data_dict[new_word].add(ind1 + 1)
                    except:
                        data_dict[new_word] = {ind1 + 1}
    return data_dict

# function takes input string and searches for cooccurances
def find_cooccurance(D, inp_str):
    inp_lst = inp_str.split(' ')
    for (ind, word) in enumerate(inp_lst):
        if word.isalpha == True:
            pass
        else:
            new_word = ''
            for char in word:
                if char.isalpha() == True:
                        new_word += char
            inp_lst[ind] = new_word
    
    if all(i in D.keys() for i in inp_lst):
        out = D[inp_lst[0]]
        for i in inp_lst[1:]:
            out = set(sorted(out.intersection(D[i])))
        if len(out) == 0:
            out = ' None '
        print('\nCo-occurance for ('+inp_str.replace(' ', ', ')+'): \n\tLines: '+str(out)[1:-1]+'\n')
    else:
        print('\nOne or more of the words inputted did not appear in the document.\n')
        
# function calls out other fuctions which return there task.
def main():
    file = open_file()
    data = read_data(file)
    while True:
        inp = input('Type query words: ').lower()
        if inp == 'q':
            print('\nQuitting...\n')
            return
        find_cooccurance(data, inp)
        
#run main function first which then calls on the previous functions
if __name__ == "__main__":
    main()