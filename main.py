import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import PIL

# Read all image files
bl26050 = PIL.Image.open("Builtland_segmented_2050_RCP26.png")
cl26050 = PIL.Image.open("Cropland_segmented_2050_RCP26.png")
gl26050 = PIL.Image.open("Grassland_segmented_2050_RCP26.png")
ml26050 = PIL.Image.open("Mangrooveland_segmented_2050_RCP26.png")
fl26050 = PIL.Image.open("Forestland_segmented_2050_RCP26.png")
bl26100 = PIL.Image.open("Builtland_segmented_2100_RCP26.png")
cl26100 = PIL.Image.open("Cropland_segmented_2100_RCP26.png")
gl26100 = PIL.Image.open("Grassland_segmented_2100_RCP26.png")
ml26100 = PIL.Image.open("Mangrooveland_segmented_2100_RCP26.png")
fl26100 = PIL.Image.open("Forestland_segmented_2100_RCP26.png")
bl26150 = PIL.Image.open("Builtland_segmented_2150_RCP26.png")
cl26150 = PIL.Image.open("Cropland_segmented_2150_RCP26.png")
gl26150 = PIL.Image.open("Grassland_segmented_2150_RCP26.png")
ml26150 = PIL.Image.open("Mangrooveland_segmented_2150_RCP26.png")
fl26150 = PIL.Image.open("Forestland_segmented_2150_RCP26.png")
bl26200 = PIL.Image.open("Builtland_segmented_2200_RCP26.png")
cl26200 = PIL.Image.open("Cropland_segmented_2200_RCP26.png")
gl26200 = PIL.Image.open("Grassland_segmented_2200_RCP26.png")
ml26200 = PIL.Image.open("Mangrooveland_segmented_2200_RCP26.png")
fl26200 = PIL.Image.open("Forestland_segmented_2200_RCP26.png")
bl26250 = PIL.Image.open("Builtland_segmented_2250_RCP26.png")
cl26250 = PIL.Image.open("Cropland_segmented_2250_RCP26.png")
gl26250 = PIL.Image.open("Grassland_segmented_2250_RCP26.png")
ml26250 = PIL.Image.open("Mangrooveland_segmented_2250_RCP26.png")
fl26250 = PIL.Image.open("Forestland_segmented_2250_RCP26.png")
bl26300 = PIL.Image.open("Builtland_segmented_2300_RCP26.png")
cl26300 = PIL.Image.open("Cropland_segmented_2300_RCP26.png")
gl26300 = PIL.Image.open("Grassland_segmented_2300_RCP26.png")
ml26300 = PIL.Image.open("Mangrooveland_segmented_2300_RCP26.png")
fl26300 = PIL.Image.open("Forestland_segmented_2300_RCP26.png")

bl45050 = PIL.Image.open("Builtland_segmented_2050_RCP45.png")
cl45050 = PIL.Image.open("Cropland_segmented_2050_RCP45.png")
gl45050 = PIL.Image.open("Grassland_segmented_2050_RCP45.png")
ml45050 = PIL.Image.open("Mangrooveland_segmented_2050_RCP45.png")
fl45050 = PIL.Image.open("Forestland_segmented_2050_RCP45.png")
bl45100 = PIL.Image.open("Builtland_segmented_2100_RCP45.png")
cl45100 = PIL.Image.open("Cropland_segmented_2100_RCP45.png")
gl45100 = PIL.Image.open("Grassland_segmented_2100_RCP45.png")
ml45100 = PIL.Image.open("Mangrooveland_segmented_2100_RCP45.png")
fl45100 = PIL.Image.open("Forestland_segmented_2100_RCP45.png")
bl45150 = PIL.Image.open("Builtland_segmented_2150_RCP45.png")
cl45150 = PIL.Image.open("Cropland_segmented_2150_RCP45.png")
gl45150 = PIL.Image.open("Grassland_segmented_2150_RCP45.png")
ml45150 = PIL.Image.open("Mangrooveland_segmented_2150_RCP45.png")
fl45150 = PIL.Image.open("Forestland_segmented_2150_RCP45.png")
bl45200 = PIL.Image.open("Builtland_segmented_2200_RCP45.png")
cl45200 = PIL.Image.open("Cropland_segmented_2200_RCP45.png")
gl45200 = PIL.Image.open("Grassland_segmented_2200_RCP45.png")
ml45200 = PIL.Image.open("Mangrooveland_segmented_2200_RCP45.png")
fl45200 = PIL.Image.open("Forestland_segmented_2200_RCP45.png")
bl45250 = PIL.Image.open("Builtland_segmented_2250_RCP45.png")
cl45250 = PIL.Image.open("Cropland_segmented_2250_RCP45.png")
gl45250 = PIL.Image.open("Grassland_segmented_2250_RCP45.png")
ml45250 = PIL.Image.open("Mangrooveland_segmented_2250_RCP45.png")
fl45250 = PIL.Image.open("Forestland_segmented_2250_RCP45.png")
bl45300 = PIL.Image.open("Builtland_segmented_2300_RCP45.png")
cl45300 = PIL.Image.open("Cropland_segmented_2300_RCP45.png")
gl45300 = PIL.Image.open("Grassland_segmented_2300_RCP45.png")
ml45300 = PIL.Image.open("Mangrooveland_segmented_2300_RCP45.png")
fl45300 = PIL.Image.open("Forestland_segmented_2300_RCP45.png")

