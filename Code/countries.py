"""
---
List containing all the countries with at least one Google office
---
Helps the WebScraper identify strings that contain location data
---
https://about.google/locations/?region=north-america
https://about.google/locations/?region=latin-america
https://about.google/locations/?region=europe
https://about.google/locations/?region=asia-pacific
https://about.google/locations/?region=africa-middle-east
---
"""

na = ["USA", "Canada"]

latam = ["Brazil", "Columbia", "Argentina", "Peru", "Mexico", "Chile"]

eu01 = ["Denmark", "Netherlands", "Greece", "Germany", "Belgium", "Ireland", "Portugal", "UK", "Spain"]

eu02 = ["Italy", "Norway", "France", "Czech Republic", "Sweden", "Austria", "Poland", "Switzerland"]

asia_pacific01 = ["New Zealand", "India", "Thailand", "China", "Hong Kong", "Indonesia", "Malaysia"]

asia_pacific02 = ["Philippines", "Australia", "South Korea", "Singapore", "Taiwan", "Japan"]

africa_middle_east = ["Ghana", "UAE", "Israel", "Turkey", "South Africa", "Nigeria"]

aggregated_data = na + latam + eu01 + eu02 + asia_pacific01 + asia_pacific02 + africa_middle_east
