import streamlit as st
from ultralytics import YOLO
from PIL import Image


st.markdown("""<h1 style="text-align:center;font-size:75px; font-family:Agency FB">Elegance in Every Step</h1>""", unsafe_allow_html=True)


shoes = {
    "Nike": [
        {"name": "Nike Air Jordan 4 Lightning", "url": "https://static.nike.com/a/images/t_prod_ss/w_640,c_limit,f_auto/b0612b56-5306-4f1e-84dd-42513f5067f9/air-jordan-4-tour-yellow-release-date.jpg"},
        {"name": "Nike Air Force 1", "url": "https://static.nike.com/a/images/t_PDP_1280_v1/f_auto,q_auto:eco/b7d9211c-26e7-431a-ac24-b0540fb3c00f/air-force-1-07-shoes-WrLlWX.png"},
        {"name": "Nike Air Jordan 1 Mochas", "url": "https://static.nike.com/a/images/t_prod_ss/w_640,c_limit,f_auto/8723269b-1e63-4b5e-922b-6d3aca20b715/air-jordan-1-dark-mocha-release-date.jpg"},
        {"name": "Nike Blazer Mid '77", "url": "https://static.nike.com/a/images/t_PDP_1728_v1/f_auto,q_auto:eco/fb7eda3c-5ac8-4d05-a18f-1c2c5e82e36e/blazer-mid-77-vintage-shoes-dNWPTj.png"},
        {"name": "Nike Air Jordan 1 Retro High OG", "url": "https://static.nike.com/a/images/t_PDP_1728_v1/f_auto,q_auto:eco,u_126ab356-44d8-4a06-89b4-fcdcc8df0245,c_scale,fl_relative,w_1.0,h_1.0,fl_layer_apply/bab11a0e-6ccd-4b17-a3ec-db5eb94d5e8c/air-jordan-1-retro-high-og-shoes-Pz6fZ9.png"}
    ],
    "Adidas": [
        {"name": "Adidas Ultraboost 21", "url": "https://assets.adidas.com/images/h_840,f_auto,q_auto,fl_lossy,c_fill,g_auto/15f26c080f2e4082bd552dab89b36dec_9366/Ultraboost_Light_Shoes_Beige_IE5978_HM1.jpg"},
        {"name": "Adidas NMD_R1", "url": "https://assets.adidas.com/images/h_840,f_auto,q_auto,fl_lossy,c_fill,g_auto/c3bd9dda9fdd4a7cbc9aad1e00dd0045_9366/NMD_R1_Shoes_White_GZ9260_01_standard.jpg"},
        {"name": "Adidas Superstar", "url": "https://assets.adidas.com/images/h_840,f_auto,q_auto,fl_lossy,c_fill,g_auto/c35214f6104c4a288bfed0c7c88dd94c_9366/Superstar_XLG_Shoes_White_IF9995_01_standard.jpg"},
        {"name": "Adidas Stan Smith", "url": "https://assets.adidas.com/images/h_840,f_auto,q_auto,fl_lossy,c_fill,g_auto/68ae7ea7849b43eca70aac1e00f5146d_9366/Stan_Smith_Shoes_White_FX5502_01_standard.jpg"},
        {"name": "Adidas Yeezy Boost 350", "url": "https://crepdogcrew.com/cdn/shop/files/EditsbyAhmar01_57b3126b-b12c-4e01-8c82-6afac5cbed48.png?v=1716190605&width=1000"}
    ],

    "Converse": [
        {"name": "Converse Chuck Taylor", "url": "https://www.converse.in/media/catalog/product/1/6/162050c_01_1.jpg"},
        {"name": "Converse All Star", "url": "https://www.converse.in/media/catalog/product/m/7/m7650c-01.jpg"},
        {"name": "Converse Pro Leather", "url": "https://www.converseindia.top/images/large/converseinindia/Converse_Chinatown_Market_Pro_Leather_Hi-CV-519OEF_ZOOM.jpg"},
        {"name": "Converse One Star", "url": "https://www.converse.in/media/catalog/product/a/0/a04612c_a_107x1.jpg"},
        {"name": "Converse Run Star Hike", "url": "https://www.converse.in/media/catalog/product/1/7/171545c_01_1.jpg"}
    ]
}



st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://wallpapers.com/images/hd/sneakerhead-tf9y8u0pv5brs6jr.jpg");
        background-size: auto;
        color: white;
        font-family: Agency FB;
    }
    .green-button {
        background-color: green;
        border: 8px solid white;
        color: white;
        padding: 16px 30px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 22px;
        margin: 10px 8px;
        cursor: pointer;
        border-radius: 22px;
    }
    </style>
    """,
    unsafe_allow_html=True
)


with tab1:
    if 'page' not in st.session_state:
         st.session_state.page = 'Home'
    tab1,tab2 =st.tabs(["Home","Prediction"])
    cols=st.columns([0.1,0.8,0.1,])
    container1=st.container()
    
    def switch_page(page):
        st.session_state.page = page
    
    if st.session_state.page == 'Home':
        with cols[1]:  
            st.markdown("""
                   <h1 style="font-family: Agency FB; font-size:40px; text-align:center">Which do you prefer?</h1> """, unsafe_allow_html=True)
        with container1:
            for brand in  shoes.keys():
                if st.button(brand,type="primary", key=brand, on_click=switch_page, args=(brand,),use_container_width=True):
                  pass

    
   

else:
    precition=st.session_state.page
    brand = st.session_state.page
    if st.button("Home",type="primary", on_click=switch_page, args=('Home',)):
         pass

    st.header(f"{brand} Sneakers")
    for sneaker in shoes[brand]:
        st.markdown(sneaker['name'])
        st.image(sneaker['url'], use_column_width=True)

with tab2:
    st.markdown("""<h1 style="font-family: Agency FB; font-size:40px; text-align:center">Get to Know your shoes</h1>""",unsafe_allow_html=True)
    @st.cache_resource
    def load_model():
        mod=YOLO("best1.pt")
        return mod
    img=st.file_uploader("Upload The Image of Your Shoes",type=["jpg","png","jpeg"])
    if img is not None:
        img=Image.open(img)
        st.image(img)
        mod1=load_model()
        res=mod1.predict(img)
        pred=res[0].probs.top1
        st.write(res[0].names[pred])
    
    


        
