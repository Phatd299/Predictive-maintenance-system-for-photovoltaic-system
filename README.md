# Predictive maintenance system for photovoltaic system

[**Update**: You can find the paper [here](https://onedrive.live.com/embedresid=8d775148de787d87%211424&authkey=!AJFlhwnj7LJytiU&em=2)]

## Solution Presentation
This study presents a predictive maintenance system for photovoltaic (PV) installations. It attempts to improve PV system efficiency and maintenance operations by utilizing AI algorithm such as fuzzy logic and a Convolutional Neural Network (CNN) model.

![abc2](https://github.com/Phatd299/Renewable-Energy/assets/110618138/ae68760c-0e69-4a32-afc2-3842fdb75a4c)

Using fuzzy logic, this project analyzes 4 input data: solar irradiance, panel temperature, voltage output, and humidity. The fuzzy logic algorithm generates alertness levels (green, yellow, and red) to show the system's state of alertness, as well as performance categorization of the PV system (good, balanced, or poor). Additionally, by analyzing images of the panels, the CNN system accurately distinguishes between working and broken solar panels.

## Installation
### Prerequisites

Python 3.6 or higher
Libraries specified in requirements.txt

## Installation Steps

1. Clone the repository.
    ```bash
    git clone https://github.com/Phatd299/Renewable-Energy.git
    cd Renewable-Energy
    ```

2. Install dependencies.
    ```bash
    pip install -r requirements.txt
    ```
## Usage

1. Ensure the model (`model.h5`) is available in the project directory.
2. Run the defect detection system using the provided Jupyter Notebook or Python script.
3. Provide images of products to be classified and analyze the results.

## Directory Structure

RE_Application
│   README.md               # Overview and instructions
│   requirements.txt        # List of Python dependencies
│   app.py                  # Main application file
│
└───CNN
│   │   RE_CNN_Images       # Dataset for training and testing the CNN model
│   │   RE_Test_Images      # Images for final product validation
│   │   model.h5            # Trained CNN model stored in H5 format
│   │   RE_CNN.ipynb        # Jupyter notebook for CNN development
│   
└───Fuzzy Logic
    │   Fuzzy rules.xlsx    # Excel file containing 81 fuzzy rules
    │   RE_Fuzzy_Logic.ipynb # Jupyter notebook for Fuzzy Logic development

## Examples

![Example](<img width="944" alt="Picture1" src="https://github.com/Phatd299/Renewable-Energy/assets/110618138/85044eee-7453-46ee-8ba8-f08e8cfddbae">)

*Image showing the defect detection system in action.*

## Contributing

Feel free to contribute by opening issues or submitting pull requests. All contributions are welcome!

## Credits

- [Phat Dang](https://github.com/Phatd299)
- The project uses libraries such as Keras, NumPy, and Matplotlib.
