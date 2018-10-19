from pythainlp.tokenize import dict_word_tokenize,create_custom_dict_trie
data=create_custom_dict_trie("wordlist.txt")
while True:
 text=input("text : ")
 print(dict_word_tokenize(text,custom_dict_trie=data, engine="newmm")
 print("\r\n")
