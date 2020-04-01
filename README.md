# ALIGMNET TOOL

> To get hypothsis string of insertion, deletion, replacement to reference string

## Process
- Chinese Word Segmentation: Jieba
- Damerau-Levenshtein Distance : String Edit Algorithm
- Alignment Score: Can define your own socre of each operation: insertion, deletion, replacement
- Error Rate: (Top Alignment Score - Alignment Socre)/Top Alignment Score

## Result
```
HYPOTHSIS:今天,心情,很,好,想,出門,啦,!
   REFERENCE:天氣,很,好,就,該,出門,吧
  ERROR RATE:57.14 %
       MATCH:3
    INSRTION:1
    DELETION:2
 REPALCEMENT:3
 ALIGN_SCORE:3
  OPERATIONS:(r)今天->天氣,(d)心情,(r)想->就,(i)該,(r)啦->吧,(d)!
```
