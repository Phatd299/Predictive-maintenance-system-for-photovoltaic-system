import streamlit as st
import os
import numpy as np
import matplotlib.pyplot as plt
from keras.preprocessing.image import load_img, img_to_array
from keras.models import load_model
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Function to load and preprocess an image for prediction
def preprocess_image(image_path):
    img = load_img(image_path, target_size=(200, 200))
    img = img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = img.astype('float32') / 255.0
    return img

# Function to perform prediction using the loaded CNN model
def predict_image(image):
    # Load your trained CNN model here
    model = load_model('CNN/model.h5')  # Replace 'your_model.h5' with your model file

    # Make prediction
    prediction = model.predict(image)
    return prediction

# Function to display the CNN image classification page
def cnn_page():
    st.title('Image Classification with CNN')

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Display the uploaded image
        image = preprocess_image(uploaded_file)
        st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)

        # Perform prediction on the uploaded image
        prediction = predict_image(image)

        # Display prediction results
        st.subheader('Prediction:')
        if prediction[0][0] > prediction[0][1]:
            st.write('Predicted Class: Good')
        else:
            st.write('Predicted Class: Defect')

maintenance_system = None

def compute_fuzzy_logic(solar_irradiance_val, panel_temp_val, dc_voltage_val, humidity_val):
    global maintenance_system
    # Define Antecedents and Consequents (similar to the previous code snippet)
    solar_irradiance = ctrl.Antecedent(np.arange(0, 100, 1), 'solar_irradiance')
    panel_temperature = ctrl.Antecedent(np.arange(0, 60, 1), 'panel_temperature')
    dc_voltage = ctrl.Antecedent(np.arange(0, 1000, 1), 'dc_voltage')
    humidity = ctrl.Antecedent(np.arange(0, 101, 1), 'humidity')
    alert = ctrl.Consequent(np.arange(0, 101, 1), 'alert')
    performance = ctrl.Consequent(np.arange(0, 101, 1), 'performance')

    # Define membership functions and rules (similar to the previous code snippet)
    solar_irradiance['low'] = fuzz.trimf(solar_irradiance.universe, [0, 0, 50])
    solar_irradiance['medium'] = fuzz.trimf(solar_irradiance.universe, [20, 50, 80])
    solar_irradiance['high'] = fuzz.trimf(solar_irradiance.universe, [50, 100, 100])
    
    panel_temperature['low'] = fuzz.trapmf(panel_temperature.universe, [0,0, 10, 20])
    panel_temperature['medium'] = fuzz.trimf(panel_temperature.universe, [15, 25, 35])
    panel_temperature['high'] = fuzz.trapmf(panel_temperature.universe, [25, 35, 60, 60])

    dc_voltage['low'] = fuzz.trapmf(dc_voltage.universe, [0, 0, 250,350])
    dc_voltage['medium'] = fuzz.trapmf(dc_voltage.universe, [200,400, 550, 700])
    dc_voltage['high'] = fuzz.trapmf(dc_voltage.universe, [600,800, 1000, 1000])

    humidity['low'] = fuzz.trimf(humidity.universe, [0, 0, 50])
    humidity['medium'] = fuzz.trimf(humidity.universe, [25, 50, 75])
    humidity['high'] = fuzz.trimf(humidity.universe, [50, 100, 100])

    alert['green'] = fuzz.trimf(alert.universe, [0, 0, 50])
    alert['yellow'] = fuzz.trimf(alert.universe, [35, 50, 80])
    alert['red'] = fuzz.trimf(alert.universe, [65, 100, 100])

    performance['poor'] = fuzz.trimf(performance.universe, [0, 0, 35])
    performance['balanced'] = fuzz.trimf(performance.universe, [30, 50, 75])
    performance['excellent'] = fuzz.trimf(performance.universe, [70, 100, 100])

    # Define fuzzy rules
    rule1=ctrl.Rule(solar_irradiance['low'] & panel_temperature['low'] & dc_voltage['low'] & humidity['low'], (alert['red'], performance['poor']))
    rule2=ctrl.Rule(solar_irradiance['low'] & panel_temperature['low'] & dc_voltage['low'] & humidity['medium'], (alert['yellow'], performance['poor']))
    rule3=ctrl.Rule(solar_irradiance['low'] & panel_temperature['low'] & dc_voltage['low'] & humidity['high'], (alert['yellow'], performance['balanced']))
    rule4=ctrl.Rule(solar_irradiance['low'] & panel_temperature['low'] & dc_voltage['medium'] & humidity['low'], (alert['green'], performance['balanced']))
    rule5=ctrl.Rule(solar_irradiance['low'] & panel_temperature['low'] & dc_voltage['medium'] & humidity['medium'], (alert['green'], performance['balanced']))
    rule6=ctrl.Rule(solar_irradiance['low'] & panel_temperature['low'] & dc_voltage['medium'] & humidity['high'], (alert['yellow'], performance['balanced']))
    rule7=ctrl.Rule(solar_irradiance['low'] & panel_temperature['low'] & dc_voltage['high'] & humidity['low'], (alert['green'], performance['excellent']))
    rule8=ctrl.Rule(solar_irradiance['low'] & panel_temperature['low'] & dc_voltage['high'] & humidity['medium'], (alert['green'], performance['balanced']))
    rule9=ctrl.Rule(solar_irradiance['low'] & panel_temperature['low'] & dc_voltage['high'] & humidity['high'], (alert['yellow'], performance['balanced']))
    rule10=ctrl.Rule(solar_irradiance['low'] & panel_temperature['medium'] & dc_voltage['low'] & humidity['low'], (alert['red'], performance['poor']))
    rule11=ctrl.Rule(solar_irradiance['low'] & panel_temperature['medium'] & dc_voltage['low'] & humidity['medium'], (alert['yellow'], performance['balanced']))
    rule12=ctrl.Rule(solar_irradiance['low'] & panel_temperature['medium'] & dc_voltage['low'] & humidity['high'], (alert['yellow'], performance['balanced']))
    rule13=ctrl.Rule(solar_irradiance['low'] & panel_temperature['medium'] & dc_voltage['medium'] & humidity['low'], (alert['red'], performance['poor']))
    rule14=ctrl.Rule(solar_irradiance['low'] & panel_temperature['medium'] & dc_voltage['medium'] & humidity['medium'], (alert['yellow'], performance['balanced']))
    rule15=ctrl.Rule(solar_irradiance['low'] & panel_temperature['medium'] & dc_voltage['medium'] & humidity['high'], (alert['green'], performance['balanced']))
    rule16=ctrl.Rule(solar_irradiance['low'] & panel_temperature['medium'] & dc_voltage['high'] & humidity['low'], (alert['yellow'], performance['balanced']))
    rule17=ctrl.Rule(solar_irradiance['low'] & panel_temperature['medium'] & dc_voltage['high'] & humidity['medium'], (alert['yellow'], performance['balanced']))
    rule18=ctrl.Rule(solar_irradiance['low'] & panel_temperature['medium'] & dc_voltage['high'] & humidity['high'], (alert['yellow'], performance['balanced']))
    rule19=ctrl.Rule(solar_irradiance['low'] & panel_temperature['high'] & dc_voltage['low'] & humidity['low'], (alert['red'], performance['poor']))
    rule20=ctrl.Rule(solar_irradiance['low'] & panel_temperature['high'] & dc_voltage['low'] & humidity['medium'], (alert['red'], performance['poor']))
    rule21=ctrl.Rule(solar_irradiance['low'] & panel_temperature['high'] & dc_voltage['low'] & humidity['high'], (alert['yellow'], performance['poor']))
    rule22=ctrl.Rule(solar_irradiance['low'] & panel_temperature['high'] & dc_voltage['medium'] & humidity['low'], (alert['red'], performance['poor']))
    rule23=ctrl.Rule(solar_irradiance['low'] & panel_temperature['high'] & dc_voltage['medium'] & humidity['medium'], (alert['yellow'], performance['poor']))
    rule24=ctrl.Rule(solar_irradiance['low'] & panel_temperature['high'] & dc_voltage['medium'] & humidity['high'], (alert['green'], performance['poor']))
    rule25=ctrl.Rule(solar_irradiance['low'] & panel_temperature['high'] & dc_voltage['high'] & humidity['low'], (alert['red'], performance['poor']))
    rule26=ctrl.Rule(solar_irradiance['low'] & panel_temperature['high'] & dc_voltage['high'] & humidity['medium'], (alert['red'], performance['poor']))
    rule27=ctrl.Rule(solar_irradiance['low'] & panel_temperature['high'] & dc_voltage['high'] & humidity['high'], (alert['red'], performance['poor']))
    rule28=ctrl.Rule(solar_irradiance['medium'] & panel_temperature['low'] & dc_voltage['low'] & humidity['low'], (alert['yellow'], performance['poor']))
    rule29=ctrl.Rule(solar_irradiance['medium'] & panel_temperature['low'] & dc_voltage['low'] & humidity['medium'], (alert['green'], performance['balanced']))
    rule30=ctrl.Rule(solar_irradiance['medium'] & panel_temperature['low'] & dc_voltage['low'] & humidity['high'], (alert['green'], performance['balanced']))
    rule31=ctrl.Rule(solar_irradiance['medium'] & panel_temperature['low'] & dc_voltage['medium'] & humidity['low'], (alert['green'], performance['balanced']))
    rule32=ctrl.Rule(solar_irradiance['medium'] & panel_temperature['low'] & dc_voltage['medium'] & humidity['medium'], (alert['green'], performance['balanced']))
    rule33=ctrl.Rule(solar_irradiance['medium'] & panel_temperature['low'] & dc_voltage['medium'] & humidity['high'], (alert['yellow'], performance['balanced']))
    rule34=ctrl.Rule(solar_irradiance['medium'] & panel_temperature['low'] & dc_voltage['high'] & humidity['low'], (alert['green'], performance['excellent']))
    rule35=ctrl.Rule(solar_irradiance['medium'] & panel_temperature['low'] & dc_voltage['high'] & humidity['medium'], (alert['green'], performance['balanced']))
    rule36=ctrl.Rule(solar_irradiance['medium'] & panel_temperature['low'] & dc_voltage['high'] & humidity['high'], (alert['yellow'], performance['balanced']))
    rule37=ctrl.Rule(solar_irradiance['medium'] & panel_temperature['medium'] & dc_voltage['low'] & humidity['low'], (alert['yellow'], performance['poor']))
    rule38=ctrl.Rule(solar_irradiance['medium'] & panel_temperature['medium'] & dc_voltage['low'] & humidity['medium'], (alert['yellow'], performance['balanced']))
    rule39=ctrl.Rule(solar_irradiance['medium'] & panel_temperature['medium'] & dc_voltage['low'] & humidity['high'], (alert['yellow'], performance['balanced']))
    rule40=ctrl.Rule(solar_irradiance['medium'] & panel_temperature['medium'] & dc_voltage['medium'] & humidity['low'], (alert['green'], performance['balanced']))
    rule41=ctrl.Rule(solar_irradiance['medium'] & panel_temperature['medium'] & dc_voltage['medium'] & humidity['medium'], (alert['green'], performance['balanced']))
    rule42=ctrl.Rule(solar_irradiance['medium'] & panel_temperature['medium'] & dc_voltage['medium'] & humidity['high'], (alert['green'], performance['balanced']))
    rule43=ctrl.Rule(solar_irradiance['medium'] & panel_temperature['medium'] & dc_voltage['high'] & humidity['low'], (alert['green'], performance['excellent']))
    rule44=ctrl.Rule(solar_irradiance['medium'] & panel_temperature['medium'] & dc_voltage['high'] & humidity['medium'], (alert['green'], performance['excellent']))
    rule45=ctrl.Rule(solar_irradiance['medium'] & panel_temperature['medium'] & dc_voltage['high'] & humidity['high'], (alert['yellow'], performance['excellent']))
    rule46=ctrl.Rule(solar_irradiance['medium'] & panel_temperature['high'] & dc_voltage['low'] & humidity['low'], (alert['red'], performance['poor']))
    rule47=ctrl.Rule(solar_irradiance['medium'] & panel_temperature['high'] & dc_voltage['low'] & humidity['medium'], (alert['red'], performance['poor']))
    rule48=ctrl.Rule(solar_irradiance['medium'] & panel_temperature['high'] & dc_voltage['low'] & humidity['high'], (alert['yellow'], performance['balanced']))
    rule49=ctrl.Rule(solar_irradiance['medium'] & panel_temperature['high'] & dc_voltage['medium'] & humidity['low'], (alert['red'], performance['poor']))
    rule50=ctrl.Rule(solar_irradiance['medium'] & panel_temperature['high'] & dc_voltage['medium'] & humidity['medium'], (alert['yellow'], performance['balanced']))
    rule51=ctrl.Rule(solar_irradiance['medium'] & panel_temperature['high'] & dc_voltage['medium'] & humidity['high'], (alert['yellow'], performance['balanced']))
    rule52=ctrl.Rule(solar_irradiance['medium'] & panel_temperature['high'] & dc_voltage['high'] & humidity['low'], (alert['yellow'], performance['excellent']))
    rule53=ctrl.Rule(solar_irradiance['medium'] & panel_temperature['high'] & dc_voltage['high'] & humidity['medium'], (alert['green'], performance['balanced']))
    rule54=ctrl.Rule(solar_irradiance['medium'] & panel_temperature['high'] & dc_voltage['high'] & humidity['high'], (alert['yellow'], performance['balanced']))
    rule55=ctrl.Rule(solar_irradiance['high'] & panel_temperature['low'] & dc_voltage['low'] & humidity['low'], (alert['green'], performance['balanced']))
    rule56=ctrl.Rule(solar_irradiance['high'] & panel_temperature['low'] & dc_voltage['low'] & humidity['medium'], (alert['green'], performance['balanced']))
    rule57=ctrl.Rule(solar_irradiance['high'] & panel_temperature['low'] & dc_voltage['low'] & humidity['high'], (alert['yellow'], performance['balanced']))
    rule58=ctrl.Rule(solar_irradiance['high'] & panel_temperature['low'] & dc_voltage['medium'] & humidity['low'], (alert['green'], performance['balanced']))
    rule59=ctrl.Rule(solar_irradiance['high'] & panel_temperature['low'] & dc_voltage['medium'] & humidity['medium'], (alert['green'], performance['excellent']))
    rule60=ctrl.Rule(solar_irradiance['high'] & panel_temperature['low'] & dc_voltage['medium'] & humidity['high'], (alert['green'], performance['excellent']))
    rule61=ctrl.Rule(solar_irradiance['high'] & panel_temperature['low'] & dc_voltage['high'] & humidity['low'], (alert['yellow'], performance['balanced']))
    rule62=ctrl.Rule(solar_irradiance['high'] & panel_temperature['low'] & dc_voltage['high'] & humidity['medium'], (alert['red'], performance['balanced']))
    rule63=ctrl.Rule(solar_irradiance['high'] & panel_temperature['low'] & dc_voltage['high'] & humidity['high'], (alert['red'], performance['balanced']))
    rule64=ctrl.Rule(solar_irradiance['high'] & panel_temperature['medium'] & dc_voltage['low'] & humidity['low'], (alert['yellow'], performance['balanced']))
    rule65=ctrl.Rule(solar_irradiance['high'] & panel_temperature['medium'] & dc_voltage['low'] & humidity['medium'], (alert['yellow'], performance['balanced']))
    rule66=ctrl.Rule(solar_irradiance['high'] & panel_temperature['medium'] & dc_voltage['low'] & humidity['high'], (alert['yellow'], performance['balanced']))
    rule67=ctrl.Rule(solar_irradiance['high'] & panel_temperature['medium'] & dc_voltage['medium'] & humidity['low'], (alert['green'], performance['balanced']))
    rule68=ctrl.Rule(solar_irradiance['high'] & panel_temperature['medium'] & dc_voltage['medium'] & humidity['medium'], (alert['green'], performance['balanced']))
    rule69=ctrl.Rule(solar_irradiance['high'] & panel_temperature['medium'] & dc_voltage['medium'] & humidity['high'], (alert['green'], performance['balanced']))
    rule70=ctrl.Rule(solar_irradiance['high'] & panel_temperature['medium'] & dc_voltage['high'] & humidity['low'], (alert['yellow'], performance['balanced']))
    rule71=ctrl.Rule(solar_irradiance['high'] & panel_temperature['medium'] & dc_voltage['high'] & humidity['medium'], (alert['green'], performance['excellent']))
    rule72=ctrl.Rule(solar_irradiance['high'] & panel_temperature['medium'] & dc_voltage['high'] & humidity['high'], (alert['yellow'], performance['balanced']))
    rule73=ctrl.Rule(solar_irradiance['high'] & panel_temperature['high'] & dc_voltage['low'] & humidity['low'], (alert['red'], performance['poor']))
    rule74=ctrl.Rule(solar_irradiance['high'] & panel_temperature['high'] & dc_voltage['low'] & humidity['medium'], (alert['red'], performance['poor']))
    rule75=ctrl.Rule(solar_irradiance['high'] & panel_temperature['high'] & dc_voltage['low'] & humidity['high'], (alert['red'], performance['balanced']))
    rule76=ctrl.Rule(solar_irradiance['high'] & panel_temperature['high'] & dc_voltage['medium'] & humidity['low'], (alert['yellow'], performance['balanced']))
    rule77=ctrl.Rule(solar_irradiance['high'] & panel_temperature['high'] & dc_voltage['medium'] & humidity['medium'], (alert['yellow'], performance['balanced']))
    rule78=ctrl.Rule(solar_irradiance['high'] & panel_temperature['high'] & dc_voltage['medium'] & humidity['high'], (alert['yellow'], performance['poor']))
    rule79=ctrl.Rule(solar_irradiance['high'] & panel_temperature['high'] & dc_voltage['high'] & humidity['low'], (alert['green'], performance['excellent']))
    rule80=ctrl.Rule(solar_irradiance['high'] & panel_temperature['high'] & dc_voltage['high'] & humidity['medium'], (alert['yellow'], performance['balanced']))
    rule81=ctrl.Rule(solar_irradiance['high'] & panel_temperature['high'] & dc_voltage['high'] & humidity['high'], (alert['yellow'], performance['balanced']))

    # Define ControlSystem and ControlSystemSimulation
    maintenance_ctrl = ctrl.ControlSystem([rule1,rule2,rule3,rule4,rule5,rule6,rule7,rule8,rule9,rule10,rule11,rule12,rule13,rule14,rule15,rule16,rule17,rule18,rule19,rule20,rule21,rule22,rule23,rule24,rule25,rule26,rule27,rule28,rule29,rule30,rule31,rule32,rule33,rule34,    rule35, rule36, rule37, rule38, rule39, rule40, rule41, rule42, rule43, rule44, rule45, rule46, rule47, rule48, rule49, rule50, rule51, rule52, rule53, rule54, rule55, rule56, rule57, rule58, rule59, rule60, rule61, rule62, rule63, rule64, rule65, rule66, rule67, rule68, rule69, rule70, rule71, rule72, rule73, rule74, rule75, rule76, rule77, rule78, rule79, rule80, rule81])
    maintenance_system = ctrl.ControlSystemSimulation(maintenance_ctrl)

    # Compute using inputs
    maintenance_system.input['solar_irradiance'] = solar_irradiance_val
    maintenance_system.input['panel_temperature'] = panel_temp_val
    maintenance_system.input['dc_voltage'] = dc_voltage_val
    maintenance_system.input['humidity'] = humidity_val
    maintenance_system.compute()


    # Return computed outputs
    return maintenance_system.output['alert'], maintenance_system.output['performance']

