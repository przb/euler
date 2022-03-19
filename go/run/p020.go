package main

import (
	"math"
)

func mergeSlice(n []int, m []int) []int {
	var merged []int
	for i := 0; i < len(n); i++ {
		merged = append(merged, n[i])
	}
	for i := 0; i < len(m); i++ {
		merged = append(merged, m[i])
	}

	return merged
}

func Factors(n int) []int {
	var factors []int
	for i := 2; i <= int(math.Sqrt(float64(n))); i++ {
		if n%i == 0 {
			factors = append(factors, i)
			factors = append(factors, n/i)
		}
	}
	return factors
}

func PrimeFactors(n int) []int {
	var factors []int
	if isPrime(n) {
		factors = append(factors, n)
		return factors
	} else {
		nonPrimeFactors := Factors(n)
		for i := 0; i < len(nonPrimeFactors); i++ {
			if !isPrime(nonPrimeFactors[i]) {
				newFactors := Factors(nonPrimeFactors[i])
				nonPrimeFactors = append(nonPrimeFactors[0:i])
				nonPrimeFactors = append(nonPrimeFactors[i:len(nonPrimeFactors)])
				factors = mergeSlice(factors, newFactors)
			}
		}
		return factors
	}
}

func isPrime(n int) bool {
	if n == 2 {
		return true
	} else if n%2 == 0 {
		return false
	}
	for i := 3; i <= int(math.Sqrt(float64(n))); i += 2 {
		if n%i == 0 {
			return false
		}
	}
	return true
}
