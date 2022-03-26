package main

//Days and months start at 1 because I'm in too lazy to change it
const jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12

var dayOfTheWeek int = 2
var day int = 1
var month int = 1
var year int = 1900

func getDayOfTheWeek() int {
	return dayOfTheWeek
}
func getDay() int {
	return day
}

func nextDay() {
	if dayOfTheWeek == 7 {
		dayOfTheWeek = 1
	} else {
		dayOfTheWeek++
	}

	if month == dec && day == 31 {
		nextYear()
	} else if month == feb {
		if isLeapYear() && day == 29 {
			nextMonth()
		} else if day == 28 {
			nextMonth()
		} else {
			day++
		}
	} else if (monthHas30Days()) && day == 30 {
		nextMonth()
	} else if day == 31 {
		nextMonth()
	} else {
		day++
	}
}

func monthHas30Days() bool {
	return month == sep || month == apr || month == jun || month == nov
}

func getMonth() int {
	return month
}
func nextMonth() {
	if month == dec {
		month = jan
		nextYear()
	} else {
		month++
	}
	day = 1
}

func getYear() int {
	return year
}
func nextYear() {
	year++
	day = 1
	month = 1
}
func isLeapYear() bool {
	if year%400 == 0 {
		return true
	} else if year%100 == 0 {
		return false
	} else if year%4 == 0 {
		return true
	} else {
		return false
	}
}

func getTotalDOTWOnFirst(dotw int) int {
	totalDays := 0
	for year < 1901 {
		nextDay()
	}
	nextDay()
	for year < 2001 {
		if getDayOfTheWeek() == dotw && getDay() == 1 {
			totalDays++
		}
		nextDay()
	}
	return totalDays
}
