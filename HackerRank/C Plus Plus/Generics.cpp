// Link --> https://www.hackerrank.com/challenges/30-generics/problem

// Code:
template <typename T>
void printArray(vector<T> vec)
{
    for(int i=0; i<vec.size(); i++)
        cout<<vec[i]<<endl;
}
