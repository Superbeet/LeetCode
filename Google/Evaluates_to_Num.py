import operator

def evaluates_to_num(nums, target):
	dp = [[None for j in xrange(4)] for i in xrange(len(target))]
	dp[0] = nums[0]

	opt = [
		operater.add, 
		operater.sub, 
		operater.mul, 
		operater.floordiv
	]

	# no parthenesis
	for i in xrange(1, len(nums)):
		for j in xrange(4):
			= opt()

#include <iostream> 
#include <string> 
#include <cmath> 
#include <cstdlib>
 
using namespace std; 
 
const  double	PRECISION = 1E-6; 
const  int	COUNT_OF_NUMBER  = 4;  
const  int	NUMBER_TO_BE_CAL = 24; 
 
double	number[COUNT_OF_NUMBER]; 
string	expression[COUNT_OF_NUMBER]; 
bool	Judgement = false;	//判断是否有解。
int	count = 0;  
 
void Search(int n) 
{
	if (n==1) { 
		if (fabs(number[0] - NUMBER_TO_BE_CAL) <= PRECISION) {	//对于除法，要小心小数的精确位数  
			cout <<expression[0] <<"\t\t";  
			Judgement = true;
			++count;
			if((count % 3)==0)
				cout <<endl;
		} 
	} 
	for(int i=0; i < n; ++i) {
		for (int j=i+1; j<n; ++j) { 
			double	a, b; 
			string		expa, expb; 
 
			a = number[i]; 
			b = number[j]; 
			number[j]  =  number[n-1]; //递归之后，n比以前小一位，所以可以不停向前赋值  
 
			expa = expression[i]; 
			expb = expression[j]; 
			expression[j]  =  expression[n - 1]; //递归之后，n比以前小一位，所以可以不停向前赋值
 
			expression[i] = '(' + expa + '+' + expb + ')'; //加法不需要分顺序
			number[i] = a + b; 
			Search(n-1);
 
			expression[i] = '(' + expa + '-' + expb + ')'; //减法应该分顺序，减数以及被减数
			number[i] = a - b; 
			Search(n-1);  
 
			expression[i] = '(' + expb + '-' + expa + ')'; //减法应该分顺序，减数以及被减数
			number[i] = b - a; 
			Search(n-1);  
 
			expression[i] = '(' + expa + '*' + expb + ')'; //乘法不需要分顺序
			number[i] = a * b; 
			Search(n-1);  
 
			if (b != 0) { 
				expression[i] = '(' + expa + '/' + expb + ')'; //除法应该分顺序，除数以及被除数
			    number[i] = a / b; 
			    Search(n-1); 
			}   
			if (a != 0) { 
			    expression[i] = '(' + expb + '/' + expa + ')'; //除法应该分顺序，除数以及被除数
			    number[i] = b  /  a; 
			    Search(n-1); 
			} 
 
			number[i] = a;      //这4句语句是为了防止如果上面几种可能都失败了的话,
			number[j] = b;      //就把原来的赋值撤消回去,以无干扰的正确的进入到下一次
			expression[i] = expa;     //for循环队列中。
			expression[j] = expb;     
      } 
  } 
} 
 
 
int  main() 
{ 
	cout<<"输入四个数:\n";
	for (int i=0; i < COUNT_OF_NUMBER; ++i) { 
		char buffer[20];  
		cout <<"第"<<i+1<<"个数:";
		cin >>number[i];       
		itoa(number[i], buffer, 10);
		expression[i] = buffer; 
	} 
	cout <<endl;
	Search(COUNT_OF_NUMBER) ;
	if(Judgement){ 
		cout <<"\n成功" <<endl; 
		cout <<"求和方法有 " <<count <<" 种" <<endl;
	} 
	else { 
		cout << "失败" << endl; 
	}    
	return 0;
}