def solution(info, query):
    answer = []
    
    infos = []
    queries = []

    for i in info:
        infos.append(i.split())
        infos[-1][-1] = int(infos[-1][-1])
        
    for q in query:
        queries.append(q.split(" and ")[:-1])
        queries[-1].append(q.split(" ")[-2])
        queries[-1].append(int(q.split(" ")[-1]))
    
    for i in range(len(queries)):
        query = queries[i]
        cnt = 0
        for j in range(len(infos)):
            check = True
            info = infos[j]

            for k in range(len(query) - 1):
                if query[-1] > info[-1]:
                    check = False
                    break
                if query[k] == '-' or query[k] == info[k]:
                    continue
                else:
                    check = False
                    break

            if check:
                cnt += 1
                
        answer.append(cnt)
        
    return answer
