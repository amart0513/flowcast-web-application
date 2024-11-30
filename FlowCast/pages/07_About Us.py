import streamlit as st


IMAGE_MLH = "media/MLH.png"
IMAGE_JESUS = "media/JesusPic.jpg"
IMAGE_ANGIE = "media/AngiePic.jpg"
IMAGE_STEVEN = "media/StevenPic.jpg"
IMAGE_CHRIS = "media/ChrisPic.jpg"
IMAGE_FIU = "media/FIU_LOGO.png"
#IMAGE_FIU_BANNER = "media/FIU_Banner.png"


st.set_page_config(page_title="FlowCast", layout="wide",
                   page_icon="🌊", initial_sidebar_state="expanded")


def load_media(column, file_path, caption):
    with column:
        if file_path.endswith(".jpeg") or file_path.endswith(".PNG") or file_path.endswith(".jpg"):
            column.image(file_path, caption=caption, width=200)
        elif file_path.endswith(".mp4"):
            column.video(file_path)
        elif file_path.endswith(".mp3"):
            column.audio(file_path)




st.title("About Us")
st.subheader("Get to Know the Team!")
st.divider()
col1, col2, col3, col4 = st.columns(4)
load_media(col1, IMAGE_JESUS, "Jesus Elespuru, Product Owner, Back-end Developer, Data-Collection, Marine Robotics Florida International "
                                  "University")
load_media(col2, IMAGE_ANGIE,
               "Angie Martinez, Team Lead, Front-End Developer, Project Management, Florida International University")
load_media(col3, IMAGE_STEVEN,
               "Steven Luque, Team Member, Hardware Design, Wiring Integration, Florida International University")
load_media(col4, IMAGE_CHRIS,
               "Christopher Perez, Team Member, Circuit Analysis, Florida International University")
st.divider()
col5, col6, col7 = st.columns([1, 1, 1])

# with col6:
#      #st.image(IMAGE_FIU_BANNER, width=200)