def collect_and_join_words():
    # მიღება რამდენი სიტყვა სურს მომხმარებელს
    num_of_words = int(input("რამდენი სიტყვა გსურთ: "))
    
    words = []
    
    # სთხოვეთ მომხმარებელს, რომ თითოეული სიტყვა შეყაროს
    for i in range(num_of_words):
        word = input(f"შეიყვანეთ სიტყვა {i+1}: ")
        words.append(word)
    
    # სიტყვების ჯოინი
    result = ' '.join(words)
    
    # გამოსახვა ტერმინალში
    print(f"შედეგი: {result}")

# გამოძახება ფუნქციის
collect_and_join_words()
