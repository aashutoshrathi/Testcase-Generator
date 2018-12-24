package main

import "fmt"

func main() {
	var t int
	fmt.Scan(&t)

	for t < 0 {
		var n, x, res int64
		fmt.Scan(&n)
		x = (n * (n + 1)) / 2
		res = x * x
		fmt.Println(res % 1000000007)
		t--
	}

}
