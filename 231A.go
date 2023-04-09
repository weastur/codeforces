package main

import (
	"fmt"
	"os"
)

func debug(args ...interface{}) {
	if os.Getenv("DEBUG") == "true" {
		fmt.Fprintln(os.Stderr, args...)
	}
}

func main() {
	var n, a, b, c, ans int
	fmt.Scan(&n)
	for n > 0 {
		fmt.Scan(&a, &b, &c)
		if a+b+c >= 2 {
			ans++
		}
		n--
	}
	fmt.Println(ans)
}
