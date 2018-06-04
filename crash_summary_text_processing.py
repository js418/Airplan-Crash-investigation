# COMPSCI 590V - Data Visualization & Exploration
# Final Project
# Jie Song
# 30272759
# text processing for word cloud

import csv
import re
from collections import Counter,OrderedDict

def writefile(c,f):
    c_counts = Counter(c)
    c_m = OrderedDict(c_counts.most_common())
    #print len(c)
    #print len(c_counts)
    out_file_c = open(f, "wb")
    w_c = csv.writer(out_file_c)
    w_c.writerow(["text","size"])
    for t in c_m:
        w_c.writerow([t,c_counts[t]])
    out_file_c.close

def main():

    stopwords = ["","a","u","s","e","about", "above", "above", "across", "after", "afterwards", "again", "against", "all", "almost", "alone", "along", "already", "also","although","always","am","among", "amongst", "amoungst", "amount",  "an", "and", "another", "any","anyhow","anyone","anything","anyway", "anywhere", "are", "around", "as",  "at", "back","be","became", "because","become","becomes", "becoming", "been", "before", "beforehand", "behind", "being", "below", "beside", "besides", "between", "beyond", "bill", "both", "bottom","but", "by", "call", "can", "cannot", "cant", "co", "con", "could", "couldnt", "cry", "de", "describe", "detail", "do", "done", "down", "due", "during", "each", "eg", "eight", "either", "eleven","else", "elsewhere", "empty", "enough", "etc", "even", "ever", "every", "everyone", "everything", "everywhere", "except", "few", "fifteen", "fify", "fill", "find", "fire", "first", "five", "for", "former", "formerly", "forty", "found", "four", "from", "front", "full", "further", "get", "give", "go", "had", "has", "hasnt", "have", "he", "hence", "her", "here", "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "him", "himself", "his", "how", "however", "hundred", "ie", "if", "in", "inc", "indeed", "interest", "into", "is", "it", "its", "itself", "keep", "last", "latter", "latterly", "least", "less", "ltd", "made", "many", "may", "me", "meanwhile", "might", "mill", "mine", "more", "moreover", "most", "mostly", "move", "much", "must", "my", "myself", "name", "namely", "neither", "never", "nevertheless", "next", "nine", "no", "nobody", "none", "noone", "nor", "not", "nothing", "now", "nowhere", "of", "off", "often", "on", "once", "one", "only", "onto", "or", "other", "others", "otherwise", "our", "ours", "ourselves", "out", "over", "own","part", "per", "perhaps", "please", "put", "rather", "re", "same", "see", "seem", "seemed", "seeming", "seems", "serious", "several", "she", "should", "show", "side", "since", "sincere", "six", "sixty", "so", "some", "somehow", "someone", "something", "sometime", "sometimes", "somewhere", "still", "such", "system", "take", "ten", "than", "that", "the", "their", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "therefore", "therein", "thereupon", "these", "they", "thickv", "thin", "third", "this", "those", "though", "three", "through", "throughout", "thru", "thus", "to", "together", "too", "top", "toward", "towards", "twelve", "twenty", "two", "un", "under", "until", "up", "upon", "us", "very", "via", "was", "we", "well", "were", "what", "whatever", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "whereupon", "wherever", "whether", "which", "while", "whither", "who", "whoever", "whole", "whom", "whose", "why", "will", "with", "within", "without", "would", "yet", "you", "your", "yours", "yourself", "yourselves", "the"]

    country = ["United States", "Russia", "Brazil", "Canada", "Colombia", "China", "France", "England", "India", "Indonesia"]

    manu = ["Douglas","Boeing","Antonov","Cessna","de Havilland Canada  Twin Otter"]
    
    in_file = open("clean_data.csv", "rb")
    reader = csv.reader(in_file)
    line = list(reader)
    in_file.close

    c = []
    p = []
    m = []
    
    us = []
    ru = []
    br = []
    ca = []
    co = []
    ch = []
    fr = []
    en = []
    ind = []
    indo = []

    do = []
    bo = []
    an = []
    ce = []
    de = []
    for i in range(1,len(line)):
        s = re.split("[^a-zA-Z]",line[i][10])
        
        if line[i][3] == country[0]:
            for word in s:
                if word not in stopwords:
                    us.append(word)
        if line[i][3] == country[1]:
            for word in s:
                if word not in stopwords:
                    ru.append(word)
        if line[i][3] == country[2]:
            for word in s:
                if word not in stopwords:
                    br.append(word)
        if line[i][3] == country[3]:
            for word in s:
                if word not in stopwords:
                    ca.append(word)
        if line[i][3] == country[4]:
            for word in s:
                if word not in stopwords:
                    co.append(word)
        if line[i][3] == country[5]:
            for word in s:
                if word not in stopwords:
                    ch.append(word)
        if line[i][3] == country[6]:
            for word in s:
                if word not in stopwords:
                    fr.append(word)
        if line[i][3] == country[7]:
            for word in s:
                if word not in stopwords:
                    en.append(word)
        if line[i][3] == country[8]:
            for word in s:
                if word not in stopwords:
                    ind.append(word)
        if line[i][3] == country[9]:
            for word in s:
                if word not in stopwords:
                    indo.append(word)

        if line[i][7] == manu[0]:
            for word in s:
                if word not in stopwords:
                    do.append(word)
        if line[i][7] == manu[1]:
            for word in s:
                if word not in stopwords:
                    bo.append(word)
        if line[i][7] == manu[2]:
            for word in s:
                if word not in stopwords:
                    an.append(word)
        if line[i][7] == manu[3]:
            for word in s:
                if word not in stopwords:
                    ce.append(word)
        if line[i][7] == manu[4]:
            for word in s:
                if word not in stopwords:
                    de.append(word) 
        
        if line[i][11] == "Military":
            for word in s:
                if word not in stopwords:
                    m.append(word)
        elif line[i][11] == "Passenger":
            for word in s:
                if word not in stopwords:
                    p.append(word)
        elif line[i][11] == "Cargo/Service":
            for word in s:
                if word not in stopwords:
                    c.append(word)
        
    writefile(us,"us.csv")
    writefile(ru,"russia.csv")
    writefile(br,"brazil.csv")
    writefile(ca,"canada.csv")
    writefile(co,"colombia.csv")
    writefile(ch,"china.csv")
    writefile(fr,"france.csv")
    writefile(en,"england.csv")
    writefile(ind,"india.csv")
    writefile(indo,"indonesia.csv")

    writefile(do,"do.csv")
    writefile(bo,"bo.csv")
    writefile(an,"an.csv")
    writefile(ce,"ce.csv")
    writefile(de,"de.csv")
    
    writefile(c,"cargo_service_word_cloud.csv")
    writefile(p,"passenger_word_cloud.csv")
    writefile(m,"military_word_cloud.csv")

    c_c = Counter(c)
    p_c = Counter(p)
    m_c = Counter(m)
    a = c_c + p_c + m_c
    a_m = OrderedDict(a.most_common())
    out_file_a = open("all_word_cloud.csv", "wb")
    w_a = csv.writer(out_file_a)
    w_a.writerow(["text","size"])
    for t in a_m:
        w_a.writerow([t,a[t]])
    out_file_a.close

    
    
    

    

    
        
        
main()
