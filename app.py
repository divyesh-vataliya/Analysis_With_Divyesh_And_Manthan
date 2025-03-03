import pandas as pd
import numpy as np
import streamlit as st
import ast
import matplotlib.pyplot as plt
import time

#_______________________________________________________________ Front Page ____________________________________________________________________________________________________________________

import streamlit as st

# ✅ Set page configuration
st.set_page_config(page_title="E-Commerce Analysis", page_icon="🛒", layout="wide")

# ✅ Custom CSS for animations and responsive logo positioning
st.markdown("""
    <style>
        .header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 10px 20px;
            background-color: ;
            border-bottom: 2px solid  ;
        }
        .logo-container {
            display: flex;
            align-items: center;
            cursor: pointer;
        }
        .logo-container img {
            width: 80px;
            transition: transform 0.3s ease-in-out;
        }
        .logo-container:hover img {
            transform: scale(1.2);
        }
        .logo-text {
            font-size: 16px;
            color: #FF5722;
            margin-left: 10px;
            display: none;
        }
        .logo-container:hover .logo-text {
            display: block;
        }
        .intro-container {
            text-align: center;
            padding: 50px;
        }
        .made-by {
            text-align: center;
            margin-top: 50px;
            padding: 20px;
            border-top: 2px solid #FF5722;
        }
        .contact-info {
            display: flex;
            justify-content: center;
            gap: 60px;
            margin-top: 20px;
        }
        .contact-card {
            text-align: center;
            font-size: 18px;
            color: #333;
            width: 250px;
        }
        .contact-card h4 {
            color: white;
        }
        .contact-card span {
            color: #FF5722;
        }
        .contact-card a {
            text-decoration: none;
            color: #FF5722;
            font-size: 18px;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-top: 8px;
        }
        .contact-card a:hover {
            color: #E64A19;
        }
        .icon {
            width: 24px;
            height: 24px;
            margin-right: 8px;
        }
    </style>
""", unsafe_allow_html=True)

# ✅ Project Introduction
st.markdown("""
    <div class="intro-container" style="padding: 50px 10px;">
        <h1 style="display: flex; align-items: center; justify-content: center; font-size: 2.5em;">
            <div class="logo-container" style="margin-right: 10px;">
                <img src="https://i.imgur.com/QBcz8jD.png" alt="Logo" style="width: 100px;">
            </div> 
            Data-Driven Insights for Online Shopping
        </h1>
        <p style="font-size: 1.2em; text-align: center;">
            This platform provides comprehensive analytics on various product categories,
            helping users compare prices, ratings, and trends effortlessly.
            Explore data-driven insights to make informed purchasing decisions.
        </p>
    </div>
""", unsafe_allow_html=True)

