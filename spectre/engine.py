import shodan

class SpectreEngine:
    def init(self, api_key):
        self.api = shodan.Shodan(api_key)

    def search_radar(self, lat, lon, radius):
        query = f'port:554 geo:{lat},{lon},{radius}'
        try:
            results = self.api.search(query)
            return results['matches']
        except Exception as e:
            return str(e)