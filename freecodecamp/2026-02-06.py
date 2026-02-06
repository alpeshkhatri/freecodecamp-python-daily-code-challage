import unittest

# 2026 Winter Games Day 1: Opening Day
# Today marks the start of the 2026 Winter Games. The next 17 days will bring you coding challenges inspired by them.
#
# For the first one, you are given a two-letter country code and need to return the flag emoji for that country.
#
#
# Country	Code	Flag
# Albania	"AL"	"🇦🇱"
# Andorra	"AD"	"🇦🇩"
# Argentina	"AR"	"🇦🇷"
# Armenia	"AM"	"🇦🇲"
# Australia	"AU"	"🇦🇺"
# Austria	"AT"	"🇦🇹"
# Azerbaijan	"AZ"	"🇦🇿"
# Belgium	"BE"	"🇧🇪"
# Benin	"BJ"	"🇧🇯"
# Bolivia	"BO"	"🇧🇴"
# Bosnia and Herzegovina	"BA"	"🇧🇦"
# Brazil	"BR"	"🇧🇷"
# Bulgaria	"BG"	"🇧🇬"
# Canada	"CA"	"🇨🇦"
# Chile	"CL"	"🇨🇱"
# China	"CN"	"🇨🇳"
# Colombia	"CO"	"🇨🇴"
# Croatia	"HR"	"🇭🇷"
# Cyprus	"CY"	"🇨🇾"
# Czech Republic	"CZ"	"🇨🇿"
# Denmark	"DK"	"🇩🇰"
# Ecuador	"EC"	"🇪🇨"
# Eritrea	"ER"	"🇪🇷"
# Estonia	"EE"	"🇪🇪"
# Finland	"FI"	"🇫🇮"
# France	"FR"	"🇫🇷"
# Georgia	"GE"	"🇬🇪"
# Germany	"DE"	"🇩🇪"
# Great Britain	"GB"	"🇬🇧"
# Greece	"GR"	"🇬🇷"
# Guinea-Bissau	"GW"	"🇬🇼"
# Haiti	"HT"	"🇭🇹"
# Hong Kong	"HK"	"🇭🇰"
# Hungary	"HU"	"🇭🇺"
# Iceland	"IS"	"🇮🇸"
# India	"IN"	"🇮🇳"
# Iran	"IR"	"🇮🇷"
# Ireland	"IE"	"🇮🇪"
# Israel	"IL"	"🇮🇱"
# Italy	"IT"	"🇮🇹"
# Jamaica	"JM"	"🇯🇲"
# Japan	"JP"	"🇯🇵"
# Kazakhstan	"KZ"	"🇰🇿"
# Kenya	"KE"	"🇰🇪"
# Kosovo	"XK"	"🇽🇰"
# Kyrgyzstan	"KG"	"🇰🇬"
# Latvia	"LV"	"🇱🇻"
# Lebanon	"LB"	"🇱🇧"
# Liechtenstein	"LI"	"🇱🇮"
# Lithuania	"LT"	"🇱🇹"
# Luxembourg	"LU"	"🇱🇺"
# Madagascar	"MG"	"🇲🇬"
# Malaysia	"MY"	"🇲🇾"
# Malta	"MT"	"🇲🇹"
# Mexico	"MX"	"🇲🇽"
# Moldova	"MD"	"🇲🇩"
# Monaco	"MC"	"🇲🇨"
# Mongolia	"MN"	"🇲🇳"
# Montenegro	"ME"	"🇲🇪"
# Morocco	"MA"	"🇲🇦"
# Netherlands	"NL"	"🇳🇱"
# New Zealand	"NZ"	"🇳🇿"
# Nigeria	"NG"	"🇳🇬"
# North Macedonia	"MK"	"🇲🇰"
# Norway	"NO"	"🇳🇴"
# Pakistan	"PK"	"🇵🇰"
# Philippines	"PH"	"🇵🇭"
# Poland	"PL"	"🇵🇱"
# Portugal	"PT"	"🇵🇹"
# Puerto Rico	"PR"	"🇵🇷"
# Romania	"RO"	"🇷🇴"
# San Marino	"SM"	"🇸🇲"
# Saudi Arabia	"SA"	"🇸🇦"
# Serbia	"RS"	"🇷🇸"
# Singapore	"SG"	"🇸🇬"
# Slovakia	"SK"	"🇸🇰"
# Slovenia	"SI"	"🇸🇮"
# South Africa	"ZA"	"🇿🇦"
# South Korea	"KR"	"🇰🇷"
# Spain	"ES"	"🇪🇸"
# Sweden	"SE"	"🇸🇪"
# Switzerland	"CH"	"🇨🇭"
# Thailand	"TH"	"🇹🇭"
# Trinidad & Tobago	"TT"	"🇹🇹"
# Turkey	"TR"	"🇹🇷"
# Ukraine	"UA"	"🇺🇦"
# United Arab Emirates	"AE"	"🇦🇪"
# United States	"US"	"🇺🇸"
# Uruguay	"UY"	"🇺🇾"
# Uzbekistan	"UZ"	"🇺🇿"
# Venezuela	"VE"	"🇻🇪"
#
import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")

