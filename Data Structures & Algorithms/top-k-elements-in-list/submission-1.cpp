class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> mp; // take a hashmap
        vector<int> ans; // to store top freq. k elements
        for(const auto &it: nums) mp[it]++; // create frequency map 
        vector<pair<int, int>> vec(mp.begin(), mp.end()); // create a vector from pairs from map to apply sort method
        sort(vec.begin(), vec.end(), [](const auto& a, const auto& b) { // sort the vector in descending order based on 
        return a.second > b.second;}); // second value from the pair(ie. frequency)
        for(int i = 0; i < k; i++){ // take first k elements and store it in the answer array
            ans.push_back(vec[i].first);
        }
        return ans; // return the answer array
    }
};
