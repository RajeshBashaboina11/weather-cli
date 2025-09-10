from weather.fetch import get_weather

def main():
	city = input("Enter city name: ")
	data = get_weather(city)

	if "error" in data:
	     print(data["error"])
	else:
	print(f"Weather in {city}:")
	print(f"Description: {data['Weather'][0]['description']}")
	print(f"Temperature: {data['main']['temp']} °C")
	print(f"Humdity: {data['main']['humidity']}%")
	print(f"Wind Speed: {data['wind']['speed']} m/s")

if__name__ == "__main__":
    main()