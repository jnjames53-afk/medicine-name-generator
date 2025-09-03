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
st.write("✨ Smarter Medicine Name Generator ✨")

# ------------------------
# Molecule → Disease & Usage Mapping
# ------------------------
therapeutic_map = {
    "Metformin": {"disease": "Diabetes", "usage": "Blood sugar control"},
    "Atorvastatin": {"disease": "Cholesterol", "usage": "Lowering bad cholesterol"},
    "Rosuvastatin": {"disease": "Cholesterol", "usage": "Cholesterol reduction"},
    "Amlodipine": {"disease": "Hypertension", "usage": "Blood pressure control"},
    "Losartan": {"disease": "Hypertension", "usage": "Blood pressure management"},
    "Metoprolol": {"disease": "Hypertension", "usage": "Heart rate and blood pressure control"},
    "Omeprazole": {"disease": "Acidity", "usage": "Reduces stomach acid"},
    "Paracetamol": {"disease": "Fever", "usage": "Fever and pain relief"},
    "Ibuprofen": {"disease": "Pain", "usage": "Pain and inflammation relief"},
    "Duloxetine": {"disease": "Pain", "usage": "Nerve pain and depression management"},
    "Aspirin": {"disease": "Pain", "usage": "Pain relief and blood thinning"},
    "Cetirizine": {"disease": "Allergy", "usage": "Allergy and hay fever relief"},
    "Amoxicillin": {"disease": "Infection", "usage": "Bacterial infection treatment"},
    "Levothyroxine": {"disease": "Thyroid", "usage": "Hypothyroidism treatment"},
    "Fluoxetine": {"disease": "Depression", "usage": "Major depressive disorder"},
    "Sertraline": {"disease": "Depression", "usage": "Major depressive and anxiety disorders"},
    "Diazepam": {"disease": "Anxiety", "usage": "Anxiety and sedation"},
    "Salbutamol": {"disease": "Asthma", "usage": "Bronchodilation for asthma relief"},
    "Prednisone": {"disease": "Inflammation", "usage": "Anti-inflammatory corticosteroid"},
}

# ------------------------
# Prefix/Suffix by Disease
# ------------------------
disease_dict = {
    "Diabetes": (["Glu", "Dia", "Ins"], ["via", "met", "ra", "tin", "cor", "lin"]),
    "Cholesterol": (["Lip", "Stat", "Card"], ["ra", "tor", "zin", "col", "max"]),
    "Hypertension": (["Hyp", "Tens", "Pres"], ["ol", "am", "pr", "ta", "rin"]),
    "Acidity": (["Om", "Gas", "Acid"], ["ra", "zol", "cid", "pam"]),
    "Fever": (["Py", "Temp", "Ther"], ["ol", "par", "mal", "ta"]),
    "Pain": (["Ibu", "Ana", "Dol"], ["pro", "fen", "ra", "pan"]),
    "Allergy": (["Cet", "Hist", "Aler"], ["ine", "ra", "la", "cet"]),
    "Infection": (["Amox", "Cefi", "Bio"], ["cillin", "mycin", "bact"]),
    "Thyroid": (["Thy", "Levo", "Horm"], ["rox", "thy", "lin"]),
    "Asthma": (["Sal", "Bude", "Air"], ["rol", "vent", "mab"]),
    "Cancer": (["Onco", "Chemo", "Neo"], ["mab", "tin", "cel"]),
    "Depression": (["Ser", "Dulo", "Ami"], ["ine", "pam", "trine"]),
    "Anxiety": (["Dia", "Clon", "Alp"], ["pam", "zol", "pin"]),
    "Inflammation": (["Pred", "Cort", "Flu"], ["nid", "ist", "one"]),
    "General": (["Neo", "Bio", "Medi"], ["ra", "ex", "lin", "via"]),
}

# ------------------------
# User Inputs
# ------------------------
molecule = st.text_input("Enter Molecule (e.g., Metformin):")
num_names = st.slider("How many names to generate?", 5, 50, 20)

# Normalize molecule input
mol_key = molecule.strip().title()
mol_cap = molecule.strip().capitalize()

# Default demo molecule if nothing entered
if molecule.strip() == "":
    mol_key, mol_cap = "Paracetamol", "Paracetamol"
    disease = therapeutic_map[mol_key]["disease"]
    usage = therapeutic_map[mol_key]["usage"]
else:
    if mol_key in therapeutic_map:
        disease = therapeutic_map[mol_key]["disease"]
        usage = therapeutic_map[mol_key]["usage"]
    else:
        disease = st.selectbox(
            f"Select therapeutic area for {mol_cap}:",
            list(disease_dict.keys())
        )
        usage = st.text_input(
            "Enter usage (e.g., 'Kidney disease treatment'):",
            value="User-defined usage"
        )

# ------------------------
# Name Generation Function
# ------------------------
def generate_names(prefixes, suffixes, num_names):
    generated = set()
    max_possible = len(prefixes) * len(suffixes)
    target = min(num_names * 3, max_possible)

    while len(generated) < target:
        prefix = random.choice(prefixes)
        suffix = random.choice(suffixes)
        new_name = (prefix + suffix).capitalize()
        generated.add(new_name)

    return generated, max_possible

# ------------------------
# Generate Smart Names
# ------------------------
if st.button("Generate Names") or molecule.strip() == "":  # auto-run demo
    prefixes, suffixes = disease_dict.get(disease, disease_dict["General"])
    generated, max_possible = generate_names(prefixes, suffixes, num_names)

    # Info if fewer names possible
    if max_possible < num_names:
        st.info(f"Only {max_possible} unique names possible for {disease}. Showing all available.")

    # Categorize by length
    short_names = [n for n in generated if 4 <= len(n) <= 6]
    medium_names = [n for n in generated if 7 <= len(n) <= 8]
    long_names = [n for n in generated if len(n) > 8]

    # Trademark portals
    india_link = "https://tmrsearch.ipindia.gov.in/tmrpublicsearch/"
    us_link = "https://www.uspto.gov/trademarks/search"
    eu_link = "https://euipo.europa.eu/ohimportal/en/rcy-search"

    # Display function
    def display_name(name, mol_cap, usage, disease, india_link, us_link, eu_link):
        st.markdown(
            f"""
            <div style="
                border: 2px solid #2E86C1; 
                border-radius: 10px; 
                padding: 15px; 
                margin: 10px 0; 
                background-color: #F8F9F9;
            ">
                <h3 style="color:#2E86C1;">💊 {name}</h3>
                <p><b>Molecule:</b> {mol_cap}</p>
                <p><b>Usage:</b> {usage} ({disease})</p>
                <p><b>Trademark:</b> 
                    <a href="{india_link}" target="_blank">India</a> | 
                    <a href="{us_link}" target="_blank">US</a> | 
                    <a href="{eu_link}" target="_blank">EU</a>
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    # Show results
    st.success(f"Generated smart names for {mol_cap} ({disease}):")

    if short_names:
        st.markdown("### 🔹 4–6 Letters")
        for n in short_names[:num_names]:
            display_name(n, mol_cap, usage, disease, india_link, us_link, eu_link)

    if medium_names:
        st.markdown("### 🔹 7–8 Letters")
        for n in medium_names[:num_names]:
            display_name(n, mol_cap, usage, disease, india_link, us_link, eu_link)

    if long_names:
        st.markdown("### 🔹 9+ Letters")
        for n in long_names[:num_names]:
            display_name(n, mol_cap, usage, disease, india_link, us_link, eu_link)

    # Reminder
    st.info("💡 Copy the brand name first, then paste it in the trademark portal search box.")
