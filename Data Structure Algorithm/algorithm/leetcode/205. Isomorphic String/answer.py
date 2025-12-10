class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n=len(s)
        map_store={}
        map_cont=set()
        for i in range(n):
            if s[i] in map_store:
                if map_store[s[i]]==t[i]:
                    continue
                else:
                   return False
            else:
                if t[i] in map_cont:
                    return False
                map_store[s[i]]=t[i]
                map_cont.add(t[i])

        return True