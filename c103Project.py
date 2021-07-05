import pandas as pd
import plotly.express as px

df = pd.read_csv("C:/Users/sango/OneDriveXX/Documents/whiteHatJr/python/Copy+of+data+-+data.csv")
fig= px.scatter(df,x="date",y="cases",title="Covid Cases",color="country",size="cases")

fig.show()