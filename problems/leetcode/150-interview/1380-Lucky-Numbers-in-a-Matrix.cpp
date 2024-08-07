class Solution {
public:
    vector<int> luckyNumbers (vector<vector<int>>& matrix) {
        int ans=0;
        int ind=0;
        for(vector<int>&x:matrix){
            auto minP=min_element(x.begin(),x.end());
            if(ans<*minP){
                ans=*minP;
                ind=minP-x.begin();
            }
        }
        for(vector<int>&x:matrix){
            if(x[ind]>ans)return {};
        }
        return {ans};
    }
};