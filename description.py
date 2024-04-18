import streamlit as st


html_string = "<h1 style='text-align: center; font-family: Times New Roman, Times, serif; font-weight: bold;'>Description</h1><p style='text-align: left; font-family: Times New Roman, Times, serif;'>This application simulates the impact of sea level rise on the Andaman and Nicobar Islands in terms of loss of land used for various purposes. The climate models used here are RCP 2.6, RCP 4.5 and RCP 8.5. The simulation is presented for the years 2050 to 2300. The simulation takes into account the rise in sea level. The rise of land due to GIA and tectonics is not taken into account. To use this application, first select the climate model which is needed to be used for the analysis. Then select the year from the slidebar. The simulation results are as displayed.</p>"

st.markdown(html_string, unsafe_allow_html=True)

html_string = "<h1 style='text-align: center; font-family: Times New Roman, Times, serif; font-weight: bold;'>Dataset Credits</h1><p style='text-align: left; font-family: Times New Roman, Times, serif;'>Assessment of change in the extent of mangrove ecosystems using different spectral indices in Google Earth Engine based on random forest model by Kolli et.al. <br> Available at: https://link.springer.com/article/10.1007/s12517-022-10158-7 </p>"

st.markdown(html_string, unsafe_allow_html=True)

html_string = "<p style='text-align: center; font-family: Times New Roman, Times, serif; font-style: oblique;'>\"The greatest threat to our planet is the belief that someone else will save it\"</p>"

st.markdown(html_string, unsafe_allow_html=True)

html_string = "<p style='text-align: center; font-family: Times New Roman, Times, serif;'>Application made by JaidevSK</p>"

st.markdown(html_string, unsafe_allow_html=True)
