def words(string):
    word_list = string.split()
    count ={}
    for word in word_list:
        try:
            if (int(word) in count):
                count[int(word)]+=1
            else:
              count[int(word)]=1
        except ValueError:
            if word in count:
                count[word]+=1
            else:
                count[word]=1
    return count

        
