# 파일 입출력
# 상대경로
# . 현재위치 c:/test
# .. c 
#  파일 쓰기
# f = open("./test.txt",'w')
# f.write("hi")
# f.close()


# 파일 읽기

# f = open("./test.txt","r")
# lines = f.readlines()
# for line in lines :
#     print(line)


# f= open("./test.txt",'w')
# f.write("print('hi')")
# f.write("hi1\n")
# # f.write("\n")
# f.write("\n")
# f.write("\tbye1")
# f.close()
# def open(filename, type):





# fr = open("./8888.txt","r",encoding="UTF-8")
# lines =fr.readlines() # lines =  [""]
# fr.close() 

# fw = open("./8888.txt","w",encoding="UTF-8")
# for line in lines:
#     update_text = input(f"전 문장 : {line}\n 바꿀문장(취소는 c):\t")
#     if update_text == "c" :
#         fw.write(line.strip())
#     else :
#         fw.write(update_text)
#     fw.write("\n")
# fw.close()

# fw = open("./test.txt","w")
# for line in lines:
#     if line == "hi" :
#         fw.write("ML")
#     elif line == "ex":
#         fw.write("as")
#     else :
#         fw.write(line)
# fw.close()



fr = open("./8888.txt","r",encoding= "UTF-8")
lines = fr.readlines()
fr.close()

fw = open("./8888.txt","w",encoding= "UTF-8")
for line in lines :
    update_text = input(f"전 문장 : {line} \n 바꿀 문장 (취소는 c):")
    if update_text == "c":
        fw.write(line.strip())
    else:
        fw.write(update_text)
    fw.write("\n")
fw.close()