bl85050 = PIL.Image.open("Builtland_segmented_2050_RCP85.png")
cl85050 = PIL.Image.open("Cropland_segmented_2050_RCP85.png")
gl85050 = PIL.Image.open("Grassland_segmented_2050_RCP85.png")
ml85050 = PIL.Image.open("Mangrooveland_segmented_2050_RCP85.png")
fl85050 = PIL.Image.open("Forestland_segmented_2050_RCP85.png")
bl85100 = PIL.Image.open("Builtland_segmented_2100_RCP85.png")
cl85100 = PIL.Image.open("Cropland_segmented_2100_RCP85.png")
gl85100 = PIL.Image.open("Grassland_segmented_2100_RCP85.png")
ml85100 = PIL.Image.open("Mangrooveland_segmented_2100_RCP85.png")
fl85100 = PIL.Image.open("Forestland_segmented_2100_RCP85.png")
bl85150 = PIL.Image.open("Builtland_segmented_2150_RCP85.png")
cl85150 = PIL.Image.open("Cropland_segmented_2150_RCP85.png")
gl85150 = PIL.Image.open("Grassland_segmented_2150_RCP85.png")
ml85150 = PIL.Image.open("Mangrooveland_segmented_2150_RCP85.png")
fl85150 = PIL.Image.open("Forestland_segmented_2150_RCP85.png")
bl85200 = PIL.Image.open("Builtland_segmented_2200_RCP85.png")
cl85200 = PIL.Image.open("Cropland_segmented_2200_RCP85.png")
gl85200 = PIL.Image.open("Grassland_segmented_2200_RCP85.png")
ml85200 = PIL.Image.open("Mangrooveland_segmented_2200_RCP85.png")
fl85200 = PIL.Image.open("Forestland_segmented_2200_RCP85.png")
bl85250 = PIL.Image.open("Builtland_segmented_2250_RCP85.png")
cl85250 = PIL.Image.open("Cropland_segmented_2250_RCP85.png")
gl85250 = PIL.Image.open("Grassland_segmented_2250_RCP85.png")
ml85250 = PIL.Image.open("Mangrooveland_segmented_2250_RCP85.png")
fl85250 = PIL.Image.open("Forestland_segmented_2250_RCP85.png")
bl85300 = PIL.Image.open("Builtland_segmented_2300_RCP85.png")
cl85300 = PIL.Image.open("Cropland_segmented_2300_RCP85.png")
gl85300 = PIL.Image.open("Grassland_segmented_2300_RCP85.png")
ml85300 = PIL.Image.open("Mangrooveland_segmented_2300_RCP85.png")
fl85300 = PIL.Image.open("Forestland_segmented_2300_RCP85.png")


import streamlit as st

html_string = "<h1 style='text-align: center; font-family: Times New Roman, Times, serif; font-weight: bold;'>Impact of Sea Level Rise on Andaman</h1><br><h2 style='text-align: center; font-family: Times New Roman, Times, serif; font-weight: bold;'>Ocean and Global Change</h2>"

st.markdown(html_string, unsafe_allow_html=True)


