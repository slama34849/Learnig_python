def Check_Vow(my_string, vowels): 
    final = [each for each in my_string if each in vowels] 
    return final


def consonents(s):
   s = s.replace('a', "")
   s = s.replace("e", "")
   s = s.replace("i", "")
   s = s.replace("o", "")
   s = s.replace("u", "")
   return s


my_string = 'hackerrank' 
vowels = 'aeiou'
vo = Check_Vow(my_string, vowels)
print("".join(vo))
print(consonents(my_string))

