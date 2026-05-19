class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_map<int, int> mp;
        for(auto n : nums) mp[n]++;
        for(auto e : mp){
            if(e.second >= 2){
                return true;
            }
        }
        return false;
    }
};
