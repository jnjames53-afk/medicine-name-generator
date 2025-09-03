import streamlit as st
import random
from PIL import Image

# ------------------------
# Page Config
# ------------------------
st.set_page_config(page_title="Myra Healthcare", page_icon="💊", layout="centered")

# ------------------------
# Logo + Branding
# ------------------------
try:
    logo = Image.open("logo.png")  # upload logo.png to your repo
    st.image(logo, width=200)
except:
    st.write("")

st.markdown(
    "<h1 style='text-align: center; color: #2E86C1;'>Myra Healthcare™</h1>",
    unsafe_allow_html=True
)
st.write("✨ Innovative Medicine Name Generator ✨")

# ------------------------
# Prefixes & Suffixes by style
# ------------------------
style_sets = {
    "Serious": {
        "prefixes": ["Medi", "Pharma", "Cura", "Cardi", "Neuro", "Onco", "Thera", "Bio", "Gen"],
        "suffixes": ["med", "lin", "set", "ron", "tab", "cap", "zol", "pan", "rin"]
    },
    "Catchy": {
        "prefixes": ["Zy", "Tri", "Max", "Vita", "Nova", "Lexa", "Azo", "Oxi", "Xy"],
        "suffixes": ["ex", "ra", "via", "lux", "pro", "go", "va", "zy", "do"]
    },
    "Luxury": {
        "prefixes": ["Astra", "Elix", "Cura", "Novo", "Vero", "Lumi", "Seren", "Prima", "Aura"],
        "suffixes": ["lux", "via", "elle", "ora", "ence", "ique", "lis", "tria", "on"]
    },
    "Scientific": {
        "prefixes": ["Neuro", "Cyto", "Immu", "Gen", "Proto", "Nano", "Chem", "Mole", "Bio"],
        "suffixes": ["mab", "stat", "vir", "zol", "micin", "phine", "dine", "cillin", "xil"]
    }
}

# ------------------------
# User Inputs
# ------------------------
molecule = st.text_input("Enter Molecule (e.g., Metformin):")
style = st.selectbox("Choose Name Style:", list(style_sets.keys()))
num_names = st.slider("How many names to generate?", 5, 50, 20)

# ------------------------
# Generate Names
# ------------------------
if st.button("Generate Names"):
    if molecule.strip() == "":
        st.warning("Please enter a molecule name!")
    else:
        prefixes = style_sets[style]["prefixes"]
        suffixes = style_sets[style]["suffixes"]

        generated = set()
        while len(generated) < num_names:
            prefix = random.choice(prefixes)
            suffix = random.choice(suffixes)
            new_name = prefix + molecule[:3].capitalize() + suffix
            generated.add(new_name)

        # ✅ Display results with Google search links
        st.success(f"Generated {len(generated)} unique {style} names:")

        for name in generated:
            search_url = f"https://www.google.com/search?q={name}+medicine"
            st.markdown(f"✅ **{name}** → [Check availability]({search_url})")
