import string

DIGITS = '0123456789'
LETTERS = string.ascii_letters
LETTERS_DIGITS = LETTERS + DIGITS

f = open(r"Code.py", "r")

str = f.read()


i = 0
j = 0
k = 0
r = 0
p_if = -1
Array = ""
c_color = []


def reverse_str(str):
    f_str=""
    str_1 = str.replace(" ","").replace("\t","")
    for i in range(len(str_1)-1,-1,-1):
        f_str+=str_1[i]
    return f_str

def make_word():
    global i
    str_w = str[i]
    i+=1


    while str[i] in LETTERS_DIGITS + '_':
        str_w+=str[i]
        i+=1
        if i == len(str):
            return str_w
    i-=1
    return str_w

while i < len(str):
    curr_char = str[i]

    temp_idx = i-1
    temp_idx_2 = i+1
    if str[i] == "=" and str[i+1] != "=" and str[i-1] != "=" and str[i-1] !="!":   
        l_val = []
        r_val = []
        temp_str = ""
        temp_str_2 = ""
        while str[temp_idx] != "\n":
            if str[temp_idx] == ",":
                l_val.append(reverse_str(temp_str))
                temp_str = ""
                temp_idx-=1
            else:
                temp_str+=str[temp_idx]
                temp_idx-=1
        
        i = temp_idx

        while str[temp_idx_2] != "\n":
            temp_idx_2+=1
        temp_idx_2-=1

        while str[temp_idx_2] != "=":
            if str[temp_idx_2] == ",":
                r_val.append(reverse_str(temp_str_2))
                temp_str_2 = ""
                temp_idx_2-=1
            else:
                temp_str_2+=str[temp_idx_2]
                temp_idx_2-=1

        l_val.append(reverse_str(temp_str))
        r_val.append(reverse_str(temp_str_2))  

        i+=1
        g=""
        while str[i] == " ":
            i+=1
            g+=" "           
        for n in range(len(l_val)):
            m=l_val[n]
            if Array+"[" in m:
                m_str=m.replace(Array,"").replace("[","").replace("]","").replace(")","").replace("(","")
                str=str[:i] + "animations.append([2," + m_str+","+r_val[n].replace(")","").replace("(","") + "])\n" + g + str[i:]
                i+= 25+len(m_str)+len(r_val[n]) + len(g)
        
        while str[i]!= "\n":
            i+=1

    if k==1 and curr_char==":":
        if(len(c_color)!=0):
            temp = p_if
            p_if-=1
            p_gap=0
            ga_str =""
            temp_str=""
            while str[p_if] == " ":
                ga_str+=" "
                p_gap+=1
                p_if-=1
        
            for c_k in range(len(c_color)):
                if(c_k!=(len(c_color)-1)):
                    temp_str+=(c_color[c_k]+",")
                else:
                    temp_str+=c_color[c_k]

            str=str[:temp]+"animations.append([0,"+temp_str+"])\n" + ga_str + "" +"animations.append([1,"+temp_str+"])\n" +ga_str + str[temp:]
            i+=48+(len(ga_str)*2) + (2*len(temp_str))
            p_if=temp  
            c_color = []
        
        k-=1

    if j==3 and curr_char==":":
        i+=2
        g=""
        while str[i] ==" " or str[i] == "\n" :
            g+=str[i]
            i+=1
        str=str[:i] + "animations = []\n" + g + str[i:]
        i+= 16 + len(g)
        curr_char = str[i]
        j=0

    if curr_char in LETTERS:
        word = make_word()

        if r == 1 :
            if Array == word:

                temp=i+1
                i-=len(word)
                str=str[:i+1]+"animations"+str[temp:]
                i-=1
            r-=1

        if k == 1:
            if word == Array:
                if str[i+1] == "[":
                    i+=2
                    c_str = ""
                    while str[i] != "]":
                        c_str+=str[i]
                        i+=1
                    c_color.append(c_str)       

        if j==2:
            Array+=word
            
            j=3

        if j==1:
            j+=1

        if word == "def":
            j+=1
        
        if word == "if":
            k+=1
            p_if = i-1

        if word == "return":
            r+=1

    i+=1

print(str)


