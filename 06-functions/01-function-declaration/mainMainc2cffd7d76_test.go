// Test generated by RoostGPT for test roost-test using AI Model vertex

package main

import (
	"fmt"
	"testing"
)

func TestMainc2cffd7d76(t *testing.T) {
	// Test case 1: Positive test case
	x := 5.75
	y := 6.25

	result := avg(x, y)

	if result != 6 {
		t.Error("Expected average to be 6, but got", result)
	}

	// Test case 2: Negative test case
	x = -5.75
	y = -6.25

	result = avg(x, y)

	if result != -6 {
		t.Error("Expected average to be -6, but got", result)
	}
}

func avg(x, y float64) float64 {
	return (x + y) / 2
}