flags = {
    "AL": "🇦🇱",
    "AD": "🇦🇩",
    "AR": "🇦🇷",
    "AM": "🇦🇲",
    "AU": "🇦🇺",
    "AT": "🇦🇹",
    "AZ": "🇦🇿",
    "BE": "🇧🇪",
    "BJ": "🇧🇯",
    "BO": "🇧🇴",
    "BA": "🇧🇦",
    "BR": "🇧🇷",
    "BG": "🇧🇬",
    "CA": "🇨🇦",
    "CL": "🇨🇱",
    "CN": "🇨🇳",
    "CO": "🇨🇴",
    "HR": "🇭🇷",
    "CY": "🇨🇾",
    "CZ": "🇨🇿",
    "DK": "🇩🇰",
    "EC": "🇪🇨",
    "ER": "🇪🇷",
    "EE": "🇪🇪",
    "FI": "🇫🇮",
    "FR": "🇫🇷",
    "GE": "🇬🇪",
    "DE": "🇩🇪",
    "GB": "🇬🇧",
    "GR": "🇬🇷",
    "GW": "🇬🇼",
    "HT": "🇭🇹",
    "HK": "🇭🇰",
    "HU": "🇭🇺",
    "IS": "🇮🇸",
    "IN": "🇮🇳",
    "IR": "🇮🇷",
    "IE": "🇮🇪",
    "IL": "🇮🇱",
    "IT": "🇮🇹",
    "JM": "🇯🇲",
    "JP": "🇯🇵",
    "KZ": "🇰🇿",
    "KE": "🇰🇪",
    "XK": "🇽🇰",
    "KG": "🇰🇬",
    "LV": "🇱🇻",
    "LB": "🇱🇧",
    "LI": "🇱🇮",
    "LT": "🇱🇹",
    "LU": "🇱🇺",
    "MG": "🇲🇬",
    "MY": "🇲🇾",
    "MT": "🇲🇹",
    "MX": "🇲🇽",
    "MD": "🇲🇩",
    "MC": "🇲🇨",
    "MN": "🇲🇳",
    "ME": "🇲🇪",
    "MA": "🇲🇦",
    "NL": "🇳🇱",
    "NZ": "🇳🇿",
    "NG": "🇳🇬",
    "MK": "🇲🇰",
    "NO": "🇳🇴",
    "PK": "🇵🇰",
    "PH": "🇵🇭",
    "PL": "🇵🇱",
    "PT": "🇵🇹",
    "PR": "🇵🇷",
    "RO": "🇷🇴",
    "SM": "🇸🇲",
    "SA": "🇸🇦",
    "RS": "🇷🇸",
    "SG": "🇸🇬",
    "SK": "🇸🇰",
    "SI": "🇸🇮",
    "ZA": "🇿🇦",
    "KR": "🇰🇷",
    "ES": "🇪🇸",
    "SE": "🇸🇪",
    "CH": "🇨🇭",
    "TH": "🇹🇭",
    "TT": "🇹🇹",
    "TR": "🇹🇷",
    "UA": "🇺🇦",
    "AE": "🇦🇪",
    "US": "🇺🇸",
    "UY": "🇺🇾",
    "UZ": "🇺🇿",
    "VE": "🇻🇪",
}


def get_flag(args):
    logging.debug(f"start of get_flag {args=}")
    return flags[args]


