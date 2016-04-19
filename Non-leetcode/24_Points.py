/*****
*
*算 24点（包括小数）
*输出计算过程
*
*****/
#include <iostream>
#include <string>
#include <cmath>
using namespace std;

const double PRECISION = 1E-6;
const int COUNT_OF_NUMBER = 4;
const int NUMBER_TO_BE_CAL = 24; 
double number[COUNT_OF_NUMBER];
string expression[COUNT_OF_NUMBER];

bool Search(int n)
{
   if (n == 1)
       { if ( fabs(number[0] - NUMBER_TO_BE_CAL) < PRECISION ) 
         { 
           return true;
         } 
           else {
             return false; 
             } 
       } 
           for (int i = 1; i < n; i++) { 
                 { 
                    a = number[i-1];
                    b = number[i];
                    number[j] = number[n - 1];

                    /*计算a+b*/
                    number[i] = a + b; 
                    if ( Search(n - 1) ) return true;

                    /*计算a-b*/
                    number[i] = a - b; 
                    if ( Search(n - 1) ) return true;

                    /*计算(a*b)*/
                    number[i] = a * b;
                    if ( Search(n - 1) ) return true;

                    /*计算(a/b)*/
                    if (b != 0) {
                        number[i] = a / b;
                        if ( Search(n - 1) ) return true;
                        }

                    /*恢复现场*/
                     number[i] = a;
                     number[j] = b;
                 } 
           } 
           return false;
}