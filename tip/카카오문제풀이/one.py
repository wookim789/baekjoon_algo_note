def solution(info, query):
    info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
    query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
    answer = []

    lang_list = ["cpp", "java", "python"]
    bf_list = ["backend", "frontend"]
    js_list = ["junior", "senior"]
    pc_list = ["pizza", "chicken"]

    l_g = dict()
    for lang in lang_list :
        b_f = dict()
        for bf in bf_list:
            j_s = dict()
            for js in js_list:
                p_c = dict()
                for pc in pc_list:
                    p_c[pc] = []
                j_s[js] = p_c
            b_f[bf] = j_s
        l_g[lang] = b_f
    
    for st in info:
        temp_list = st.split()
        l_g[temp_list[0]][temp_list[1]][temp_list[2]][temp_list[3]].append(int(temp_list[4]))
    
    for q in query :
        q = q.replace('and', '')
        q_arr = q.split()
        count = 0

        l_arr = None
        if q_arr[0] == '-':
            l_arr = lang_list
        else:
            l_arr = [q_arr[0]]
        
        bf_arr = None
        if q_arr[1] == '-':
            bf_arr = bf_list
        else:
            bf_arr = [q_arr[1]]
        
        js_arr = None
        if q_arr[2] == '-':
            js_arr = js_list
        else:
            js_arr = [q_arr[2]]

        pc_arr = None
        if q_arr[3] == '-':
            pc_arr = pc_list
        else:
            pc_arr = [q_arr[3]]
        

        for l in l_arr:
            for bf in bf_arr:
                for js in js_arr:
                    for pc in pc_arr:
                        print()
                        print(l, bf, js, pc)
                        print(l_g[l][bf][js])
                        print(q_arr)
                        for score in l_g[l][bf][js][pc]:
                            if score >= int(q_arr[4]):
                                count += 1
                        
        answer.append(count)
    print(answer)
solution('','')