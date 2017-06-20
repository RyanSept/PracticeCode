from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.network.urlrequest import UrlRequest
from kivy.uix.listview import ListItemButton,ListItemLabel
from kivy.uix.button import Button
from kivy.factory import Factory
from gesture_box import GestureBox

class WeatherRoot(GestureBox):
    weatherroot=ObjectProperty()
    current_weather=ObjectProperty()
    def show_current_weather(self, location=None):
        self.clear_widgets()
        if location is None and self.current_weather is None:
            location = "New York (US)"
        if location is not None:
            self.current_weather = Factory.CurrentWeather()
            self.current_weather.location = location
        self.add_widget(self.current_weather)
    def back(self):
        self.clear_widgets()
        self.weatherroot=Factory.WeatherRoot()
        self.add_widget(self.weatherroot)
class LocationButton(ListItemButton):
    pass
class AddLocationForm(GestureBox):
    search_input=ObjectProperty()
    search_results=ObjectProperty()
    def search_location(self):
        search_template = "http://api.openweathermap.org/data/2.5/" +"find?q={}&type=like"
        search_url = search_template.format(self.search_input.text)
        request = UrlRequest(search_url, self.found_location)
    def found_location(self, request, data):
        cities = ["{} ({})".format(d['name'], d['sys']['country'])for d in data['list']]
        print("\n".join(cities))
        self.search_results.item_strings = cities
        self.search_results.adapter.data[:]
        self.search_results.adapter.data.extend(cities)
        self.search_results._trigger_reset_populate()
class WeatherApp(App):
    def build_config(self, config):
        config.setdefaults('General', {'temp_type': "Metric"})
    def build_settings(self, settings):
    
        settings.add_json_panel("Weather Settings", self.config, data="""\
[\
{"type": "options",
"title": "Temperature System",
"section": "General",
"key": "temp_type",
"options": ["Metric", "Imperial"]\
}\
]"""        
if __name__ == "__main__":
    WeatherApp().run()
