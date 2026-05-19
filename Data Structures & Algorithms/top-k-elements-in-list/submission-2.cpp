class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> mp;
        for(auto &i:nums) mp[i]++;
        vector<vector<int>> buc(nums.size()+1);
        for(auto &[k,v] : mp)
            buc[v].push_back(k);
        vector<int> ans;
        for(int i = buc.size() - 1; i >= 0 && ans.size() < k ;i--){
            for(auto ele: buc[i]){
                ans.push_back(ele);
            }
            if(ans.size() > k) break;
        }
        return ans;
    }
};
