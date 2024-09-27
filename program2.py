def decode_message( s: str, p: str) -> bool:

 # write your code here
  def match_star(i,j):
        while i<len(s):
            if decode_message(s[i:],p[j+1:]):
                return True
            i+=1
        return decode_message(s[i:],p[j+1:])
  i=j=0
  while i<len(s) and len(p):
        if p[j] == '?':
            i += 1
            j += 1
        elif p[j] == '*':
            return match_star(i,j)
        elif p[j] == s[i]:
            i += 1
            j += 1
        else:
            return False
  if j < len(p) and p[j] == '*':
        return True
  return i == len(s) and j == len(p)
print(decode_message("aa" , "a*"))
print(decode_message("ab","a?"))  
print(decode_message("ab","a*"))  
print(decode_message("abc","a*c"))    
