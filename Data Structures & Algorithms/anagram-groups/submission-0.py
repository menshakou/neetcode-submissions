class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        
        for s in strs:
            # Сортируем символы строки — анаграммы дадут одинаковый результат
            key = ''.join(sorted(s))
            ans[key].append(s)
        
        return list(ans.values())