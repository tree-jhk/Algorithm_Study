def solution(genres, plays):
    answer = []
    g = {}  # 장르별 재생 횟수와 인덱스 저장할 딕셔너리
    cnt = {}    # 장르별 총 재생 횟수를 저장할 딕셔너리
    
    # 각 장르의 재생 횟수와 몇 번째인지 인덱스 g 딕셔너리에 저장
    # 장르 총합도 cnt 딕셔너리에 저장
    for i, genre in enumerate(genres):
        if genre in g:
            g[genre].append([plays[i], i])
            cnt[genre] += plays[i]
        else:
            g[genre] = [[plays[i], i]]
            cnt[genre] = plays[i]
    
    # g 딕셔너리 정렬  # 2, 3번 조건
    for key, value in g.items():
        value.sort(key=lambda x: (-x[0], x[1]))

    # cnt 딕셔너리 정렬  # 1번 조건
    cnt = dict(sorted(cnt.items(), key=lambda x: -x[1]))
    
    # 1번 조건으로 재생 횟수 많은 장르부터 노래 수록
    for key, value in cnt.items():
        # 두 개씩 수록해야하므로 2번까지 수록
        for play, idx in g[key][:2]:
            answer.append(idx)
    
    return answer