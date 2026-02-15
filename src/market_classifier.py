class MarketClassifier:
    """From https://www.msci.com/indexes/index-resources/market-classification"""

    DEVELOPED_MARKETS = {
        # Americas
        "Canada",
        "United States",
        # EMEA
        "Austria",
        "Belgium",
        "Denmark",
        "Finland",
        "France",
        "Germany",
        "Ireland",
        "Israel",
        "Italy",
        "Netherlands",
        "Norway",
        "Portugal",
        "Spain",
        "Sweden",
        "Switzerland",
        "United Kingdom",
        # APAC
        "Australia",
        "Hong Kong",
        "Japan",
        "New Zealand",
        "Singapore",
    }

    EMERGING_MARKETS = {
        # Americas
        "Brazil",
        "Chile",
        "Colombia",
        "Mexico",
        "Peru",
        # EMEA
        "Czech Republic",
        "Egypt",
        "Greece",
        "Hungary",
        "Kuwait",
        "Poland",
        "Qatar",
        "Saudi Arabia",
        "South Africa",
        "Turkey",
        "United Arab Emirates",
        # APAC
        "China",
        "India",
        "Indonesia",
        "South Korea",
        "Malaysia",
        "Philippines",
        "Thailand",
        "Taiwan",
    }

    FRONTIER_MARKETS = {
        # EMEA
        "Bahrain",
        "Benin",
        "Burkina Faso",
        "Croatia",
        "Guinea-Bissau",
        "Iceland",
        "Ivory Coast",
        "Jordan",
        "Kazakhstan",
        "Kenya",
        "Mali",
        "Mauritius",
        "Morocco",
        "Niger",
        "Oman",
        "Senegal",
        "Serbia",
        "Togo",
        "Tunisia",
        "Estonia",
        "Latvia",
        "Lithuania",
        "Romania",
        "Slovenia",
        # APAC
        "Bangladesh",
        "Pakistan",
        "Sri Lanka",
        "Vietnam",
    }

    @classmethod
    def classify(cls, country: str | None) -> str:
        if not country:
            return ""
        country = str(country).strip().title()
        if country in cls.DEVELOPED_MARKETS:
            return "Developed"
        if country in cls.EMERGING_MARKETS:
            return "Emerging"
        if country in cls.FRONTIER_MARKETS:
            return "Frontier"
        print(f"Unable to classify {country}")
        return ""
