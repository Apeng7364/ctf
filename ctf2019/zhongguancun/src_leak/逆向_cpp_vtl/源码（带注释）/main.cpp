#include<iostream>
using namespace std;

typedef unsigned int uint;


// 实现选择分支
// 二分法求根值
template <bool Flag, class MaybeA, class MaybeB> class IfElse;

template <class MaybeA, class MaybeB>
class IfElse<true, MaybeA, MaybeB> {
public:
	using ResultType = MaybeA;
};

template <class MaybeA, class MaybeB>
class IfElse<false, MaybeA, MaybeB> {
public:
	using ResultType = MaybeB;
};

template <uint N, uint L, uint R> struct func1 {
	enum { mid = (L + R + 1) / 2 };

	using ResultType = typename IfElse<(N < mid * mid),
		func1<N, L, mid - 1>, func1<N, mid, R> >::ResultType;

	enum { result = ResultType::result };
};

template <uint N, uint L> struct func1<N, L, L> { enum { result = L }; };

template <uint N> struct _func1 { enum { result = func1<N, 1, N>::result }; };






// 递归实现循环
template<size_t Input>
constexpr size_t func2 = (Input % 2) + func2< (Input / 2) >;

template<>
constexpr size_t func2<0> = 0;
//计算无符号数中有多少个1
//比如func2<3> == 2




//简单的判断奇偶性，奇数返回1，偶数返回0
template<size_t num>
constexpr size_t func3 = num % 2;





// 素数相关
// 判断无符号数k是不是素数
// func4<7>::value == 1
// func4<12>::value == 0
template<uint n, uint m>struct NEXTN {
	const static uint value = ((n % m != 0) * n);
};
template<uint n, uint m>struct NEXTM {
	const static uint value = (m * m <= n ? (m + 1) : 0);
};
template<uint n, uint m>struct TEST {
	const static uint value = TEST<NEXTN<n, m>::value, NEXTM<n, m>::value>::value;
};
template<uint m>struct TEST<0, m> {
	const static uint value = 0;
};
template<uint n>struct TEST<n, 0> {
	const static uint value = 1;
};
template<uint n>struct func4 {
	const static uint value = TEST<n, 2>::value;
};
template<>struct func4<1> {
	const static uint value = 0;
};
template<>struct func4<2> {
	const static uint value = 1;
};











int main(int argc, char**argv) {
	//input 5 uint numbers ,x1,x2,x3,x4,x5
	//the sum of them should be MIN
	//这里输入5个无符号整形数，func2要求二进制表示时，有奇数个1，返回1
	//func3接收到1，返回1，表示奇数
	/*
	cout << func3< func2<x1> > << endl;
	cout << func3< func2<x2> > << endl;
	cout << func3< func2<x3> > << endl;
	cout << func3< func2<x4> > << endl;
	cout << func3< func2<x5> > << endl;
	*/
	// output: 1 1 1 1 1


	//开根号
	//要求开根号之后等于接下来的五个数，由于是向下取整，会有很多满足的
	//!因此我在之前提到，要求这五个数的 累加和 最小
	//所以只会有一组解
	/*
	cout << _func1<x1>::result << endl;
	cout << _func1<x2>::result << endl;
	cout << _func1<x3>::result << endl;
	cout << _func1<x4>::result << endl;
	cout << _func1<x5>::result << endl;
	*/
	//output: 963 4396 6666 1999 3141


	// 927369	 963
	// 19324816	 4396
	// 44435556  6666
	// 3996001   1999
	// 9865881	 3141







	//素数返回1
	//预期的值是1229，因为1-10000有1229个素数
	//if you input 10000
	//how many "1" will func4<1>,func4<2>,fun4<3>......fun4<10000> ::value  return?
	//x6 = count;

	
	// your flag is flag{x1-x2-x3-x4-x5-x6}
	// if x1=1,x2=2,x3=3,x4=4,x5=5,x6=6
	// flag is     flag{1-2-3-4-5-6}
	
	
	//于是最后的flag是
	flag{927369-19324816-44435556-3996001-9865881-1229}
	
	return 0;
}


