def parse_data(text): #returns frequency distribution, bigram table, pos table, takes in tokenized text
    prev_token = ""
    f_bigrams = {}
    f_dist = {}
    pos = {}
    count = 0
    for token in text: # get counts
        count += 1
        if(token in f_dist):
            f_dist[token] += 1
        else:
            f_dist[token] = 1
        if(prev_token != ""):
            if(prev_token in f_bigrams):
                if(token in f_bigrams[prev_token]):
                    f_bigrams[prev_token][token] += 1
                else:
                    f_bigrams[prev_token][token] = 1
            else:
                f_bigrams[prev_token] = {token: 1}
        prev_token = token
    #normalize
    p_dist = {}
    p_bigrams = {}
    for token in text:
        p_dist[token] = f_dist[token]/float(count)
        bigram_norm = 0
        p_bigrams[token] = {}
        for key in f_bigrams[token]:
            p_bigrams[token][key] = f_bigrams[token][key]/float(f_dist[token])
    return (f_dist, f_bigrams, p_dist, p_bigrams)