background_image = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background-image: url("https://static.independent.co.uk/2021/09/07/11/sea-and-sky.jpg");
    background-size: 100vw 100vh;  # This sets the size to cover 100% of the viewport width and height
    background-position: center;  
    background-repeat: no-repeat;
}
</style>
"""

st.markdown(background_image, unsafe_allow_html=True)


year =  st.select_slider(
    'Select the Year',
    options=[2050, 2100, 2150, 2200, 2250, 2300])
st.write('You selected:', year)

model = st.radio(
    "Select the Climate Model",
    ["RCP 2.6", "RCP 4.5", "RCP 8.5"],
    index=None,
)
st.write('You selected:', model)

st.write("The simulation results are as displayed.")

rcp26res = {2050: [40.99988015819119, 73.14248682245899, 4.384034687423282, 37.869158715332034, 3.408355003944085], 2100: [40.99988015819119, 73.14248682245899, 4.384034687423282, 37.869158715332034, 3.408355003944085], 2150: [40.99988015819119, 73.14248682245899, 4.384034687423282, 37.869158715332034, 3.408355003944085], 2200: [40.99988015819119, 73.14248682245899, 4.384034687423282, 37.869158715332034, 3.408355003944085], 2250: [43.46573633914344, 74.32215980955853, 5.454568428957211, 40.085202224336754, 3.5883774243680557], 2300: [43.46573633914344, 74.32215980955853, 5.454568428957211, 40.085202224336754, 3.5883774243680557]}
rcp45res = {2050: [43.46573633914344, 74.32215980955853, 5.454568428957211, 40.085202224336754, 3.5883774243680557], 2100: [43.46573633914344, 74.32215980955853, 5.454568428957211, 40.085202224336754, 3.5883774243680557], 2150: [43.46573633914344, 74.32215980955853, 5.454568428957211, 40.085202224336754, 3.5883774243680557], 2200: [46.021473876704974, 75.51803431407747, 6.633500368247, 42.64301490165952, 3.786556756825822], 2250: [46.021473876704974, 75.51803431407747, 6.633500368247, 42.64301490165952, 3.786556756825822], 2300: [48.69350235466962, 76.72679638927092, 7.857289846491544, 45.614617070125966, 4.0052802990107175]}
rcp85res = {2050: [48.69350235466962, 76.72679638927092, 7.857289846491544, 45.614617070125966, 4.0052802990107175], 2100: [48.69350235466962, 76.72679638927092, 7.857289846491544, 45.614617070125966, 4.0052802990107175], 2150: [51.40259302165586, 77.8547349855199, 9.117813768105478, 48.93933706384056, 4.242967727097578], 2200: [51.40259302165586, 77.8547349855199, 9.117813768105478, 48.93933706384056, 4.242967727097578], 2250: [54.124111728074496, 78.9232066485136, 10.384384883099628, 52.59666000296811, 4.4972653673042435], 2300: [59.540073769291205, 80.90108053074698, 12.918790705734546, 60.011697846374105, 5.0188731013417955]}

if model == "RCP 2.6":
    st.write("Loss of land for various purposes in the year ", year, " for RCP 2.6")
    st.write("Settlement Land: ", rcp26res[year][0], "%")
    st.write("Agricultural Land: ", rcp26res[year][1], "%")
    st.write("Grass Land: ", rcp26res[year][2], "%")
    st.write("Mangroove Land: ", rcp26res[year][3], "%")
    st.write("Forest Land: ", rcp26res[year][4], "%")
    if year == 2050:
        fig, axes = plt.subplots(1, 5)
        fig.suptitle("Remaining Land in the year 2050 for RCP 2.6")
        plt.subplots_adjust(left=0.1,
                            bottom=0.1, 
                            right=0.9, 
                            top=0.9, 
                            wspace=0.4, 
                            hspace=0.4)
        # Plot something on each subplot
        axes[0].imshow(bl26050)
        axes[0].set_title("Settlement")
        axes[0].axis("off")
        axes[1].imshow(cl26050)
        axes[1].set_title("Agricultural")
        axes[1].axis("off")
        axes[2].imshow(gl26050)
        axes[2].set_title("Grasslands")
        axes[2].axis("off")
        axes[3].imshow(ml26050)
        axes[3].set_title("Mangrooves")
        axes[3].axis("off")
        axes[4].imshow(fl26050)
        axes[4].set_title("Forests")
        axes[4].axis("off")
        st.pyplot(fig)

        img = PIL.Image.open('Elevation_2050_RCP26.png')
        z_data = np.array(img)
        z = z_data.transpose()
        sh_0, sh_1 = z.shape
        z = z/255*0.7
        x, y = np.linspace(0, 360, sh_0), np.linspace(0, 180, sh_1)
        xv, yv = np.meshgrid(x, y)
        fig = go.Figure(data=[go.Surface(z=z[::10], x=xv[::10], y=yv[::10])])
        fig.update_layout(title='Sea Level Impact on Andaman in Year 2050 for RCP 2.6', height = 500, width = 5000)
        st.plotly_chart(fig, use_container_width=True)
        fig = go.Figure(data =
    go.Contour(
        z=z[::10, ::10],
        colorscale='Hot',
        contours=dict(
            start=0,
            end=0.7,
            size=0.05,
        ),
    ))
        fig.update_layout(title='Sea Level Impact on Andaman in Year 2050 for RCP 2.6') 
        st.plotly_chart(fig, use_container_width=True)

    if year == 2100:

        fig, axes = plt.subplots(1, 5)
        fig.suptitle("Remaining Land in the year 2100 for RCP 2.6")
        plt.subplots_adjust(left=0.1,
                            bottom=0.1, 
                            right=0.9, 
                            top=0.9, 
                            wspace=0.4, 
                            hspace=0.4)
        # Plot something on each subplot
        axes[0].imshow(bl26100)
        axes[0].set_title("Settlement")
        axes[0].axis("off")
        axes[1].imshow(cl26100)
        axes[1].set_title("Agricultural")
        axes[1].axis("off")
        axes[2].imshow(gl26100)
        axes[2].set_title("Grasslands")
        axes[2].axis("off")
        axes[3].imshow(ml26100)
        axes[3].set_title("Mangrooves")
        axes[3].axis("off")
        axes[4].imshow(fl26100)
        axes[4].set_title("Forests")
        axes[4].axis("off")
        st.pyplot(fig)

        img = PIL.Image.open('Elevation_2100_RCP26.png')
        z_data = np.array(img)
        z = z_data.transpose()
        sh_0, sh_1 = z.shape
        z = z/255*0.7
        x, y = np.linspace(0, 360, sh_0), np.linspace(0, 180, sh_1)
        xv, yv = np.meshgrid(x, y)
        fig = go.Figure(data=[go.Surface(z=z[::10], x=xv[::10], y=yv[::10])])
        fig.update_layout(title='Sea Level Impact on Andaman in Year 2100 for RCP 2.6', height = 500, width = 5000)
        st.plotly_chart(fig, use_container_width=True)
        fig = go.Figure(data =
    go.Contour(
        z=z[::10, ::10],
        colorscale='Hot',
        contours=dict(
            start=0,
            end=0.7,
            size=0.05,
        ),
    ))
        fig.update_layout(title='Sea Level Impact on Andaman in Year 2100 for RCP 2.6') 
        st.plotly_chart(fig, use_container_width=True)
    elif year == 2150:
        fig, axes = plt.subplots(1, 5)
        fig.suptitle("Remaining Land in the year 2150 for RCP 2.6")
        plt.subplots_adjust(left=0.1,
                            bottom=0.1, 
                            right=0.9, 
                            top=0.9, 
                            wspace=0.4, 
                            hspace=0.4)
        # Plot something on each subplot
        axes[0].imshow(bl26150)
        axes[0].set_title("Settlement")
        axes[0].axis("off")
        axes[1].imshow(cl26150)
        axes[1].set_title("Agricultural")
        axes[1].axis("off")
        axes[2].imshow(gl26150)
        axes[2].set_title("Grasslands")
        axes[2].axis("off")
        axes[3].imshow(ml26150)
        axes[3].set_title("Mangrooves")
        axes[3].axis("off")
        axes[4].imshow(fl26150)
        axes[4].set_title("Forests")
        axes[4].axis("off")
        st.pyplot(fig)

        img = PIL.Image.open('Elevation_2150_RCP26.png')
        z_data = np.array(img)
        z = z_data.transpose()
        sh_0, sh_1 = z.shape
        z = z/255*0.7
        x, y = np.linspace(0, 360, sh_0), np.linspace(0, 180, sh_1)
        xv, yv = np.meshgrid(x, y)
        fig = go.Figure(data=[go.Surface(z=z[::10], x=xv[::10], y=yv[::10])])
        fig.update_layout(title='Sea Level Impact on Andaman in Year 2150 for RCP 2.6', height = 500, width = 5000)
        st.plotly_chart(fig, use_container_width=True)
        fig = go.Figure(data =
    go.Contour(
        z=z[::10, ::10],
        colorscale='Hot',
        contours=dict(
            start=0,
            end=0.7,
            size=0.05,
        ),
    ))
        fig.update_layout(title='Sea Level Impact on Andaman in Year 2150 for RCP 2.6') 
        st.plotly_chart(fig, use_container_width=True)
    elif year == 2200:
        fig, axes = plt.subplots(1, 5)
        fig.suptitle("Remaining Land in the year 2200 for RCP 2.6")
        plt.subplots_adjust(left=0.1,
                            bottom=0.1, 
                            right=0.9, 
                            top=0.9, 
                            wspace=0.4, 
                            hspace=0.4)
        # Plot something on each subplot
        axes[0].imshow(bl26200)
        axes[0].set_title("Settlement")
        axes[0].axis("off")
        axes[1].imshow(cl26200)
        axes[1].set_title("Agricultural")
        axes[1].axis("off")
        axes[2].imshow(gl26200)
        axes[2].set_title("Grasslands")
        axes[2].axis("off")
        axes[3].imshow(ml26200)
        axes[3].set_title("Mangrooves")
        axes[3].axis("off")
        axes[4].imshow(fl26200)
        axes[4].set_title("Forests")
        axes[4].axis("off")
        st.pyplot(fig)

        img = PIL.Image.open('Elevation_2200_RCP26.png')
        z_data = np.array(img)
        z = z_data.transpose()
        sh_0, sh_1 = z.shape
        z = z/255*0.7
        x, y = np.linspace(0, 360, sh_0), np.linspace(0, 180, sh_1)
        xv, yv = np.meshgrid(x, y)
        fig = go.Figure(data=[go.Surface(z=z[::10], x=xv[::10], y=yv[::10])])
        fig.update_layout(title='Sea Level Impact on Andaman in Year 2200 for RCP 2.6', height = 500, width = 5000)
        st.plotly_chart(fig, use_container_width=True)
        fig = go.Figure(data =
    go.Contour(
        z=z[::10, ::10],
        colorscale='Hot',
        contours=dict(
            start=0,
            end=0.7,
            size=0.05,
        ),
    ))
        fig.update_layout(title='Sea Level Impact on Andaman in Year 2200 for RCP 2.6') 
        st.plotly_chart(fig, use_container_width=True)
    elif year == 2250:
        fig, axes = plt.subplots(1, 5)
        fig.suptitle("Remaining Land in the year 2250 for RCP 2.6")
        plt.subplots_adjust(left=0.1,
                            bottom=0.1, 
                            right=0.9, 
                            top=0.9, 
                            wspace=0.4, 
                            hspace=0.4)
        # Plot something on each subplot
        axes[0].imshow(bl26250)
        axes[0].set_title("Settlement")
        axes[0].axis("off")
        axes[1].imshow(cl26250)
        axes[1].set_title("Agricultural")
        axes[1].axis("off")
        axes[2].imshow(gl26250)
        axes[2].set_title("Grasslands")
        axes[2].axis("off")
        axes[3].imshow(ml26250)
        axes[3].set_title("Mangrooves")
        axes[3].axis("off")
        axes[4].imshow(fl26250)
        axes[4].set_title("Forests")
        axes[4].axis("off")
        st.pyplot(fig)

        img = PIL.Image.open('Elevation_2250_RCP26.png')
        z_data = np.array(img)
        z = z_data.transpose()
        sh_0, sh_1 = z.shape
        z = z/255*0.7
        x, y = np.linspace(0, 360, sh_0), np.linspace(0, 180, sh_1)
        xv, yv = np.meshgrid(x, y)
        fig = go.Figure(data=[go.Surface(z=z[::10], x=xv[::10], y=yv[::10])])
        fig.update_layout(title='Sea Level Impact on Andaman in Year 2250 for RCP 2.6', height = 500, width = 5000)
        st.plotly_chart(fig, use_container_width=True)
        fig = go.Figure(data =
    go.Contour(
        z=z[::10, ::10],
        colorscale='Hot',
        contours=dict(
            start=0,
            end=0.7,
            size=0.05,
        ),
    ))
        fig.update_layout(title='Sea Level Impact on Andaman in Year 2250 for RCP 2.6') 
        st.plotly_chart(fig, use_container_width=True)
    elif year == 2300:
        fig, axes = plt.subplots(1, 5)
        fig.suptitle("Remaining Land in the year 2300 for RCP 2.6")
        plt.subplots_adjust(left=0.1,
                            bottom=0.1, 
                            right=0.9, 
                            top=0.9, 
                            wspace=0.4, 
                            hspace=0.4)
        # Plot something on each subplot
        axes[0].imshow(bl26300)
        axes[0].set_title("Settlement")
        axes[0].axis("off")
        axes[1].imshow(cl26300)
        axes[1].set_title("Agricultural")
        axes[1].axis("off")
        axes[2].imshow(gl26300)
        axes[2].set_title("Grasslands")
        axes[2].axis("off")
        axes[3].imshow(ml26300)
        axes[3].set_title("Mangrooves")
        axes[3].axis("off")
        axes[4].imshow(fl26300)
        axes[4].set_title("Forests")
        axes[4].axis("off")
        st.pyplot(fig)

        img = PIL.Image.open('Elevation_2300_RCP26.png')
        z_data = np.array(img)
        z = z_data.transpose()
        sh_0, sh_1 = z.shape
        z = z/255*0.7
        x, y = np.linspace(0, 360, sh_0), np.linspace(0, 180, sh_1)
        xv, yv = np.meshgrid(x, y)
        fig = go.Figure(data=[go.Surface(z=z[::10], x=xv[::10], y=yv[::10])])
        fig.update_layout(title='Sea Level Impact on Andaman in Year 2300 for RCP 2.6', height = 500, width = 5000)
        st.plotly_chart(fig, use_container_width=True)
        fig = go.Figure(data =
    go.Contour(
        z=z[::10, ::10],
        colorscale='Hot',
        contours=dict(
            start=0,
            end=0.7,
            size=0.05,
        ),
    ))
        fig.update_layout(title='Sea Level Impact on Andaman in Year 2300 for RCP 2.6') 
        st.plotly_chart(fig, use_container_width=True)



#########################################
#####################################
#####################################




elif model == "RCP 4.5":
    st.write("Loss of land for various purposes in the year ", year, " for RCP 4.5")
    st.write("Settlement Land: ", rcp45res[year][0], "%")
    st.write("Agricultural Land: ", rcp45res[year][1], "%")
    st.write("Grass Land: ", rcp45res[year][2], "%")
    st.write("Mangroove Land: ", rcp45res[year][3], "%")
    st.write("Forest Land: ", rcp45res[year][4], "%")
    if year == 2050:
        fig, axes = plt.subplots(1, 5)
        fig.suptitle("Remaining Land in the year 2050 for RCP 4.5")
        plt.subplots_adjust(left=0.1,
                            bottom=0.1, 
                            right=0.9, 
                            top=0.9, 
                            wspace=0.4, 
                            hspace=0.4)
        # Plot something on each subplot
        axes[0].imshow(bl45050)
        axes[0].set_title("Settlement")
        axes[0].axis("off")
        axes[1].imshow(cl45050)
        axes[1].set_title("Agricultural")
        axes[1].axis("off")
        axes[2].imshow(gl45050)
        axes[2].set_title("Grasslands")
        axes[2].axis("off")
        axes[3].imshow(ml45050)
        axes[3].set_title("Mangrooves")
        axes[3].axis("off")
        axes[4].imshow(fl45050)
        axes[4].set_title("Forests")
        axes[4].axis("off")
        st.pyplot(fig)

        img = PIL.Image.open('Elevation_2050_RCP45.png')
        z_data = np.array(img)
        z = z_data.transpose()
        sh_0, sh_1 = z.shape
        z = z/255*0.7
        x, y = np.linspace(0, 360, sh_0), np.linspace(0, 180, sh_1)
        xv, yv = np.meshgrid(x, y)
        fig = go.Figure(data=[go.Surface(z=z[::10], x=xv[::10], y=yv[::10])])
        fig.update_layout(title='Sea Level Impact on Andaman in Year 2050 for RCP 4.5', height = 500, width = 5000)
        st.plotly_chart(fig, use_container_width=True)
        fig = go.Figure(data =
    go.Contour(
        z=z[::10, ::10],
        colorscale='Hot',
        contours=dict(
            start=0,
            end=0.7,
            size=0.05,
        ),
    ))
        fig.update_layout(title='Sea Level Impact on Andaman in Year 2050 for RCP 4.5') 
        st.plotly_chart(fig, use_container_width=True)

    if year == 2100:
            
            fig, axes = plt.subplots(1, 5)
            fig.suptitle("Remaining Land in the year 2100 for RCP 4.5")
            plt.subplots_adjust(left=0.1,
                                bottom=0.1, 
                                right=0.9, 
                                top=0.9, 
                                wspace=0.4, 
                                hspace=0.4)
            # Plot something on each subplot
            axes[0].imshow(bl45100)
            axes[0].set_title("Settlement")
            axes[0].axis("off")
            axes[1].imshow(cl45100)
            axes[1].set_title("Agricultural")
            axes[1].axis("off")
            axes[2].imshow(gl45100)
            axes[2].set_title("Grasslands")
            axes[2].axis("off")
            axes[3].imshow(ml45100)
            axes[3].set_title("Mangrooves")
            axes[3].axis("off")
            axes[4].imshow(fl45100)
            axes[4].set_title("Forests")
            axes[4].axis("off")
            st.pyplot(fig)
    
            img = PIL.Image.open('Elevation_2100_RCP45.png')
            z_data = np.array(img)
            z = z_data.transpose()
            sh_0, sh_1 = z.shape
            z = z/255*0.7
            x, y = np.linspace(0, 360, sh_0), np.linspace(0, 180, sh_1)
            xv, yv = np.meshgrid(x, y)
            fig = go.Figure(data=[go.Surface(z=z[::10], x=xv[::10], y=yv[::10])])
            fig.update_layout(title='Sea Level Impact on Andaman in Year 2100 for RCP 4.5', height = 500, width = 5000)
            st.plotly_chart(fig, use_container_width=True)
            fig = go.Figure(data =
        go.Contour(
            z=z[::10, ::10],
            colorscale='Hot',
            contours=dict(
                start=0,
                end=0.7,
                size=0.05,
            ),
        ))
            fig.update_layout(title='Sea Level Impact on Andaman in Year 2100 for RCP 4.5')
            st.plotly_chart(fig, use_container_width=True)
    elif year == 2150:
        fig, axes = plt.subplots(1, 5)
        fig.suptitle("Remaining Land in the year 2150 for RCP 4.5")
        plt.subplots_adjust(left=0.1,
                            bottom=0.1, 
                            right=0.9, 
                            top=0.9, 
                            wspace=0.4, 
                            hspace=0.4)
        # Plot something on each subplot
        axes[0].imshow(bl45150)
        axes[0].set_title("Settlement")
        axes[0].axis("off")
        axes[1].imshow(cl45150)
        axes[1].set_title("Agricultural")
        axes[1].axis("off")
        axes[2].imshow(gl45150)
        axes[2].set_title("Grasslands")
        axes[2].axis("off")
        axes[3].imshow(ml45150)
        axes[3].set_title("Mangrooves")
        axes[3].axis("off")
        axes[4].imshow(fl45150)
        axes[4].set_title("Forests")
        axes[4].axis("off")
        st.pyplot(fig)

        img = PIL.Image.open('Elevation_2150_RCP45.png')
        z_data = np.array(img)
        z = z_data.transpose()
        sh_0, sh_1 = z.shape
        z = z/255*0.7
        x, y = np.linspace(0, 360, sh_0), np.linspace(0, 180, sh_1)
        xv, yv = np.meshgrid(x, y)
        fig = go.Figure(data=[go.Surface(z=z[::10], x=xv[::10], y=yv[::10])])
        fig.update_layout(title='Sea Level Impact on Andaman in Year 2150 for RCP 4.5', height = 500, width = 5000)
        st.plotly_chart(fig, use_container_width=True)
        fig = go.Figure(data =
    go.Contour(
        z=z[::10, ::10],
        colorscale='Hot',
        contours=dict(
            start=0,
            end=0.7,
            size=0.05,
        ),
    ))
        fig.update_layout(title='Sea Level Impact on Andaman in Year 2150 for RCP 4.5') 
        st.plotly_chart(fig, use_container_width=True)
    elif year == 2200:
        fig, axes = plt.subplots(1, 5)
        fig.suptitle("Remaining Land in the year 2200 for RCP 4.5")
        plt.subplots_adjust(left=0.1,
                            bottom=0.1, 
                            right=0.9, 
                            top=0.9, 
                            wspace=0.4, 
                            hspace=0.4)
        # Plot something on each subplot
        axes[0].imshow(bl45200)
        axes[0].set_title("Settlement")
        axes[0].axis("off")
        axes[1].imshow(cl45200)
        axes[1].set_title("Agricultural")
        axes[1].axis("off")
        axes[2].imshow(gl45200)
        axes[2].set_title("Grasslands")
        axes[2].axis("off")
        axes[3].imshow(ml45200)
        axes[3].set_title("Mangrooves")
        axes[3].axis("off")
        axes[4].imshow(fl45200)
        axes[4].set_title("Forests")
        axes[4].axis("off")
        st.pyplot(fig)

        img = PIL.Image.open('Elevation_2200_RCP45.png')
        z_data = np.array(img)
        z = z_data.transpose()
        sh_0, sh_1 = z.shape
        z = z/255*0.7
        x, y = np.linspace(0, 360, sh_0), np.linspace(0, 180, sh_1)
        xv, yv = np.meshgrid(x, y)
        fig = go.Figure(data=[go.Surface(z=z[::10], x=xv[::10], y=yv[::10])])
        fig.update_layout(title='Sea Level Impact on Andaman in Year 2200 for RCP 4.5', height = 500, width = 5000)
        st.plotly_chart(fig, use_container_width=True)
        fig = go.Figure(data =
    go.Contour(
        z=z[::10, ::10],
        colorscale='Hot',
        contours=dict(
            start=0,
            end=0.7,
            size=0.05,
        ),
    ))
        fig.update_layout(title='Sea Level Impact on Andaman in Year 2200 for RCP 4.5') 
        st.plotly_chart(fig, use_container_width=True)
    elif year == 2250:
        fig, axes = plt.subplots(1, 5)
        fig.suptitle("Remaining Land in the year 2250 for RCP 4.5")
        plt.subplots_adjust(left=0.1,
                            bottom=0.1, 
                            right=0.9, 
                            top=0.9, 
                            wspace=0.4, 
                            hspace=0.4)
        # Plot something on each subplot
        axes[0].imshow(bl45250)
        axes[0].set_title("Settlement")
        axes[0].axis("off")
        axes[1].imshow(cl45250)
        axes[1].set_title("Agricultural")
        axes[1].axis("off")
        axes[2].imshow(gl45250)
        axes[2].set_title("Grasslands")
        axes[2].axis("off")
        axes[3].imshow(ml45250)
        axes[3].set_title("Mangrooves")
        axes[3].axis("off")
        axes[4].imshow(fl45250)
        axes[4].set_title("Forests")
        axes[4].axis("off")
        st.pyplot(fig)

        img = PIL.Image.open('Elevation_2250_RCP45.png')
        z_data = np.array(img)
        z = z_data.transpose()
        sh_0, sh_1 = z.shape
        z = z/255*0.7
        x, y = np.linspace(0, 360, sh_0), np.linspace(0, 180, sh_1)
        xv, yv = np.meshgrid(x, y)
        fig = go.Figure(data=[go.Surface(z=z[::10], x=xv[::10], y=yv[::10])])
        fig.update_layout(title='Sea Level Impact on Andaman in Year 2250 for RCP 4.5', height = 500, width = 5000)
        st.plotly_chart(fig, use_container_width=True)
        fig = go.Figure(data =
    go.Contour(
        z=z[::10, ::10],
        colorscale='Hot',
        contours=dict(
            start=0,
            end=0.7,
            size=0.05,
        ),
    ))
        fig.update_layout(title='Sea Level Impact on Andaman in Year 2250 for RCP 4.5') 
        st.plotly_chart(fig, use_container_width=True)
    elif year == 2300:
        fig, axes = plt.subplots(1, 5)
        fig.suptitle("Remaining Land in the year 2300 for RCP 4.5")
        plt.subplots_adjust(left=0.1,
                            bottom=0.1, 
                            right=0.9, 
                            top=0.9, 
                            wspace=0.4, 
                            hspace=0.4)
        # Plot something on each subplot
        axes[0].imshow(bl45300)
        axes[0].set_title("Settlement")
        axes[0].axis("off")
        axes[1].imshow(cl45300)
        axes[1].set_title("Agricultural")
        axes[1].axis("off")
        axes[2].imshow(gl45300)
        axes[2].set_title("Grasslands")
        axes[2].axis("off")
        axes[3].imshow(ml45300)
        axes[3].set_title("Mangrooves")
        axes[3].axis("off")
        axes[4].imshow(fl45300)
        axes[4].set_title("Forests")
        axes[4].axis("off")
        st.pyplot(fig)

        img = PIL.Image.open('Elevation_2300_RCP45.png')
        z_data = np.array(img)
        z = z_data.transpose()
        sh_0, sh_1 = z.shape
        z = z/255*0.7
        x, y = np.linspace(0, 360, sh_0), np.linspace(0, 180, sh_1)
        xv, yv = np.meshgrid(x, y)
        fig = go.Figure(data=[go.Surface(z=z[::10], x=xv[::10], y=yv[::10])])
        fig.update_layout(title='Sea Level Impact on Andaman in Year 2300 for RCP 4.5', height = 500, width = 5000)
        st.plotly_chart(fig, use_container_width=True)
        fig = go.Figure(data =
    go.Contour(
        z=z[::10, ::10],
        colorscale='Hot',
        contours=dict(
            start=0,
            end=0.7,
            size=0.05,
        ),
    ))
        fig.update_layout(title='Sea Level Impact on Andaman in Year 2300 for RCP 4.5') 
        st.plotly_chart(fig, use_container_width=True)


elif model == "RCP 8.5":
    st.write("Loss of land for various purposes in the year ", year, " for RCP 8.5")
    st.write("Settlement Land: ", rcp85res[year][0], "%")
    st.write("Agricultural Land: ", rcp85res[year][1], "%")
    st.write("Grass Land: ", rcp85res[year][2], "%")
    st.write("Mangroove Land: ", rcp85res[year][3], "%")
    st.write("Forest Land: ", rcp85res[year][4], "%")
    if year == 2050:
        fig, axes = plt.subplots(1, 5)
        fig.suptitle("Remaining Land in the year 2050 for RCP 8.5")
        plt.subplots_adjust(left=0.1,
                            bottom=0.1, 
                            right=0.9, 
                            top=0.9, 
                            wspace=0.4, 
                            hspace=0.4)
        # Plot something on each subplot
        axes[0].imshow(bl85050)
        axes[0].set_title("Settlement")
        axes[0].axis("off")
        axes[1].imshow(cl85050)
        axes[1].set_title("Agricultural")
        axes[1].axis("off")
        axes[2].imshow(gl85050)
        axes[2].set_title("Grasslands")
        axes[2].axis("off")
        axes[3].imshow(ml85050)
        axes[3].set_title("Mangrooves")
        axes[3].axis("off")
        axes[4].imshow(fl85050)
        axes[4].set_title("Forests")
        axes[4].axis("off")
        st.pyplot(fig)

        img = PIL.Image.open('Elevation_2050_RCP85.png')
        z_data = np.array(img)
        z = z_data.transpose()
        sh_0, sh_1 = z.shape
        z = z/255*0.7
        x, y = np.linspace(0, 360, sh_0), np.linspace(0, 180, sh_1)
        xv, yv = np.meshgrid(x, y)
        fig = go.Figure(data=[go.Surface(z=z[::10], x=xv[::10], y=yv[::10])])
        fig.update_layout(title='Sea Level Impact on Andaman in Year 2050 for RCP 8.5', height = 500, width = 5000)
        st.plotly_chart(fig, use_container_width=True)
        fig = go.Figure(data =
    go.Contour(
        z=z[::10, ::10],
        colorscale='Hot',
        contours=dict(
            start=0,
            end=0.7,
            size=0.05,
        ),
    ))
        fig.update_layout(title='Sea Level Impact on Andaman in Year 2050 for RCP 8.5') 
        st.plotly_chart(fig, use_container_width=True)

    if year == 2100:
        fig, axes = plt.subplots(1, 5)
        fig.suptitle("Remaining Land in the year 2100 for RCP 8.5")
        plt.subplots_adjust(left=0.1,
                            bottom=0.1, 
                            right=0.9, 
                            top=0.9, 
                            wspace=0.4, 
                            hspace=0.4)
        # Plot something on each subplot
        axes[0].imshow(bl85100)
        axes[0].set_title("Settlement")
        axes[0].axis("off")
        axes[1].imshow(cl85100)
        axes[1].set_title("Agricultural")
        axes[1].axis("off")
        axes[2].imshow(gl85100)
        axes[2].set_title("Grasslands")
        axes[2].axis("off")
        axes[3].imshow(ml85100)
        axes[3].set_title("Mangrooves")
        axes[3].axis("off")
        axes[4].imshow(fl85100)
        axes[4].set_title("Forests")
        axes[4].axis("off")
        st.pyplot(fig)

        img = PIL.Image.open('Elevation_2100_RCP85.png')
        z_data = np.array(img)
        z = z_data.transpose()
        sh_0, sh_1 = z.shape
        z = z/255*0.7
        x, y = np.linspace(0, 360, sh_0), np.linspace(0, 180, sh_1)
        xv, yv = np.meshgrid(x, y)
        fig = go.Figure(data=[go.Surface(z=z[::10], x=xv[::10], y=yv[::10])])
        fig.update_layout(title='Sea Level Impact on Andaman in Year 2100 for RCP 8.5', height = 500, width = 5000)
        st.plotly_chart(fig, use_container_width=True)
        fig = go.Figure(data =
    go.Contour(
        z=z[::10, ::10],
        colorscale='Hot',
        contours=dict(
            start=0,
            end=0.7,
            size=0.05,
        ),
    ))
        fig.update_layout(title='Sea Level Impact on Andaman in Year 2100 for RCP 8.5') 
        st.plotly_chart(fig, use_container_width=True)
    elif year == 2150:
        fig, axes = plt.subplots(1, 5)
        fig.suptitle("Remaining Land in the year 2150 for RCP 8.5")
        plt.subplots_adjust(left=0.1,
                            bottom=0.1, 
                            right=0.9, 
                            top=0.9, 
                            wspace=0.4, 
                            hspace=0.4)
        # Plot something on each subplot
        axes[0].imshow(bl85150)
        axes[0].set_title("Settlement")
        axes[0].axis("off")
        axes[1].imshow(cl85150)
        axes[1].set_title("Agricultural")
        axes[1].axis("off")
        axes[2].imshow(gl85150)
        axes[2].set_title("Grasslands")
        axes[2].axis("off")
        axes[3].imshow(ml85150)
        axes[3].set_title("Mangrooves")
        axes[3].axis("off")
        axes[4].imshow(fl85150)
        axes[4].set_title("Forests")
        axes[4].axis("off")
        st.pyplot(fig)

        img = PIL.Image.open('Elevation_2150_RCP85.png')
        z_data = np.array(img)
        z = z_data.transpose()
        sh_0, sh_1 = z.shape
        z = z/255*0.7
        x, y = np.linspace(0, 360, sh_0), np.linspace(0, 180, sh_1)
        xv, yv = np.meshgrid(x, y)
        fig = go.Figure(data=[go.Surface(z=z[::10], x=xv[::10], y=yv[::10])])
        fig.update_layout(title='Sea Level Impact on Andaman in Year 2150 for RCP 8.5', height = 500, width = 5000)

        st.plotly_chart(fig, use_container_width=True)
        fig = go.Figure(data =
    go.Contour(
        z=z[::10, ::10],
        colorscale='Hot',
        contours=dict(
            start=0,
            end=0.7,
            size=0.05,
        ),
    ))
        fig.update_layout(title='Sea Level Impact on Andaman in Year 2150 for RCP 8.5') 
        st.plotly_chart(fig, use_container_width=True)
    elif year == 2200:
        fig, axes = plt.subplots(1, 5)
        fig.suptitle("Remaining Land in the year 2200 for RCP 8.5")
        plt.subplots_adjust(left=0.1,
                            bottom=0.1, 
                            right=0.9, 
                            top=0.9, 
                            wspace=0.4, 
                            hspace=0.4)
        # Plot something on each subplot
        axes[0].imshow(bl85200)
        axes[0].set_title("Settlement")
        axes[0].axis("off")
        axes[1].imshow(cl85200)
        axes[1].set_title("Agricultural")
        axes[1].axis("off")
        axes[2].imshow(gl85200)
        axes[2].set_title("Grasslands")
        axes[2].axis("off")
        axes[3].imshow(ml85200)
        axes[3].set_title("Mangrooves")
        axes[3].axis("off")
        axes[4].imshow(fl85200)
        axes[4].set_title("Forests")
        axes[4].axis("off")
        st.pyplot(fig)

        img = PIL.Image.open('Elevation_2200_RCP85.png')
        z_data = np.array(img)
        z = z_data.transpose()
        sh_0, sh_1 = z.shape
        z = z/255*0.7
        x, y = np.linspace(0, 360, sh_0), np.linspace(0, 180, sh_1)
        xv, yv = np.meshgrid(x, y)
        fig = go.Figure(data=[go.Surface(z=z[::10], x=xv[::10], y=yv[::10])])
        fig.update_layout(title='Sea Level Impact on Andaman in Year 2200 for RCP 8.5', height = 500, width = 5000)
        st.plotly_chart(fig, use_container_width=True)
        fig = go.Figure(data =
    go.Contour(
        z=z[::10, ::10],
        colorscale='Hot',
        contours=dict(
            start=0,
            end=0.7,
            size=0.05,
        ),
    ))
        fig.update_layout(title='Sea Level Impact on Andaman in Year 2200 for RCP 8.5') 
        st.plotly_chart(fig, use_container_width=True)
    elif year == 2250:
        fig, axes = plt.subplots(1, 5)
        fig.suptitle("Remaining Land in the year 2250 for RCP 8.5")
        plt.subplots_adjust(left=0.1,
                            bottom=0.1, 
                            right=0.9, 
                            top=0.9, 
                            wspace=0.4, 
                            hspace=0.4)
        # Plot something on each subplot
        axes[0].imshow(bl85250)
        axes[0].set_title("Settlement")
        axes[0].axis("off")
        axes[1].imshow(cl85250)
        axes[1].set_title("Agricultural")
        axes[1].axis("off")
        axes[2].imshow(gl85250)
        axes[2].set_title("Grasslands")
        axes[2].axis("off")
        axes[3].imshow(ml85250)
        axes[3].set_title("Mangrooves")
        axes[3].axis("off")
        axes[4].imshow(fl85250)
        axes[4].set_title("Forests")
        axes[4].axis("off")
        st.pyplot(fig)

        img = PIL.Image.open('Elevation_2250_RCP85.png')
        z_data = np.array(img)
        z = z_data.transpose()
        sh_0, sh_1 = z.shape
        z = z/255*0.7
        x, y = np.linspace(0, 360, sh_0), np.linspace(0, 180, sh_1)
        xv, yv = np.meshgrid(x, y)
        fig = go.Figure(data=[go.Surface(z=z[::10], x=xv[::10], y=yv[::10])])
        fig.update_layout(title='Sea Level Impact on Andaman in Year 2250 for RCP 8.5', height = 500, width = 5000)
        st.plotly_chart(fig, use_container_width=True)
        fig = go.Figure(data =
    go.Contour(
        z=z[::10, ::10],
        colorscale='Hot',
        contours=dict(
            start=0,
            end=0.7,
            size=0.05,
        ),
    ))
        fig.update_layout(title='Sea Level Impact on Andaman in Year 2250 for RCP 8.5') 
        st.plotly_chart(fig, use_container_width=True)
    elif year == 2300:
        fig, axes = plt.subplots(1, 5)
        fig.suptitle("Remaining Land in the year 2300 for RCP 8.5")
        plt.subplots_adjust(left=0.1,
                            bottom=0.1, 
                            right=0.9, 
                            top=0.9, 
                            wspace=0.4, 
                            hspace=0.4)
        # Plot something on each subplot
        axes[0].imshow(bl85300)
        axes[0].set_title("Settlement")
        axes[0].axis("off")
        axes[1].imshow(cl85300)
        axes[1].set_title("Agricultural")
        axes[1].axis("off")
        axes[2].imshow(gl85300)
        axes[2].set_title("Grasslands")
        axes[2].axis("off")
        axes[3].imshow(ml85300)
        axes[3].set_title("Mangrooves")
        axes[3].axis("off")
        axes[4].imshow(fl85300)
        axes[4].set_title("Forests")
        axes[4].axis("off")
        st.pyplot(fig)

        img = PIL.Image.open('Elevation_2300_RCP85.png')
        z_data = np.array(img)
        z = z_data.transpose()
        sh_0, sh_1 = z.shape
        z = z/255*0.7
        x, y = np.linspace(0, 360, sh_0), np.linspace(0, 180, sh_1)
        xv, yv = np.meshgrid(x, y)
        fig = go.Figure(data=[go.Surface(z=z[::10], x=xv[::10], y=yv[::10])])
        fig.update_layout(title='Sea Level Impact on Andaman in Year 2300 for RCP 8.5', height = 500, width = 5000)
        st.plotly_chart(fig, use_container_width=True)
        fig = go.Figure(data =
    go.Contour(
        z=z[::10, ::10],
        colorscale='Hot',
        contours=dict(
            start=0,
            end=0.7,
            size=0.05,
        ),
    ))
        fig.update_layout(title='Sea Level Impact on Andaman in Year 2300 for RCP 8.5') 
        st.plotly_chart(fig, use_container_width=True)


html_string = "<h1 style='text-align: center; font-family: Times New Roman, Times, serif; font-weight: bold;'>Description</h1><p style='text-align: left; font-family: Times New Roman, Times, serif;'>This application simulates the impact of sea level rise on the Andaman and Nicobar Islands in terms of loss of land used for various purposes. The climate models used here are RCP 2.6, RCP 4.5 and RCP 8.5. The simulation is presented for the years 2050 to 2300. The simulation takes into account the rise in sea level. The decrease in Land level due to GIA is roughly around 1mm. The extensive GIA modeling has not been done yet. The rise in land level due to tectonics is also around 1 mm. So, in this simulation, I am considering the net influence of the parameters roughly and not to the precise values. The most important assumption is the status of present day land use is the same as 2300. That is, there is no deforestation done for agriculture and settlements. To use this application, first select the climate model which is needed to be used for the analysis. Then select the year from the slidebar. The simulation results are as displayed.</p>"

st.markdown(html_string, unsafe_allow_html=True)

html_string = "<h1 style='text-align: center; font-family: Times New Roman, Times, serif; font-weight: bold;'>Dataset Credits</h1><p style='text-align: left; font-family: Times New Roman, Times, serif;'>Assessment of change in the extent of mangrove ecosystems using different spectral indices in Google Earth Engine based on random forest model by Kolli et.al. <br> Available at: https://link.springer.com/article/10.1007/s12517-022-10158-7 <br>SRTM Dataset collected from: https://portal.opentopography.org/raster?opentopoID=OTSRTM.082015.4326.1 <br> The GIA Data was colelcted from: https://grace.jpl.nasa.gov/data/get-data/gia-trends/</p>"

st.markdown(html_string, unsafe_allow_html=True)

html_string = "<p style='text-align: center; font-family: Times New Roman, Times, serif; font-style: oblique;'>\"The greatest threat to our planet is the belief that someone else will save it\"</p>"

st.markdown(html_string, unsafe_allow_html=True)

html_string = "<p style='text-align: center; font-family: Times New Roman, Times, serif;'>Application made by JaidevSK</p>"

st.markdown(html_string, unsafe_allow_html=True)
