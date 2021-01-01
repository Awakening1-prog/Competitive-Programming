


bool solve(vector<int>& nums, int k) {
    for(int i=0;i<nums.size();i++)
    {
        int res=nums[i];
        int s=0;
        nums.erase(nums.begin()+i);
        for(auto x: nums)
        {
            s+=x;
        }
        cout<<"s"<<s;
        if(s==k*nums.size())
        {
            return true;
        }
        //cout<<nums[i]<<;
        nums.insert(nums.begin()+i,res);
    }
    return false;

}
