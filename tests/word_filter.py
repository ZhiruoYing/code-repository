"""
Word Filter and Counter Function

Objective:
Write a function named 'word_filter_counter' that filters and counts specific words in a given text.

Function Parameters:
1. text (string): The text from which words will be filtered and counted.
2. filter_words (list of strings): A list of words to be filtered out from the text.

Instructions:
- The function should filter out the words from the text that are present in the filter_words list. The comparison should be case-insensitive.
- The function should return a dictionary. In this dictionary, the keys are the filtered words, and the values are the counts of how often these words appeared in the text.
- The text may contain punctuation marks and spaces. Only whole words, separated by spaces or punctuation, should be considered.

Example Test Cases:
1. word_filter_counter("Hello world, hello!", ["hello"]) should return a dictionary with the count of occurrences of "hello".
2. word_filter_counter("The quick brown fox.", ["the"]) should return a dictionary with the count of occurrences of "the".
3. word_filter_counter("Is this real life? Is this just fantasy?", ["is", "this", "just"]) should return a dictionary with the counts of occurrences of "is", "this", and "just".
4. word_filter_counter("Do we see the big picture or just small details?", ["we", "the", "or"]) should return a dictionary with the counts of occurrences of "we", "the", and "or".
"""
#text.split(以什么作为标志分割,分割几次)
#text.replece(替换前,替换后)

def word_filter_counter(text, filter_words):
    dic_count={}
    for i in ",.?!":
        text=text.replace(i," ")
    
    text=text.lower()
    word_list=text.split()#变成一个list

    for w in filter_words:#啊啊啊啊这里需要在fliter_words中遍历，如果在text中遍历就是计算整个text中每个单词的数量了啊
        c=word_list.count(w.lower())#这里就是需要把filter_words全部变成小写，和上面的对应
        if c >0: #首先这个单词要存在
             dic_count[w]=c
        else:
            return "not exsiting"
    return dic_count


    # Your code goes h
    # Implement the logic to filter words and count their occurrences
    pass  # Delete this after implementing some code inside this function
#filter_words里面应该用到的是元素的计算，那就是先把整个句子做成一个字典。然后遇到不是单词的内容，就换下一个。
#先把句子里面的单词提取出来

# Test cases
print(
    word_filter_counter("Hello world, hello!", ["hello"])
)  # Expected output: {'hello': 2}
print(
    word_filter_counter("The quick brown fox.", ["the"])
)  # Expected output: {'the': 1}
print(
    word_filter_counter(
        "Is this real life? Is this just fantasy?", ["is", "this", "just"]
    )
)  # Expected output: {'is': 2, 'this': 2, 'just': 1}
print(
    word_filter_counter(
        "Do we see the big picture or just small details?", ["we", "the", "or"]
    )
)  # Expected output: {'we': 1, 'the': 1, 'or': 1}
