package main

import "fmt"

func main() {
	var n, k int
	fmt.Scanf("%d%d", &n, &k)
	for k > 0 {
		if n%10 == 0 {
			n /= 10
		} else {
			n--
		}
		k--
	}
	fmt.Printf("%d", n)
}
