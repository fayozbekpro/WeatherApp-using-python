from flet import *
import requests as rq
def main(page: Page):
	page.title = "Weather App"
	page.theme_mode = "dark"
	page.vertical_alignment = MainAxisAlignment.CENTER

	city_name = TextField(label="Enter the city name: ", width=280)
	weather_data = Text('')
	MainSymbol = "°C"
	kelvin = temp = 0;


	def get_info(e):
		nonlocal kelvin, temp
		if len(city_name.value) < 2:
			return;
		API = "021cc4d180793e2374ab5de3dd5ee818"
		URL = f"https://api.openweathermap.org/data/2.5/weather?q={city_name.value}&appid={API}"

		res = rq.get(URL).json()
		weatherData = {
			"temp": res['main']['temp'],
			"feels_like": res["main"]["feels_like"],
			"sky": res['weather'][0]['description'],
		}
		kelvin = weatherData["temp"]
		temp = (kelvin - 273.15) * 9/5 + 32 if MainSymbol == "°F" else kelvin - 273.15

		weather_data.value = f"Result: {temp: .0f}{MainSymbol}"
		
		page.update()
	def change_theme(e):
		page.theme_mode = 'light' if page.theme_mode == "dark" else "dark"
		page.update()


	def change_the_symbol(r):
		nonlocal MainSymbol
		nonlocal kelvin, temp
		MainSymbol = "°C" if MainSymbol == "°F" else "°F"
		temp = (kelvin - 273.15) * 9/5 + 32 if MainSymbol == "°F" else kelvin - 273.15 		
		get_info(0)
	page.add(
		Row(
			[
				IconButton(icons.SUNNY,on_click=change_theme),
				Text("Weather App"),
			],
			alignment=MainAxisAlignment.CENTER
			),

		Row([city_name],alignment=MainAxisAlignment.CENTER),
		Row(
				[
					OutlinedButton("°C / °F",on_click=change_the_symbol),
				],
				alignment=MainAxisAlignment.CENTER,
				
		),
			
		Row([weather_data],alignment=MainAxisAlignment.CENTER),
		Row([ElevatedButton(text="Submit", on_click=get_info)],alignment=MainAxisAlignment.CENTER)
	)
app(target=main)