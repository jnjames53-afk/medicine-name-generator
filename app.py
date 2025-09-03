import streamlit as st
import random

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
# Streamlit UI
# ------------------------
st.title("💊 Medicine Brand Name Generator")

# Molecule input
molecule = st.text_input("Enter Molecule (e.g., Metformin):")

# Style selection
style = st.selectbox("Choose Name Style:", list(style_sets.keys()))

# Number of names
num_names = st.slider("How many names to generate?", 5, 50, 20)

# Generate button
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

        st.success(f"Generated {len(generated)} unique {style} names:")
        for name in generated:
            st.write("✅", name)

# Optional: availability checker
st.markdown("### 🌍 Availability Check (Google Search)")
if molecule:
    st.markdown(f"[Search Google for '{molecule} medicine'](https://www.google.com/search?q={molecule}+medicine)")
