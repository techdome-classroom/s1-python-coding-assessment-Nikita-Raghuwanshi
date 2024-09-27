def decode_message( s: str, p: str) -> bool:

# write your code here
  def match_star(i,j):
        while i<len(s):
            if decode_message(s[i],p[j+1]):
                return True
            i+=1
  
        return False