class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> mp;
        for(string &s : strs) {
            int freq[26] = {0};
            // O(k)
            for(char c : s)
                freq[c - 'a']++;
            // Build key in O(26) = O(1)
            string key;
            for(int i = 0; i < 26; i++) {
                key += to_string(freq[i]) + '#';
            }
            mp[key].push_back(s);
        }
        vector<vector<string>> result;
        for(auto &it : mp)
            result.push_back(it.second);
        return result;
    }
};
