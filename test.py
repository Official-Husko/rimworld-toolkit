from bs4 import BeautifulSoup as bs4

with open(".\data\datasets\example_about.xml", "r") as f:
    data = f.read()
    Bs_data = bs4(data, "xml")

with open("test_output.xml", "a") as test:
    test.write(data)

print(Bs_data)