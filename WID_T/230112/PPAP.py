# PPAP,PPAPPAP,PPPAPAP,
#

# 문자열을 지나가면서 확인을 어떻게??? # 문자열을 뒤에서부터 잘라주자 ppap일경우 p로 반환시키기
# FOR문으로 흠,, 인덱스번호를 넘긴다?

words = input()
words = list(words)
del_list = []
check = 0
while len(words) > 5:
    print(1)
    check = 0
    for i in range(len(words), -1, -1):
        if i < 2 and words[i] == "A":
            print("NP", "강종")
            exit()
        if words[i] == "A":  # for문 중간에 포문을 변경하게된다면 ? 오류발생 흠 ,,  4개 인덱스를 1개 인덱스로 변경
            if (words[i - 1], words[i - 2], words[i + 1]) == ("P", "P", "P"):
                del_list.append(i)
                del_list.append(i - 1)
                del_list.append(i - 2)
                check = 1
            print("A찾음")
        # try:
        # for j in del_list:
        del del_list
        del_list.clear()
        print(words)
        # except:
        #     break

k = "".join(words)
if "PPAP" == k or "P" == k:
    print("PPAP")
else:
    print("NP")
