class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> ans(n);
        int pre = 1;
        ans[0] = 1;
        for(int i = 1; i < n; i++){
            pre *= nums[i-1];
            ans[i] = pre;
        }
        int post = 1;
        for(int i = n-2; i>=0; i--){
            post *= nums[i+1];
            ans[i] *= post;
        }
        return ans;
    }
};
