class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
            ans = {}
            for word in strs:
                sort_word = ''.join(sorted(word))
                if sort_word in ans.keys():
                    ans[sort_word].append(word)
                else:
                    ans[sort_word] = [word]
                # print(ans)
            return ans.values()
            
            hashmap = {}
            for str_ in strs:
                tmp = ''.join(sorted(str_))
                if tmp in hashmap:
                    hashmap[tmp].append(str_)
                else:
                    hashmap[tmp] = [str_]
            
            ans = []
            for k in hashmap:
                ans.append(hashmap[k])
            return ans