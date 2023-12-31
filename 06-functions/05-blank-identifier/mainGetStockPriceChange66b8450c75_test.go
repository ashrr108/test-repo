// Test generated by RoostGPT for test roost-test using AI Model vertex

package main

import (
	"fmt"
	"math"
	"testing"
)

func TestGetStockPriceChange66b8450c75(t *testing.T) {
	// Test case 1: Positive change
	prevPrice := 100.0
	currentPrice := 110.0
	change, percentChange := getStockPriceChange(prevPrice, currentPrice)
	if change != 10.0 {
		t.Error("Expected change to be 10.0, but got", change)
	}
	if percentChange != 10.0 {
		t.Error("Expected percent change to be 10.0, but got", percentChange)
	}

	// Test case 2: Negative change
	prevPrice = 100.0
	currentPrice = 90.0
	change, percentChange = getStockPriceChange(prevPrice, currentPrice)
	if change != -10.0 {
		t.Error("Expected change to be -10.0, but got", change)
	}
	if percentChange != -10.0 {
		t.Error("Expected percent change to be -10.0, but got", percentChange)
	}

	// Test case 3: Same price
	prevPrice = 100.0
	currentPrice = 100.0
	change, percentChange = getStockPriceChange(prevPrice, currentPrice)
	if change != 0.0 {
		t.Error("Expected change to be 0.0, but got", change)
	}
	if percentChange != 0.0 {
		t.Error("Expected percent change to be 0.0, but got", percentChange)
	}
}