int solve(vector<int>& nums, int k) {
    int n=nums.size();
    int p=k;
    int r=1;
    if(n==0)
    return 0;
    for(int i=0;i<n;i++)
    {
        int res=0;
        while(1)
        {
            if(k>=n)
             return r++;
             k=nums[k];
             if(k<n)
             r++;
             if(r>n+10)
             break;
        }
    }
    return -1;
}
