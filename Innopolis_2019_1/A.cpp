#include <iostream>

int main()
{
	double a, b;
	int x;
	std::cin >> a >> b >> x;
	int volume = 0;
	double temp = 0;
	double m = 0;
	double n = 0;
	while (m + n < 1000) {
		if (temp < x) {
			n += a;
			temp = (100 * n) / (n + m);
		}
		else {
			m += b;
			temp = (100 * n) / (n + m);
		}
		if (temp == x && m + n < 1001) {
			volume = m + n;
		}
	}
	std::cout << volume;
}