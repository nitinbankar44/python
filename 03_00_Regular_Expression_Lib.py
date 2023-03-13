#Regular Expression Liabrary
#the functions in this module let you check 
#if a particular string matches a given regular expression 
# (or if a given regular expression matches a particular string,
#  which comes down to the same thing).
import re
class RegularExpression():
    def __init__(self,mystring) -> None:
        self.myString = mystring
    def findalloccurance(self,txt):
        return re.findall(txt,self.myString)  #Return list of occurances of respctive work or char      
    def separateWords(self):
        return re.split("\s",self.myString)  #returns list of words which separeted my whitespaces
    def subfunction(self):
        return re.sub("\s","9",self.myString)
sampleTxt = "Nitin Shyamsundar Bankar"
regEx = RegularExpression(sampleTxt)
print(regEx.findalloccurance("Nitin"))
print(regEx.separateWords())
print(regEx.subfunction())