# Hands-on 2

### What is it?
In Hands-on 2, we write three different kinds of code to select sentences with "可以"(ke yi) from corpus.  
Data from corpus: [中央研究院現代漢語平衡語料庫](https://asbc.iis.sinica.edu.tw/)

Generally, these three versions demonstrate how we processed the raw data by eliminating "more", "\n", and "\t" within the sentences. Basically, we employed the regular expression to create several patterns to split every sentences.


### Content
```
Main
|   ke_yi_raw.txt
|   README.md
|   
+---output
|       ke_yi_new_list.txt
|       ke_yi_processed.txt
|       Re.txt
|       
\---ways to extract ke_yi
        cotask1.py
        em_attempt.py
        extractor_em.py
        revised.py
        
        
