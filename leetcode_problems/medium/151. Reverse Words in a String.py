class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        myString = s.split()
        listString = []
        for x in range(len(myString)-1,-1,-1):
            listString.append(myString[x])
        
        res = ' '.join(listString) 
        return res
