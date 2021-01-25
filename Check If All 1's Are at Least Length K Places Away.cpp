class Solution {
public:
    bool kLengthApart(vector<int>& nums, int k) {
        vector<int>l;
        for(int i=0;i<nums.size();i++)
        {
            if(nums[i]==1)
            {
                l.push_back(i);
            }
        }
        if(l.size()==0)
        {
            return 1;
        }
        else
        {
        for(int i=0;i<l.size()-1;i++)
        {
            if((abs(l[i]-l[i+1])-1)<k)
            {
                return 0;
            }
        }
        return 1;
        }
    }
};
