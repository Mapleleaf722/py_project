d_table = ["A","B","C","D","E","F",
           "G","H","I","J","K","L",
           "M","N","O","P",'Q','R',
           'S','T','U','V','W','X',
           'Y','Z','1','2','3','4',
           '5','6','7','8','9','0']
c_table=[".-",'-...','-.-.','-..','.','..-.',
         '--.','....','..','.---','-.-','.-..',
         '--','-.','---','.--.','--.-','.-.',
         '...','-','..-','...-','.--','-..-',
         '-.--','--..','.----','..---','...--','....-',
         '.....','-....','--...','---..','----.','-----']
#code=input("请输入摩斯电码：")
#split_code=code.split(" ")
#result=[d_table[c_table.index(each)] for each in split_code]
#print(result)
def cmorse(key,value):
    return(key,value)
morseCode=dict(map(cmorse,d_table,c_table))
print(morseCode)

               
