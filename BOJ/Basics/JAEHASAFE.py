import sys

def search_kmp(h,n):
    h_len, n_len = len(h), len(n)
    begin, matched = 0, 0
    pos = []

    def partial_match(s):
        begin, matched = 1, 0
        ret = [0] * (n_len + 1)
        while begin + matched < n_len:
            if s[begin + matched] == s[matched]:
                matched += 1
                ret[begin + matched] = matched
            else:
                if matched == 0:
                    begin += 1
                else:
                    begin += matched - ret[matched]
                    matched = ret[matched]
        return ret

    pi = partial_match(n)
    while begin <= h_len - n_len:
        if matched < n_len and h[begin + matched] == n[matched]:
            matched += 1
            if matched == n_len:
                pos.append(begin)
        else:
            if matched == 0:
                begin += 1
            else:
                begin += matched - pi[matched]
                matched = pi[matched]
    return pos


def get_direction(s):
    answer = 0
    right = True
    for i in range(len(s)-1):
        if right:
            answer += search_kmp(s[i+1] * 2, s[i])[0]
        else:
            answer += search_kmp(s[i] * 2, states[i+1])[0]
    return answer

case = int(sys.stdin.readline().rstrip())
ans = []
for _ in range(case):
    states = []
    n = int(sys.stdin.readline().rstrip())
    for _ in range(n+1):
        states.append(sys.stdin.readline().rstrip())
    ans.append(get_direction(states))
for n in ans:
    print(n)
# getDirection 호출