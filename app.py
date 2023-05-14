import streamlit as st
from PIL import Image
from Imgur import generate_url as gu
import json
import os
import requests
from streamlit_lottie import st_lottie
import time

from api_interaction import api_main as apim

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# set the title of the web app
st.title("Real State Marketplace Recommender")

# display some text in the app
st.write("""Do you want to rent your house, but you're not sure where to start? We're here to help! Our team of 
experts can guide you through the process and help you find the perfect tenant for your property. Whether you're a 
first-time landlord or an experienced property owner, we have the knowledge and expertise to make the rental process 
as smooth and stress-free as possible. """)

st.write("""\n\n\nWe make renting out your property easy! With our streamlined process, we only need the images of your 
house to get started. You can relax and let us take care of the rest. Our team of experts will use advanced image 
recognition technology to analyze the visual features of your property, and provide personalized recommendations 
based on those features. """)

st.write("""\n\n**Upload 4 Images of your house**""")
# Create a button for users to upload photos
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])


number_of_images_stored = gu.get_num_of_images_stored()


# Display the uploaded photo
if uploaded_file is not None:
    img = uploaded_file.read()

    image_url = gu.uploadToBlobStorage2(img, os.path.splitext(uploaded_file.name)[-1] )


while number_of_images_stored < 3:
    time.sleep(1)


st_lottie( load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_lp7qD9RDx1.json"), height=200, )

st.write(f'{gu.get_urls_of_images_stored()}')

st.write(apim.create_estate_description(gu.get_urls_of_images_stored()))








