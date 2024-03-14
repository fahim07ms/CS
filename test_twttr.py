from twttr import shorten

def main():
	test_shorten()

def test_shorten():
	assert shorten("Twitter") == "Twttr"
	assert shorten("65") == "65"
	assert shorten("fAhIm") == "fhm"