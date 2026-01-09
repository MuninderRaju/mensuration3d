import streamlit as st

# Page Configuration
st.set_page_config(page_title="10th Class Mensuration", layout="wide")

# Title and Description
st.title("📐 Mensuration Formulas - 3D Shapes")
st.subheader("పదవ తరగతి క్షేత్రమితి సూత్రాలు (Bilingual)")
st.write("---")

# Dictionary of formulas and image URLs
shapes = {
    "Cube (ఘనము)": {
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a3/Cube_isometric.png/220px-Cube_isometric.png",
        "formulas": {
            "Lateral Surface Area (ప్రక్క తల వైశాల్యం)": "4a²",
            "Total Surface Area (సంపూర్ణ తల వైశాల్యం)": "6a²",
            "Volume (ఘనపరిమాణం)": "a³"
        }
    },
    "Cuboid (దీర్ఘ ఘనము)": {
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dc/Cuboid.svg/250px-Cuboid.svg.png",
        "formulas": {
            "Lateral Surface Area (ప్రక్క తల వైశాల్యం)": "2h(l + b)",
            "Total Surface Area (సంపూర్ణ తల వైశాల్యం)": "2(lb + bh + lh)",
            "Volume (ఘనపరిమాణం)": "l × b × h"
        }
    },
    "Cylinder (స్తూపం)": {
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Cylinder_geometry.svg/200px-Cylinder_geometry.svg.png",
        "formulas": {
            "Curved Surface Area (వక్రతల వైశాల్యం)": "2πrh",
            "Total Surface Area (సంపూర్ణ తల వైశాల్యం)": "2πr(r + h)",
            "Volume (ఘనపరిమాణం)": "πr²h"
        }
    },
    "Cone (శంఖువు)": {
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Cone_3d.png/220px-Cone_3d.png",
        "formulas": {
            "Slant Height (ఏటవాలు ఎత్తు)": "l = √(r² + h²)",
            "Curved Surface Area (వక్రతల వైశాల్యం)": "πrl",
            "Total Surface Area (సంపూర్ణ తల వైశాల్యం)": "πr(r + l)",
            "Volume (ఘనపరిమాణం)": "1/3 πr²h"
        }
    },
    "Sphere (గోళం)": {
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Sphere_wireframe_10deg_6row.svg/200px-Sphere_wireframe_10deg_6row.svg.png",
        "formulas": {
            "Surface Area (ఉపరితల వైశాల్యం)": "4πr²",
            "Volume (ఘనపరిమాణం)": "4/3 πr³"
        }
    },
    "Hemisphere (అర్ధగోళం)": {
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Hemisphere.png/220px-Hemisphere.png",
        "formulas": {
            "Curved Surface Area (వక్రతల వైశాల్యం)": "2πr²",
            "Total Surface Area (సంపూర్ణ తల వైశాల్యం)": "3πr²",
            "Volume (ఘనపరిమాణం)": "2/3 πr³"
        }
    }
}

# Sidebar for Selection
st.sidebar.header("Select a Shape")
selected_shape = st.sidebar.selectbox("ఆకారాన్ని ఎంచుకోండి:", list(shapes.keys()))

# Main Display Area
col1, col2 = st.columns([1, 1])

with col1:
    st.header(selected_shape)
    st.image(shapes[selected_shape]["image"], width=300)

with col2:
    st.subheader("Formulas (సూత్రాలు)")
    for label, formula in shapes[selected_shape]["formulas"].items():
        st.markdown(f"**{label}:**")
        st.latex(formula)

st.write("---")
st.info("Note: π (Pi) value is approximately 22/7 or 3.14")
