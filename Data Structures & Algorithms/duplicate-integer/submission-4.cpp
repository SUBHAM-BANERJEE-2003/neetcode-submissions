class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_map<int, int> mp;
        for(int i = 0; i < nums.size(); i++){
            if(mp.find(nums[i]) != mp.end()){
                mp[nums[i]] = 1;
            }
            mp[nums[i]]++;
        }
        for(auto &[k, v] : mp)
            if(v > 1) return true;
        return false;
    }
};