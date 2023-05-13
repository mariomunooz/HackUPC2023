import streamlit as st

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



# Create a button for users to upload photos
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# Display the uploaded photo
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded image')