class Solution {
public:

    bool isanagram(string &s1, string &s2){
        if(s1.size() != s2.size()) return false;
        int hash[26] = {0};
        for(int i = 0; i < s1.size(); i++){hash[s1[i]-'a']++; hash[s2[i]-'a']--;}
        for(const auto &it: hash) if(it != 0) return false;
        return true;
    }
    
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> anagramgroups;
        vector<bool> included(strs.size(), false);
        for(int i = 0; i < strs.size(); i++){
            if(!included[i]){
                string currentstr = strs[i];
                included[i] = true;
                vector<string> anagramgroup = {currentstr};
                for(int j = i+1; j < strs.size();j++){
                    if(isanagram(currentstr, strs[j])){
                        anagramgroup.push_back(strs[j]);
                        included[j] = true;
                    }
                }
                anagramgroups.push_back(anagramgroup);
            }
        }
        return anagramgroups;
    }
};
