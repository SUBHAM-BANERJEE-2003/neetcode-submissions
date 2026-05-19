class Solution {
public:
    bool isAnagram(string s, string t) {
        char mp[26] = {0};
        if(s.size() != t.size()) return false;
        for(auto c : s) mp[c - 'a']++;
        for(auto c : t) mp[c - 'a']--;
        for(auto n : mp)
            if(n != 0) return false;
        return true;
    }
};
