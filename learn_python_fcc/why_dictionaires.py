monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "Jun",
    "Jul": "Jul",
    "Aug": "Aug",
    "Sep": "Sep",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
    "1": "One",
    "2": "Two",
    "3": "Three",
}

print(monthConversions["Jul"])

print(monthConversions.get("Bla", "Not a valid key"))