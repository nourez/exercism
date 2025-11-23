// Package weather provides weather forecast functionality.
package weather

var (
	// CurrentCondition represents the current weather condition.
	CurrentCondition string
	// CurrentLocation represents the current location.
	CurrentLocation string
)

// Forecast takes a city and a condition and returns a string with the current location and weather condition.
func Forecast(city, condition string) string {
	CurrentLocation, CurrentCondition = city, condition
	return CurrentLocation + " - current weather condition: " + CurrentCondition
}
