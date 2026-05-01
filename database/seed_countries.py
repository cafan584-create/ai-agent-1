"""
Seed all 195 countries into the database.
Run: python database/seed_countries.py
"""

COUNTRIES = [
    {"code": "AF", "name": "Afghanistan", "region": "Asia", "sub_region": "Southern Asia"},
    {"code": "AL", "name": "Albania", "region": "Europe", "sub_region": "Southern Europe"},
    {"code": "DZ", "name": "Algeria", "region": "Africa", "sub_region": "Northern Africa"},
    {"code": "AO", "name": "Angola", "region": "Africa", "sub_region": "Middle Africa"},
    {"code": "AR", "name": "Argentina", "region": "Americas", "sub_region": "South America"},
    {"code": "AM", "name": "Armenia", "region": "Asia", "sub_region": "Western Asia"},
    {"code": "AU", "name": "Australia", "region": "Oceania", "sub_region": "Australia and New Zealand"},
    {"code": "AT", "name": "Austria", "region": "Europe", "sub_region": "Western Europe"},
    {"code": "AZ", "name": "Azerbaijan", "region": "Asia", "sub_region": "Western Asia"},
    {"code": "BH", "name": "Bahrain", "region": "Asia", "sub_region": "Western Asia"},
    {"code": "BD", "name": "Bangladesh", "region": "Asia", "sub_region": "Southern Asia"},
    {"code": "BY", "name": "Belarus", "region": "Europe", "sub_region": "Eastern Europe"},
    {"code": "BE", "name": "Belgium", "region": "Europe", "sub_region": "Western Europe"},
    {"code": "BZ", "name": "Belize", "region": "Americas", "sub_region": "Central America"},
    {"code": "BJ", "name": "Benin", "region": "Africa", "sub_region": "Western Africa"},
    {"code": "BT", "name": "Bhutan", "region": "Asia", "sub_region": "Southern Asia"},
    {"code": "BO", "name": "Bolivia", "region": "Americas", "sub_region": "South America"},
    {"code": "BA", "name": "Bosnia and Herzegovina", "region": "Europe", "sub_region": "Southern Europe"},
    {"code": "BW", "name": "Botswana", "region": "Africa", "sub_region": "Southern Africa"},
    {"code": "BR", "name": "Brazil", "region": "Americas", "sub_region": "South America"},
    {"code": "BN", "name": "Brunei", "region": "Asia", "sub_region": "South-Eastern Asia"},
    {"code": "BG", "name": "Bulgaria", "region": "Europe", "sub_region": "Eastern Europe"},
    {"code": "BF", "name": "Burkina Faso", "region": "Africa", "sub_region": "Western Africa"},
    {"code": "BI", "name": "Burundi", "region": "Africa", "sub_region": "Eastern Africa"},
    {"code": "KH", "name": "Cambodia", "region": "Asia", "sub_region": "South-Eastern Asia"},
    {"code": "CM", "name": "Cameroon", "region": "Africa", "sub_region": "Middle Africa"},
    {"code": "CA", "name": "Canada", "region": "Americas", "sub_region": "Northern America"},
    {"code": "CV", "name": "Cape Verde", "region": "Africa", "sub_region": "Western Africa"},
    {"code": "CF", "name": "Central African Republic", "region": "Africa", "sub_region": "Middle Africa"},
    {"code": "TD", "name": "Chad", "region": "Africa", "sub_region": "Middle Africa"},
    {"code": "CL", "name": "Chile", "region": "Americas", "sub_region": "South America"},
    {"code": "CN", "name": "China", "region": "Asia", "sub_region": "Eastern Asia"},
    {"code": "CO", "name": "Colombia", "region": "Americas", "sub_region": "South America"},
    {"code": "KM", "name": "Comoros", "region": "Africa", "sub_region": "Eastern Africa"},
    {"code": "CD", "name": "Congo (DRC)", "region": "Africa", "sub_region": "Middle Africa"},
    {"code": "CR", "name": "Costa Rica", "region": "Americas", "sub_region": "Central America"},
    {"code": "CI", "name": "Côte d'Ivoire", "region": "Africa", "sub_region": "Western Africa"},
    {"code": "HR", "name": "Croatia", "region": "Europe", "sub_region": "Southern Europe"},
    {"code": "CU", "name": "Cuba", "region": "Americas", "sub_region": "Caribbean"},
    {"code": "CY", "name": "Cyprus", "region": "Europe", "sub_region": "Southern Europe"},
    {"code": "CZ", "name": "Czech Republic", "region": "Europe", "sub_region": "Eastern Europe"},
    {"code": "DK", "name": "Denmark", "region": "Europe", "sub_region": "Northern Europe"},
    {"code": "DJ", "name": "Djibouti", "region": "Africa", "sub_region": "Eastern Africa"},
    {"code": "DO", "name": "Dominican Republic", "region": "Americas", "sub_region": "Caribbean"},
    {"code": "EC", "name": "Ecuador", "region": "Americas", "sub_region": "South America"},
    {"code": "EG", "name": "Egypt", "region": "Africa", "sub_region": "Northern Africa"},
    {"code": "SV", "name": "El Salvador", "region": "Americas", "sub_region": "Central America"},
    {"code": "GQ", "name": "Equatorial Guinea", "region": "Africa", "sub_region": "Middle Africa"},
    {"code": "ER", "name": "Eritrea", "region": "Africa", "sub_region": "Eastern Africa"},
    {"code": "EE", "name": "Estonia", "region": "Europe", "sub_region": "Northern Europe"},
    {"code": "SZ", "name": "Eswatini", "region": "Africa", "sub_region": "Southern Africa"},
    {"code": "ET", "name": "Ethiopia", "region": "Africa", "sub_region": "Eastern Africa"},
    {"code": "FJ", "name": "Fiji", "region": "Oceania", "sub_region": "Melanesia"},
    {"code": "FI", "name": "Finland", "region": "Europe", "sub_region": "Northern Europe"},
    {"code": "FR", "name": "France", "region": "Europe", "sub_region": "Western Europe"},
    {"code": "GA", "name": "Gabon", "region": "Africa", "sub_region": "Middle Africa"},
    {"code": "GM", "name": "Gambia", "region": "Africa", "sub_region": "Western Africa"},
    {"code": "GE", "name": "Georgia", "region": "Asia", "sub_region": "Western Asia"},
    {"code": "DE", "name": "Germany", "region": "Europe", "sub_region": "Western Europe"},
    {"code": "GH", "name": "Ghana", "region": "Africa", "sub_region": "Western Africa"},
    {"code": "GR", "name": "Greece", "region": "Europe", "sub_region": "Southern Europe"},
    {"code": "GT", "name": "Guatemala", "region": "Americas", "sub_region": "Central America"},
    {"code": "GN", "name": "Guinea", "region": "Africa", "sub_region": "Western Africa"},
    {"code": "GW", "name": "Guinea-Bissau", "region": "Africa", "sub_region": "Western Africa"},
    {"code": "GY", "name": "Guyana", "region": "Americas", "sub_region": "South America"},
    {"code": "HT", "name": "Haiti", "region": "Americas", "sub_region": "Caribbean"},
    {"code": "HN", "name": "Honduras", "region": "Americas", "sub_region": "Central America"},
    {"code": "HU", "name": "Hungary", "region": "Europe", "sub_region": "Eastern Europe"},
    {"code": "IS", "name": "Iceland", "region": "Europe", "sub_region": "Northern Europe"},
    {"code": "IN", "name": "India", "region": "Asia", "sub_region": "Southern Asia"},
    {"code": "ID", "name": "Indonesia", "region": "Asia", "sub_region": "South-Eastern Asia"},
    {"code": "IR", "name": "Iran", "region": "Asia", "sub_region": "Southern Asia"},
    {"code": "IQ", "name": "Iraq", "region": "Asia", "sub_region": "Western Asia"},
    {"code": "IE", "name": "Ireland", "region": "Europe", "sub_region": "Northern Europe"},
    {"code": "IL", "name": "Israel", "region": "Asia", "sub_region": "Western Asia"},
    {"code": "IT", "name": "Italy", "region": "Europe", "sub_region": "Southern Europe"},
    {"code": "JM", "name": "Jamaica", "region": "Americas", "sub_region": "Caribbean"},
    {"code": "JP", "name": "Japan", "region": "Asia", "sub_region": "Eastern Asia"},
    {"code": "JO", "name": "Jordan", "region": "Asia", "sub_region": "Western Asia"},
    {"code": "KZ", "name": "Kazakhstan", "region": "Asia", "sub_region": "Central Asia"},
    {"code": "KE", "name": "Kenya", "region": "Africa", "sub_region": "Eastern Africa"},
    {"code": "KW", "name": "Kuwait", "region": "Asia", "sub_region": "Western Asia"},
    {"code": "KG", "name": "Kyrgyzstan", "region": "Asia", "sub_region": "Central Asia"},
    {"code": "LA", "name": "Laos", "region": "Asia", "sub_region": "South-Eastern Asia"},
    {"code": "LV", "name": "Latvia", "region": "Europe", "sub_region": "Northern Europe"},
    {"code": "LB", "name": "Lebanon", "region": "Asia", "sub_region": "Western Asia"},
    {"code": "LS", "name": "Lesotho", "region": "Africa", "sub_region": "Southern Africa"},
    {"code": "LR", "name": "Liberia", "region": "Africa", "sub_region": "Western Africa"},
    {"code": "LY", "name": "Libya", "region": "Africa", "sub_region": "Northern Africa"},
    {"code": "LT", "name": "Lithuania", "region": "Europe", "sub_region": "Northern Europe"},
    {"code": "LU", "name": "Luxembourg", "region": "Europe", "sub_region": "Western Europe"},
    {"code": "MG", "name": "Madagascar", "region": "Africa", "sub_region": "Eastern Africa"},
    {"code": "MW", "name": "Malawi", "region": "Africa", "sub_region": "Eastern Africa"},
    {"code": "MY", "name": "Malaysia", "region": "Asia", "sub_region": "South-Eastern Asia"},
    {"code": "MV", "name": "Maldives", "region": "Asia", "sub_region": "Southern Asia"},
    {"code": "ML", "name": "Mali", "region": "Africa", "sub_region": "Western Africa"},
    {"code": "MT", "name": "Malta", "region": "Europe", "sub_region": "Southern Europe"},
    {"code": "MR", "name": "Mauritania", "region": "Africa", "sub_region": "Western Africa"},
    {"code": "MU", "name": "Mauritius", "region": "Africa", "sub_region": "Eastern Africa"},
    {"code": "MX", "name": "Mexico", "region": "Americas", "sub_region": "Central America"},
    {"code": "MD", "name": "Moldova", "region": "Europe", "sub_region": "Eastern Europe"},
    {"code": "MN", "name": "Mongolia", "region": "Asia", "sub_region": "Eastern Asia"},
    {"code": "ME", "name": "Montenegro", "region": "Europe", "sub_region": "Southern Europe"},
    {"code": "MA", "name": "Morocco", "region": "Africa", "sub_region": "Northern Africa"},
    {"code": "MZ", "name": "Mozambique", "region": "Africa", "sub_region": "Eastern Africa"},
    {"code": "MM", "name": "Myanmar", "region": "Asia", "sub_region": "South-Eastern Asia"},
    {"code": "NA", "name": "Namibia", "region": "Africa", "sub_region": "Southern Africa"},
    {"code": "NP", "name": "Nepal", "region": "Asia", "sub_region": "Southern Asia"},
    {"code": "NL", "name": "Netherlands", "region": "Europe", "sub_region": "Western Europe"},
    {"code": "NZ", "name": "New Zealand", "region": "Oceania", "sub_region": "Australia and New Zealand"},
    {"code": "NI", "name": "Nicaragua", "region": "Americas", "sub_region": "Central America"},
    {"code": "NE", "name": "Niger", "region": "Africa", "sub_region": "Western Africa"},
    {"code": "NG", "name": "Nigeria", "region": "Africa", "sub_region": "Western Africa"},
    {"code": "KP", "name": "North Korea", "region": "Asia", "sub_region": "Eastern Asia"},
    {"code": "MK", "name": "North Macedonia", "region": "Europe", "sub_region": "Southern Europe"},
    {"code": "NO", "name": "Norway", "region": "Europe", "sub_region": "Northern Europe"},
    {"code": "OM", "name": "Oman", "region": "Asia", "sub_region": "Western Asia"},
    {"code": "PK", "name": "Pakistan", "region": "Asia", "sub_region": "Southern Asia"},
    {"code": "PA", "name": "Panama", "region": "Americas", "sub_region": "Central America"},
    {"code": "PG", "name": "Papua New Guinea", "region": "Oceania", "sub_region": "Melanesia"},
    {"code": "PY", "name": "Paraguay", "region": "Americas", "sub_region": "South America"},
    {"code": "PE", "name": "Peru", "region": "Americas", "sub_region": "South America"},
    {"code": "PH", "name": "Philippines", "region": "Asia", "sub_region": "South-Eastern Asia"},
    {"code": "PL", "name": "Poland", "region": "Europe", "sub_region": "Eastern Europe"},
    {"code": "PT", "name": "Portugal", "region": "Europe", "sub_region": "Southern Europe"},
    {"code": "QA", "name": "Qatar", "region": "Asia", "sub_region": "Western Asia"},
    {"code": "RO", "name": "Romania", "region": "Europe", "sub_region": "Eastern Europe"},
    {"code": "RU", "name": "Russia", "region": "Europe", "sub_region": "Eastern Europe"},
    {"code": "RW", "name": "Rwanda", "region": "Africa", "sub_region": "Eastern Africa"},
    {"code": "SA", "name": "Saudi Arabia", "region": "Asia", "sub_region": "Western Asia"},
    {"code": "SN", "name": "Senegal", "region": "Africa", "sub_region": "Western Africa"},
    {"code": "RS", "name": "Serbia", "region": "Europe", "sub_region": "Southern Europe"},
    {"code": "SL", "name": "Sierra Leone", "region": "Africa", "sub_region": "Western Africa"},
    {"code": "SG", "name": "Singapore", "region": "Asia", "sub_region": "South-Eastern Asia"},
    {"code": "SK", "name": "Slovakia", "region": "Europe", "sub_region": "Eastern Europe"},
    {"code": "SI", "name": "Slovenia", "region": "Europe", "sub_region": "Southern Europe"},
    {"code": "SB", "name": "Solomon Islands", "region": "Oceania", "sub_region": "Melanesia"},
    {"code": "SO", "name": "Somalia", "region": "Africa", "sub_region": "Eastern Africa"},
    {"code": "ZA", "name": "South Africa", "region": "Africa", "sub_region": "Southern Africa"},
    {"code": "KR", "name": "South Korea", "region": "Asia", "sub_region": "Eastern Asia"},
    {"code": "SS", "name": "South Sudan", "region": "Africa", "sub_region": "Eastern Africa"},
    {"code": "ES", "name": "Spain", "region": "Europe", "sub_region": "Southern Europe"},
    {"code": "LK", "name": "Sri Lanka", "region": "Asia", "sub_region": "Southern Asia"},
    {"code": "SD", "name": "Sudan", "region": "Africa", "sub_region": "Northern Africa"},
    {"code": "SR", "name": "Suriname", "region": "Americas", "sub_region": "South America"},
    {"code": "SE", "name": "Sweden", "region": "Europe", "sub_region": "Northern Europe"},
    {"code": "CH", "name": "Switzerland", "region": "Europe", "sub_region": "Western Europe"},
    {"code": "SY", "name": "Syria", "region": "Asia", "sub_region": "Western Asia"},
    {"code": "TW", "name": "Taiwan", "region": "Asia", "sub_region": "Eastern Asia"},
    {"code": "TJ", "name": "Tajikistan", "region": "Asia", "sub_region": "Central Asia"},
    {"code": "TZ", "name": "Tanzania", "region": "Africa", "sub_region": "Eastern Africa"},
    {"code": "TH", "name": "Thailand", "region": "Asia", "sub_region": "South-Eastern Asia"},
    {"code": "TG", "name": "Togo", "region": "Africa", "sub_region": "Western Africa"},
    {"code": "TT", "name": "Trinidad and Tobago", "region": "Americas", "sub_region": "Caribbean"},
    {"code": "TN", "name": "Tunisia", "region": "Africa", "sub_region": "Northern Africa"},
    {"code": "TR", "name": "Turkey", "region": "Asia", "sub_region": "Western Asia"},
    {"code": "TM", "name": "Turkmenistan", "region": "Asia", "sub_region": "Central Asia"},
    {"code": "UG", "name": "Uganda", "region": "Africa", "sub_region": "Eastern Africa"},
    {"code": "UA", "name": "Ukraine", "region": "Europe", "sub_region": "Eastern Europe"},
    {"code": "AE", "name": "United Arab Emirates", "region": "Asia", "sub_region": "Western Asia"},
    {"code": "GB", "name": "United Kingdom", "region": "Europe", "sub_region": "Northern Europe"},
    {"code": "US", "name": "United States", "region": "Americas", "sub_region": "Northern America"},
    {"code": "UY", "name": "Uruguay", "region": "Americas", "sub_region": "South America"},
    {"code": "UZ", "name": "Uzbekistan", "region": "Asia", "sub_region": "Central Asia"},
    {"code": "VE", "name": "Venezuela", "region": "Americas", "sub_region": "South America"},
    {"code": "VN", "name": "Vietnam", "region": "Asia", "sub_region": "South-Eastern Asia"},
    {"code": "YE", "name": "Yemen", "region": "Asia", "sub_region": "Western Asia"},
    {"code": "ZM", "name": "Zambia", "region": "Africa", "sub_region": "Eastern Africa"},
    {"code": "ZW", "name": "Zimbabwe", "region": "Africa", "sub_region": "Eastern Africa"},
]


