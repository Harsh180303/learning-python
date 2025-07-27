# Nesting a List in a Dictionary

travel_log = {
    "MP": {"cities_visited": ["Bhopal", "Indore", "Jabalpur", "Gwaliar"], "total_visits": 12},
    "Rajasthan": {"cities_visited": ["Ajmer", "Jaipur", "Pushkar",], "total_visits": 7}
}

# Nesting Dictionary in a Dictionary

travel_log = [
    {
        "State": "MP",
        "cities_visited": ["Bhopal", "Indore", "Jabalpur", "Gwaliar"],
        "total_visits": 12
    },
    {
        "State": "Rajasthan",
        "cities_visited": ["Ajmer", "Jaipur", "Pushkar",],
        "total_visits": 7
    }
]