# ✅ Made By Section
st.markdown("""
    <div class="made-by">
        <h2>🚀 Made by</h2>
        <div class="contact-info">
            <div class="contact-card">
                <h4>Divyesh Vataliya</h4>
                <div>📞 <span>9328941914</span></div>
                <div>
                    <a href="https://www.linkedin.com/in/divyesh-vataliya-b31b2a254/" target="_blank">
                        <img src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png" class="icon">LinkedIn
                    </a>
                </div>
                <div>
                    <a href="https://docs.google.com/forms/d/e/1FAIpQLSe3wwHYipRuZjjyS587FdXiLx9np0xlVJ6O2SWzidd3NiE9Sw/viewform?usp=header" target="_blank">
                        <img src="https://upload.wikimedia.org/wikipedia/commons/4/4e/Gmail_Icon.png" class="icon">Gmail
                    </a>
                </div>
            </div>
            <div class="contact-card">
                <h4>Manthan Pandya</h4>
                <div>📞 <span>8758054764</span></div>
                <div>
                    <a href="https://www.linkedin.com/in/manthan-pandya-750776253" target="_blank">
                        <img src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png" class="icon">LinkedIn
                    </a>
                </div>
                <div>
                    <a href="https://docs.google.com/forms/d/e/1FAIpQLSdpIrHFaq5FL47LKmbDEUybg7io-jPHBUQgQoz8gxcjDff2YA/viewform?usp=header" target="_blank">
                        <img src="https://upload.wikimedia.org/wikipedia/commons/4/4e/Gmail_Icon.png" class="icon">Gmail
                    </a>
                </div>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)









#_______________________________________________________________ Second Analysis Page ____________________________________________________________________________________________________________________


# ✅ Cache dataset loading for performance optimization
@st.cache_data
def load_data():
    df = pd.read_csv(r"C:\vs\project\processed_flipkart_data_with_images.csv")
    return df

data_new = load_data()

# Extract unique categories from "category" column
unique_categories = data_new['category'].dropna().unique()

# ✅ Default images for categories
category_images = {
    "Kurtis": "https://your-image-url.com/kurtis_default.jpg",
    "Shoes": "https://your-image-url.com/shoes_default.jpg",
    "Bracelets": "https://your-image-url.com/bracelets_default.jpg",
    "Handbags": "https://your-image-url.com/handbags_default.jpg",
    # Add more categories if needed
}

# ✅ Custom CSS for improved styling
st.markdown("""
    <style>
        body { font-family: 'Arial', sans-serif; }
        .stTable { text-align: left; }
        .stButton>button { 
            background-color: #FF5722; 
            color: white !important; 
            font-size: 16px; 
            padding: 10px; 
            border-radius: 8px; 
            transition: all 0.3s ease;
        }
        .stButton>button:hover {
            background-color: #E64A19;
            color: white !important;
        }
        .stSelectbox>div { font-size: 16px; }
        .result-container { 
            border: 2px solid #FF5722; 
            padding: 20px; 
            border-radius: 10px; 
            background-color:#0E1117; 
            color: white;
            text-align: center;
            margin-bottom: 30px;
        }
        .product-container {
            display: flex;
            flex-wrap: wrap;
            justify-content: left;
            gap: 50px;
            margin-bottom: 50px;
        }
        .product-card {
            width: 280px;
            padding: 15px;
            border-radius: 10px;
            background: #f9f9f9;
            box-shadow: 0px 2px 10px rgba(0, 0, 0, 0.1);
            text-align: left;
        }
        .product-card img {
            width: 100%;
            height: auto;
            border-radius: 10px;
        }
        .product-title {
            font-weight: bold;
            font-size: 16px;
            margin-top: 10px;
        }
        .product-price {
            color: #D84315;
            font-size: 18px;
            font-weight: bold;
        }
        .product-rating {
            font-size: 18px;
            color: #FFAB00;
            font-weight: bold;
        }
        .chart-container {
            margin-top: 80px;
            text-align: center;
        }
        #MainMenu, footer { visibility: hidden; }
    </style>
""", unsafe_allow_html=True)

# ✅ 🔍 Search Mechanism
st.sidebar.header("🔍 Search for a Product")

# User input for searching products
st.sidebar.markdown("The comparison results will be displayed at the bottom of the page after clicking 'Compare Categories'.")
search_input = st.sidebar.text_input("Type a product name (partial allowed)", "")

# Suggest products based on input
if search_input:
    suggestions = [cat for cat in unique_categories if search_input.lower() in cat.lower()]
    if suggestions:
        selected_product = st.sidebar.selectbox("Did you mean?", suggestions)
    else:
        selected_product = None
else:
    selected_product = None

# ✅ Sidebar category selection
st.sidebar.header("📌 Category Selection")
num_categories = st.sidebar.number_input("How many categories to compare?", min_value=1, max_value=len(unique_categories), step=1)

selected_categories = []
for i in range(num_categories):
    category_choice = st.sidebar.selectbox(f"Select Category {i + 1}:", unique_categories, key=f"category_{i}")
    selected_categories.append(category_choice)

# ✅ Placeholder for results
result_section = st.empty()
result_section.markdown('<div class="result-container"><h3>📊 Results will appear here after clicking "Compare Categories"</h3><p>Select categories from the sidebar and click the button to generate insights.</p></div>', unsafe_allow_html=True)

# ✅ Function to display products
def display_products(selected_category):
    products = data_new[data_new['category'] == selected_category]
    if products.empty:
        st.write(f"No products found in {selected_category}.")
        return pd.DataFrame()

    products.fillna({
        'retail_price': np.random.randint(100, 10000),
        'discounted_price': np.random.randint(50, 9000),
        'product_rating': np.random.uniform(1, 5),
        'overall_rating': np.random.uniform(1, 5),
    }, inplace=True)

    product_html = '<div class="product-container">'

    for _, row in products.iterrows():
        try:
            image_urls = ast.literal_eval(row['image'])
            image_url = image_urls[0] if image_urls else category_images.get(selected_category, "https://via.placeholder.com/150")
        except:
            image_url = category_images.get(selected_category, "https://via.placeholder.com/150")

        product_html += f"""
        <div class="product-card">
            <img src="{image_url}" alt="Product Image">
            <div class="product-title">{row['product_name']}</div>
            <div class="product-price">💰 Price: ₹{row['discounted_price']} (MRP: ₹{row['retail_price']})</div>
            <div class="product-rating">⭐ Rating: {'⭐' * int(round(row['product_rating'], 0))}</div>
        </div>
        """

    product_html += '</div>'
    st.markdown(product_html, unsafe_allow_html=True)

    return products

# ✅ Function to display a comparison pie chart
def display_comparison_piechart(all_products):
    if all_products.empty:
        return
    
    st.markdown('<h2 style="text-align: center; margin-bottom: 20px;">Category-wise Comparison of Price, Discounted Price, and Rating</h2>', unsafe_allow_html=True)
    
    categories = all_products['category'].unique()
    values = []
    labels = []
    colors = plt.cm.Paired.colors[:len(categories)]
    
    for category in categories:
        subset = all_products[all_products['category'] == category]
        values.append(subset['discounted_price'].sum())
        labels.append(category)
    
    plt.figure(figsize=(5, 4))
    plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors)
    plt.title("Category-wise Price Distribution", fontsize=16)
    st.pyplot(plt)
    

# ✅ Main function
def main():
    all_products = pd.DataFrame()

    # ✅ Search functionality execution
    if selected_product:
        st.write(f"## 🔎 Search Results for: {selected_product}")
        display_products(selected_product)

    if st.sidebar.button("Compare Categories"):
        with result_section:
            st.markdown('<div class="result-container"><h3>🔄 Generating Results...</h3><p>Please wait while we analyze the data.</p></div>', unsafe_allow_html=True)
        
        st.write("## 📊 Comparison Results")
        
        for category in selected_categories:
            st.write(f"### {category}")
            products = display_products(category)
            if not products.empty:
                all_products = pd.concat([all_products, products])
        
        display_comparison_piechart(all_products)

if __name__ == "__main__":
    main()
