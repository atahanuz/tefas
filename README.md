# tefas
Get daily price data of 5 years from TEFAS, Turkey's exchange traded funds platform. (in Turkish: Yatırım Fonları) <br>
https://www.tefas.gov.tr

TEFAS doesn't provice an API for easy data retrieval, so the program uses Selenium to physically visit the website and scrape the data.


## Installation
```
pip install tefas
```

## Usage

```python
import tefas

data= tefas.get_data("AFT","MAC","TCD")
```
call tefas.get_data() function with the ETF names. You can pass a single or as many ETFs as you want.
You will get a Pandas dataframe with days as indexes and each ETFs daily prices as columns.

You can pass an optional verbose=False argument if you want to disable printing scraping progression to the console.

```python
import tefas

data= tefas.get_data("IPJ",verbose=False)
```

### Example Dataframe
<img src="https://i.imgur.com/0uSyTcH.png" width="50%" height="50%">




## Additional Features ?

Initially, I thougt about adding various data manipulation functions to the library. But to keep the library lightweight, I think it is enough to retrieve the dataframe. Because once the dataframe is ready, users can easily process the data according to their needs using the Pandas library.
Examples:

```python
import tefas

data= tefas.get_data("AFT","MAC","TCD")

# print the correlation matrix between ETFs
print(data.corr(),"\n")

#print total percentage return for each ETF
for column in data:
    print(f"{column} total return: {data[column].iloc[-1] / data[column].iloc[0] * 100 - 100:.2f} %")
```
### Output
<img src="https://i.imgur.com/nKX6Idi.png" width="50%" height="50%">




## Contact
Raise an issue on the GitHub repo:
https://github.com/atahanuz/tefas/
<br>

*Disclaimer: This program doesn't provide any investment advice, it simply displays data based on user request.*



