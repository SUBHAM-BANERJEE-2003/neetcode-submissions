class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> mp;
        for(auto n: nums) mp[n]++;
        vector<pair<int, int>> fp;
        for(auto &[k, v] : mp) fp.push_back({v, k});
        priority_queue<pair<int, int>> pq(fp.begin(), fp.end());
        vector<int> ans;
        for(int i = 0; i < k; i++){
            ans.push_back(pq.top().second);
            pq.pop();
        }
        return ans;
    }
};
