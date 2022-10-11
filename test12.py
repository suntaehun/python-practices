fr = open("./888.txt","r",encoding ="UTF-8")
lines = fr.readlines()
fr.close()

fw = open("./888.txt","w",encoding ="UTF-8")
for line in lines :
    update_text = input(f"전 문장 : {line} 바꿀 문장(c는 취소) :\t")
    if update_text == 'c':
        fw.write(line.strip())
    else :
        fw.write(update_text)
    fw.write("\n")
fw.close()