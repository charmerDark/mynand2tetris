import sys

#Reading name of hack file from commmandline arguement and fetching file
file_name=sys.argv[1]
file_reader=open(file_name, 'r')
if file_reader.mode=='r':
    content=file_reader.readlines()
file_reader.close()
######################cleaning all whitespaces and comments from code#################
    #removing newlines
for line in content:
    if line=="\n":
        content.remove(line)
 #removing comments and whitespaces from remaining lines
for line in content:
    comm_pos=line.find("//")
    if comm_pos!=-1:
        content[content.index(line)]=line[0:comm_pos]
#Deleting empty list elements and removing newline to make instruction only.
content=[ele.replace('\n','') for ele in content if ele!=""]
content=[ele.strip() for ele in content if ele!=""]
##################symbol table predefined symbols################
symb_table={'R0':0,'R1':1,'R2':2,'R3':3,'R4':4,"R5":5,"R6":6,'R7':7,"R8":8,"R9":9,"R10":10,"R11":11,"R12":12,"R13":13,"R14":14,"R15":15,"SCREEN":16384,"KBD":24576,"SP":0,"LCL":1,"ARG":2,"THIS":3,"THAT":4}
###############Firstpass and initialization of symbol table############
n=-1
for line in content:
    n+=1
    if line[0]=="(":
        ky=line[1:-1]
        if ky not in symb_table.keys():
            symb_table[ky]=n
            n-=1
content=[line for line in content if line[0]!="("]
"""Tested and verified upto here"""
########################Second Pass and  code generation ##########################
destin={"M":'001',"D":'010',"MD":'011',"A":'100',"AM":'101',"AD":'110','AMD':'111'}
comput={"0":"0101010","1":"0111111","-1":"0111010","A":"0110000","M":"1110000","D":"0001100","!D":"0001101","!A":"0110001","!M":"1110001","-D":"0001111","-A":"0110011","-M":"1110011","D+1":"0011111","A+1":"0110111","M+1":"1110111","D-1":"0001110","A-1":"0110010","M-1":"1110010","D+A":"0000010","D+M":"1000010","D-A":"0010011","D-M":"1010011","A-D":"0000111","M-D":"1000111","D&A":"0000000","D&M":"1000000","D|A":"0010101","D|M":"1010101"}
jmp={"JGT":"001","JEQ":"010","JGE":"011","JLT":"100","JNE":"101","JLE":"110","JMP":"111"}
codes=[]
n=16
for line in content:
    if line[0]=="@":                #####if it is an A- instruction
        location=line[1:]
        if location in symb_table.keys():
            codes.append("{:016b}".format(symb_table[location]))
        elif location.isdigit():
            codes.append("{:016b}".format(int(location)))
        else:
            if location not in symb_table.keys():
                symb_table[location]=n
                n+=1
                codes.append("{:016b}".format(symb_table[location]))
            else:
                codes.append("{:016b}".format(symb_table[location]))
    else:
        dest=line.find("=")
        comp=line.find(";")
        if comp==-1:                                    #############If it is an instuction of the form dest=comp
            code="111"+comput[line[dest+1:]]+destin[line[0:dest]]+"000"
        elif dest==-1:
            code="111"+comput[line[0:comp]]+"000"+jmp[line[comp+1:]]
        else:
            code="111"+comput[line[dest+1:comp]]+destin[line[0:dest]]+jmp[line[comp+1:]]
        codes.append(code)
########################Writing Assembly code to new file#####################
codes=[line+"\n" for line in codes ]
file_name=file_name[:-3]+"hack"
file_reader=open(file_name, 'w')
for line in codes:
    file_reader.write(line)
file_reader.close
print("File written in ",file_name)
