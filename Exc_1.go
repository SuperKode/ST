package main

import (
    . "fmt"
    "runtime"
    "time"
)

var i int = 0

func dec() {
	for j := 0;j<999999;j++ {
    	i--;
    }
}

func inc() {
    for j := 0;j<999999;j++ {
    	i++;
    }
}

func main() {
    runtime.GOMAXPROCS(runtime.NumCPU())
    go dec()
    go inc()                     
    
    time.Sleep(100*time.Millisecond)
    Println(i)
}
