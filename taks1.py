from itertools import count 
OUTPUT = 'summary.txt'
WRITE_MODE = 'w'
FILENAME = 'remarks.txt'
READ_MODE = 'r'

with open(OUTPUT, WRITE_MODE) as output:
    try:

        def words_count(string):
            words = string.split()
            count = len(words)
            output.write(f'Total words count: {count}\n')
        
        def char_count(string):
            total_char = 0
            for i in string:
                total_char = total_char + 1
            output.write(f"Total Characters count: {total_char}\n")
        
        def avg_word_length(string):
            filtered = ''.join(filter(lambda x: x not in '".,;!-', string)) 
            words = [word for word in filtered.split() if word]
            avg = sum(map(len, words))/len(words)
            output.write(f"The average word length is: {avg:0.1f}\n")

        def avg_sent_length(string):
            sents = string.split('.')
            avg_sents_len = sum(len(x.split()) for x in sents) / len(sents)
            output.write(f"The average sentense length is: {avg_sents_len:0.1f}\n")
        di = {}
        def count_words_endinly(string):
            for word in string.split():
                if word.endswith("ly") == True:
                    if word in di:
                        di[word]+=1
                    else:
                        di[word]=1
                    string = string.replace(word,'')

        def longwords(l, x):
            c = count()
            return sorted(l, key=lambda i: (len(i), next(c)),
                  reverse=True)[:x]

    except:
        output.write(f'Unexpected exception, blame its developer.\n')

    with open(FILENAME, READ_MODE) as input:
        data = input.read()
        result1 = words_count(data)
        result2 = char_count(data)
        result3 = avg_word_length(data)
        result4 = avg_sent_length(data)
        result5 = count_words_endinly(data)
        output.write("A word distribution of all words ending in 'ly'\n")
        for i in di:
            output.write(f'{i} {di[i]} \n')
        output.write("A list of top 10 longest words in descending order:\n")
        K = 10
        string_to_list = list(data.split())
        output.write(f'{longwords(string_to_list, K)}')
        


            

    
