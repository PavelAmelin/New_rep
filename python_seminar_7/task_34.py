def rhythm(st):
    lst, res = st.split(), []
    for phrase in lst:
        cnt = 0
        for let in phrase:
            if let in 'аеоуиёяюыэ':
                cnt += 1
        res.append(cnt)
    if len(set(res)) == 1:
        return 'Парам пам-пам'
    else:
        return 'Пам парам'

print(rhythm('пара-ра-рам рам-пам-папам па-ра-па-да'))