class TestCodeChallenge(unittest.TestCase):
    def test_daily_coding_challenge(self):
        self.assertEqual(get_flag("AL"), "🇦🇱")
        self.assertEqual(get_flag("AD"), "🇦🇩")
        self.assertEqual(get_flag("AR"), "🇦🇷")
        self.assertEqual(get_flag("AM"), "🇦🇲")
        self.assertEqual(get_flag("AU"), "🇦🇺")
        self.assertEqual(get_flag("AT"), "🇦🇹")
        self.assertEqual(get_flag("AZ"), "🇦🇿")
        self.assertEqual(get_flag("BE"), "🇧🇪")
        self.assertEqual(get_flag("BJ"), "🇧🇯")
        self.assertEqual(get_flag("BO"), "🇧🇴")
        self.assertEqual(get_flag("BA"), "🇧🇦")
        self.assertEqual(get_flag("BR"), "🇧🇷")
        self.assertEqual(get_flag("BG"), "🇧🇬")
        self.assertEqual(get_flag("CA"), "🇨🇦")
        self.assertEqual(get_flag("CL"), "🇨🇱")
        self.assertEqual(get_flag("CN"), "🇨🇳")
        self.assertEqual(get_flag("CO"), "🇨🇴")
        self.assertEqual(get_flag("HR"), "🇭🇷")
        self.assertEqual(get_flag("CY"), "🇨🇾")
        self.assertEqual(get_flag("CZ"), "🇨🇿")
        self.assertEqual(get_flag("DK"), "🇩🇰")
        self.assertEqual(get_flag("EC"), "🇪🇨")
        self.assertEqual(get_flag("ER"), "🇪🇷")
        self.assertEqual(get_flag("EE"), "🇪🇪")
        self.assertEqual(get_flag("FI"), "🇫🇮")
        self.assertEqual(get_flag("FR"), "🇫🇷")
        self.assertEqual(get_flag("GE"), "🇬🇪")
        self.assertEqual(get_flag("DE"), "🇩🇪")
        self.assertEqual(get_flag("GB"), "🇬🇧")
        self.assertEqual(get_flag("GR"), "🇬🇷")
        self.assertEqual(get_flag("GW"), "🇬🇼")
        self.assertEqual(get_flag("HT"), "🇭🇹")
        self.assertEqual(get_flag("HK"), "🇭🇰")
        self.assertEqual(get_flag("HU"), "🇭🇺")
        self.assertEqual(get_flag("IS"), "🇮🇸")
        self.assertEqual(get_flag("IN"), "🇮🇳")
        self.assertEqual(get_flag("IR"), "🇮🇷")
        self.assertEqual(get_flag("IE"), "🇮🇪")
        self.assertEqual(get_flag("IL"), "🇮🇱")
        self.assertEqual(get_flag("IT"), "🇮🇹")
        self.assertEqual(get_flag("JM"), "🇯🇲")
        self.assertEqual(get_flag("JP"), "🇯🇵")
        self.assertEqual(get_flag("KZ"), "🇰🇿")
        self.assertEqual(get_flag("KE"), "🇰🇪")
        self.assertEqual(get_flag("XK"), "🇽🇰")
        self.assertEqual(get_flag("KG"), "🇰🇬")
        self.assertEqual(get_flag("LV"), "🇱🇻")
        self.assertEqual(get_flag("LB"), "🇱🇧")
        self.assertEqual(get_flag("LI"), "🇱🇮")
        self.assertEqual(get_flag("LT"), "🇱🇹")
        self.assertEqual(get_flag("LU"), "🇱🇺")
        self.assertEqual(get_flag("MG"), "🇲🇬")
        self.assertEqual(get_flag("MY"), "🇲🇾")
        self.assertEqual(get_flag("MT"), "🇲🇹")
        self.assertEqual(get_flag("MX"), "🇲🇽")
        self.assertEqual(get_flag("MD"), "🇲🇩")
        self.assertEqual(get_flag("MC"), "🇲🇨")
        self.assertEqual(get_flag("MN"), "🇲🇳")
        self.assertEqual(get_flag("ME"), "🇲🇪")
        self.assertEqual(get_flag("MA"), "🇲🇦")
        self.assertEqual(get_flag("NL"), "🇳🇱")
        self.assertEqual(get_flag("NZ"), "🇳🇿")
        self.assertEqual(get_flag("NG"), "🇳🇬")
        self.assertEqual(get_flag("MK"), "🇲🇰")
        self.assertEqual(get_flag("NO"), "🇳🇴")
        self.assertEqual(get_flag("PK"), "🇵🇰")
        self.assertEqual(get_flag("PH"), "🇵🇭")
        self.assertEqual(get_flag("PL"), "🇵🇱")
        self.assertEqual(get_flag("PT"), "🇵🇹")
        self.assertEqual(get_flag("PR"), "🇵🇷")
        self.assertEqual(get_flag("RO"), "🇷🇴")
        self.assertEqual(get_flag("SM"), "🇸🇲")
        self.assertEqual(get_flag("SA"), "🇸🇦")
        self.assertEqual(get_flag("RS"), "🇷🇸")
        self.assertEqual(get_flag("SG"), "🇸🇬")
        self.assertEqual(get_flag("SK"), "🇸🇰")
        self.assertEqual(get_flag("SI"), "🇸🇮")
        self.assertEqual(get_flag("ZA"), "🇿🇦")
        self.assertEqual(get_flag("KR"), "🇰🇷")
        self.assertEqual(get_flag("ES"), "🇪🇸")
        self.assertEqual(get_flag("SE"), "🇸🇪")
        self.assertEqual(get_flag("CH"), "🇨🇭")
        self.assertEqual(get_flag("TH"), "🇹🇭")
        self.assertEqual(get_flag("TT"), "🇹🇹")
        self.assertEqual(get_flag("TR"), "🇹🇷")
        self.assertEqual(get_flag("UA"), "🇺🇦")
        self.assertEqual(get_flag("AE"), "🇦🇪")
        self.assertEqual(get_flag("US"), "🇺🇸")
        self.assertEqual(get_flag("UY"), "🇺🇾")
        self.assertEqual(get_flag("UZ"), "🇺🇿")
        self.assertEqual(get_flag("VE"), "🇻🇪")


if __name__ == "__main__":

    unittest.main(verbosity=2)
