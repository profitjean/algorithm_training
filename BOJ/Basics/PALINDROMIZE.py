import sys


def reverse(s):
    ret = ''
    N = len(s)
    for i in range(N):
        ret += s[N-1-i]
    return ret


def generate_partial(s):
    N = len(s)
    ret = [0] * (N+1)
    begin, matched = 1, 0

    while begin + matched < N:
        if s[begin + matched] == s[matched]:
            matched += 1
            ret[begin+matched] = matched
        else:
            if matched == 0:
                begin += 1
            else:
                begin += matched - ret[matched]
                matched = ret[matched]
    return ret


def len_palindrome(s):
    rs = reverse(s)
    pi_rs = generate_partial(rs)
    N = len(s)
    begin = 0
    matched = 0
    rs_len = 0

    while begin + matched < N:
        if matched < N and s[begin + matched] == rs[matched]:
            matched += 1
            if begin + matched == N:
                rs_len = matched
                break
        else:
            if matched == 0:
                begin += 1
            else:
                begin += matched - pi_rs[matched]
                matched = pi_rs[matched]


case = int(sys.stdin.readline().rstrip())
ans = []
for _ in range(case):
    palindrome = sys.stdin.readline().rstrip()
    ans.append(len_palindrome(palindrome))
for n in ans:
    print(n)