def seed_countries(db_url: str):
    """Connect to Supabase and insert all 195 countries."""
    import psycopg2
    from psycopg2.extras import execute_values

    conn = psycopg2.connect(db_url)
    cur = conn.cursor()

    rows = []
    for c in COUNTRIES:
        rows.append((c["code"], c["name"], c["region"], c["sub_region"]))

    execute_values(
        cur,
        """
        INSERT INTO countries (code, name, region, sub_region)
        VALUES %s
        ON CONFLICT (code) DO UPDATE SET
            name = EXCLUDED.name,
            region = EXCLUDED.region,
            sub_region = EXCLUDED.sub_region,
            updated_at = NOW()
        """,
        rows,
        template="(code, name, region, sub_region)",
    )

    conn.commit()
    print(f"Seeded {cur.rowcount} countries successfully.")

    cur.execute("SELECT COUNT(*) FROM countries")
    total = cur.fetchone()[0]
    print(f"Total countries in database: {total}")

    cur.close()
    conn.close()


if __name__ == "__main__":
    import os
    from dotenv import load_dotenv

    load_dotenv()

    db_url = os.getenv("SUPABASE_DB_URL")
    if not db_url:
        print("ERROR: SUPABASE_DB_URL not set in .env file")
        exit(1)

    seed_countries(db_url)
