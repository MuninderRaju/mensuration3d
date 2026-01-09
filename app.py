import streamlit as st
import plotly.graph_objects as go
import numpy as np

# Page setup
st.set_page_config(page_title="Interactive 3D Mensuration", layout="wide")

st.title("📐 10th Class Mensuration - Interactive 3D")
st.subheader("3D ఆకారాలను తిప్పుతూ (Rotate) సూత్రాలను నేర్చుకోండి")

# Function to create 3D Cylinder
def draw_cylinder():
    z = np.linspace(0, 2, 50)
    theta = np.linspace(0, 2*np.pi, 50)
    theta_grid, z_grid = np.meshgrid(theta, z)
    x_grid = np.cos(theta_grid)
    y_grid = np.sin(theta_grid)
    return go.Surface(x=x_grid, y=y_grid, z=z_grid, colorscale='Viridis', showscale=False)

# Function to create 3D Cone
def draw_cone():
    z = np.linspace(0, 2, 50)
    theta = np.linspace(0, 2*np.pi, 50)
    theta_grid, z_grid = np.meshgrid(theta, z)
    r_grid = (2 - z_grid) / 2 # Radius decreases as z increases
    x_grid = r_grid * np.cos(theta_grid)
    y_grid = r_grid * np.sin(theta_grid)
    return go.Surface(x=x_grid, y=y_grid, z=z_grid, colorscale='Reds', showscale=False)

# Function to create 3D Sphere
def draw_sphere():
    phi = np.linspace(0, np.pi, 50)
    theta = np.linspace(0, 2*np.pi, 50)
    phi, theta = np.meshgrid(phi, theta)
    x = np.sin(phi) * np.cos(theta)
    y = np.sin(phi) * np.sin(theta)
    z = np.cos(phi)
    return go.Surface(x=x, y=y, z=z, colorscale='Blues', showscale=False)

# Function to create 3D Cube
def draw_cube():
    # Cube faces using Mesh3d
    return go.Mesh3d(
        x=[0, 1, 1, 0, 0, 1, 1, 0],
        y=[0, 0, 1, 1, 0, 0, 1, 1],
        z=[0, 0, 0, 0, 1, 1, 1, 1],
        i=[7, 0, 0, 0, 4, 4, 6, 6, 4, 0, 3, 2],
        j=[3, 4, 1, 2, 5, 6, 5, 2, 0, 1, 6, 3],
        k=[0, 7, 2, 3, 6, 7, 1, 1, 5, 5, 7, 6],
        color='orange', opacity=0.70
    )

# Sidebar menu
shape_name = st.sidebar.selectbox("Select a Shape (ఆకారాన్ని ఎంచుకోండి):", 
    ["Cylinder (స్తూపం)", "Cone (శంఖువు)", "Sphere (గోళం)", "Cube (ఘనము)"])

col1, col2 = st.columns([1.5, 1])

with col1:
    st.write(f"### 3D View: {shape_name}")
    fig = go.Figure()
    
    if "Cylinder" in shape_name:
        fig.add_trace(draw_cylinder())
        formulas = {
            "CSA (వక్రతల వైశాల్యం)": "2πrh",
            "TSA (సంపూర్ణ తల వైశాల్యం)": "2πr(r + h)",
            "Volume (ఘనపరిమాణం)": "πr²h"
        }
    elif "Cone" in shape_name:
        fig.add_trace(draw_cone())
        formulas = {
            "Slant Height (ఏటవాలు ఎత్తు)": "l = \sqrt{r^2 + h^2}",
            "CSA (వక్రతల వైశాల్యం)": "πrl",
            "TSA (సంపూర్ణ తల వైశాల్యం)": "πr(r + l)",
            "Volume (ఘనపరిమాణం)": "\\frac{1}{3}πr^2h"
        }
    elif "Sphere" in shape_name:
        fig.add_trace(draw_sphere())
        formulas = {
            "Surface Area (ఉపరితల వైశాల్యం)": "4πr^2",
            "Volume (ఘనపరిమాణం)": "\\frac{4}{3}πr^3"
        }
    elif "Cube" in shape_name:
        fig.add_trace(draw_cube())
        formulas = {
            "LSA (ప్రక్క తల వైశాల్యం)": "4a^2",
            "TSA (సంపూర్ణ తల వైశాల్యం)": "6a^2",
            "Volume (ఘనపరిమాణం)": "a^3"
        }

    fig.update_layout(scene=dict(xaxis_showticklabels=False, yaxis_showticklabels=False, zaxis_showticklabels=False),
                      margin=dict(l=0, r=0, b=0, t=0), height=500)
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.write("### Formulas (సూత్రాలు)")
    for name, f in formulas.items():
        st.info(f"**{name}**")
        st.latex(f)

st.warning("Note: Use your mouse to rotate and zoom the 3D shapes!")