# Function to display the fuzzy logic page
def fuzzy_logic_page():
    global maintenance_system
    st.title('Solar Panel Maintenance and Performance Monitoring')
    
    # Fuzzy logic inputs
    solar_irradiance_val = st.slider('Solar Irradiance (W/m2)', 0, 100, 50)
    panel_temp_val = st.slider('Panel Temperature (Celsius)', 0, 60, 25)
    dc_voltage_val = st.slider('DC Voltage Output (V)', 0, 1000, 500)
    humidity_val = st.slider('Humidity (%)', 0, 100, 50)

    submitted = st.button('Submit')  # Add a submit button
    if submitted:
        try:
            # Compute fuzzy logic outputs
            alert, performance = compute_fuzzy_logic(solar_irradiance_val, panel_temp_val, dc_voltage_val, humidity_val)
            
            # Display fuzzy logic outputs
            st.subheader('Fuzzy Logic Outputs')
            st.write('Maintenance Alerts:', alert, '%')
            st.write('Performance Monitoring:', performance, '%')
                    
        except Exception as e:
            st.error(f"An error occurred: {e}")


st.sidebar.title('Menu')
selection = st.sidebar.radio("Go to", ["CNN Image Classification", "Fuzzy Logic"])

# Render the selected page
if selection == "CNN Image Classification":
    cnn_page()
elif selection == "Fuzzy Logic":
    fuzzy_logic_page()
