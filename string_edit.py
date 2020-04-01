import jieba
import logging

# text1 -> text2
def string_edit(text1, text2):
    
    h = len(text1)+1
    r = len(text2)+1
    match_count = 0
    # store the accumulated operations
    dp = [[[] for _ in range(r)] for _ in range(h)]

    for i in range(h):
        for j in range(r):
            if i == 0 and j == 0:
                dp[i][j] = []
            elif i == 0 and j != 0:
                # insertion
                for c in text2[:j]: dp[i][j].append(('i',c))
            elif j == 0 and i != 0:
                # deletion
                for c in text1[:i]: dp[i][j].append(('d',c))
            elif text1[i-1] == text2[j-1]:
                # do nothing, match
                dp[i][j] = dp[i-1][j-1]
                match_count += 1
            else:
                deletion = dp[i-1][j] + [('d', text1[i-1])]
                insertion = dp[i][j-1] + [('i', text2[j-1])]
                replacement = dp[i-1][j-1] + [('r', text1[i-1] + "->" + text2[j-1])]
                
                operation = sorted([deletion, insertion, replacement], key=len)
                dp[i][j] = operation[0]
    
    res = { "match_cnt": match_count, 
            "operations":dp[-1][-1] }

    return res

def alignment_report(res, scores, hypothsis, reference):
    
    score, i_cnt, d_cnt, r_cnt = 0, 0, 0, 0

    match_cnt = res["match_cnt"]
    operations = res["operations"]
    # alignment score, i_cnt, d_cnt, r_cnt
    score += (match_cnt*scores['m'])
    for operation in operations:
        op = operation[0]
        score += scores[op] 
        if op == 'i': i_cnt += 1
        if op == 'd': d_cnt += 1
        if op == 'r': r_cnt += 1
    # error rate
    top_score = len(reference)*scores['m']
    error_rate = (1-(score/top_score))*100
    ops_str = ["("+op[0]+")"+op[1] for op in operations]
    # print report
    print("%12s:%s" % ("HYPOTHSIS", ','.join(hypothsis)))
    print("%12s:%s" % ("REFERENCE", ','.join(reference)))
    print("%12s:%.2f %s" % ("ERROR RATE",error_rate,'%'))
    print("%12s:%d" % ("MATCH", match_cnt))
    print("%12s:%d" % ("INSRTION", i_cnt))
    print("%12s:%d" % ("DELETION", d_cnt))
    print("%12s:%d" % ("REPALCEMENT", r_cnt))
    print("%12s:%d" % ("ALIGN_SCORE", r_cnt))
    print("%12s:%s" % ("OPERATIONS", ",".join(ops_str)))

def main():
    jieba.setLogLevel(logging.INFO)
    hypothsis = "今天心情很好想出門啦!"
    reference = "天氣很好就該出門吧"
    hs = [w for w in jieba.cut(hypothsis)]
    rf = [w for w in jieba.cut(reference)]
    scores = {'m':5, 'i':-2, 'd':-2, 'r': -1}
    res = string_edit(hs, rf)
    alignment_report(res, scores, hs, rf)

if __name__ == '__main__':
    main()

