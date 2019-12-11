# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

# M は立候補者の人数を、N は有権者の人数を、K は演説が行われる回数を表します
m_in, n_in, k_in = input().split()
m = int(m_in)
n = int(n_in)
k = int(k_in)
# supporter[i] は候補者iの支持者の数
supporter = list()
for i in range(m):
    supporter.append(0)
# process of speech
for i in range(k):
    speaker = int(input()) - 1
    # for all candidates
    for j in range(m):
        # except the specific one and who has more than 0 supporters
        if speaker != j and supporter[j] > 0:
            # decrease es number of supporters by 1
            supporter[j] = supporter[j] - 1
            # and increase the num of the supporters of the specific candidate
            supporter[speaker] = supporter[speaker] + 1
    # if there are more than 0 free supporters
    if n > 0:
        # decrease 1 free
        n = n - 1
        # and increase the num of supporters of the specific speaker
        supporter[speaker] = supporter[speaker] + 1
# suppose the candidate 0 has the biggest number of supporters
highest = supporter[0]
# change the highest if the supporter 0 and others has
for i in range(1, m):
    if supporter[i] > highest:
        highest = supporter[i]
# retrieve the candidate who has the highest number of supporters
eligible = [i for i, x in enumerate(supporter) if x == highest]
# output
for e in eligible:
    print(e + 1)
