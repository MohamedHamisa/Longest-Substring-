from collections import Counter
class Solution:
    def longestSubstring(self, s, k):
        ctr = Counter(s)
        for c,v in ctr.items():
            if v<k:
                return max([self.longestSubstring(sub, k) for sub in s.split(c) if len(sub)>=k] or [0])
        return len(s)

'''
If every character appears at least k times, the whole string is ok. Otherwise split by a least frequent character 
(because it will always be too infrequent and thus can't be part of any ok substring) and make the most out of the splits.
'''
