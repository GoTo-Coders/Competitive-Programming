// Link --> https://www.hackerrank.com/challenges/tree-top-view/problem

// Code:
void helper(Node *root, int distance, int level, map<int, pair<int,int>> &Map)
{ 
    if(root == NULL) 
        return; 
    
    helper(root->left, distance-1, level+1, Map);
  
    if(Map.find(distance) == Map.end())
        Map[distance] = {root->data, level}; 
    else if(Map[distance].second > level)
        Map[distance] = {root->data, level};
    
    helper(root->right, distance+1, level+1, Map); 
}

void topView(Node *root) 
{
    if(root ==  NULL)
        return;
    
    map<int, pair<int,int>> Map; 
  
    helper(root, 0, 0, Map); 
    
    for(auto i : Map)
        cout << i.second.first << " ";
}
