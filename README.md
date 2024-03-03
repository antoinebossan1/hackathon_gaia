# 🌱 Gaia Mistral Hackathon Project 🌍

## Introduction 📖

I participated in the Gaia Hackathon, an initiative by La Ferme Digitale in collaboration with Mistral AI, alongside fellow students from CentraleSupélec. Held on the 26th and 27th of February, the event aimed at tackling significant agricultural challenges through the application of Generative Artificial Intelligence. My contribution to this collaborative effort was the development of a data enhancement module. This module enabled the Mistral Large Language Model (LLM) to interface with real-time databases on weather conditions, authorized animal medicines, and approved pesticides, with the aim of sharing the code I developed for this purpose.

Upon completing my development work, my teammates and I integrated this data enhancement with other functionalities, such as an interactive map, resulting in a smart dashboard designed specifically for farmers. 

For more details about the hackathon, you can find the description [here](https://www.lafermedigitale.fr/gaia/).


## Features ✨

- **Current Weather Data Integration**: Access real-time weather data to make informed agricultural decisions.
- **Animal Medicines Database**: Consult authorized animal medicines to ensure the well-being of livestock.
- **Pesticides Database**: Access information on authorized pesticides to protect crops effectively.

## Getting Started 🚀

To get a local copy up and running follow these simple steps.

### Prerequisites

- Git (Installation guide: [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git))
- Ensure you have entered your Mistral API key and the name of the model you want to use in the `.env` file for the project to function correctly.

### Installation

1. **Clone the repo:**

git clone https://github.com/antoniebossan1/hackathon_gaia.git

2. **Navigate into the project directory:**

cd hackathon_gaia

3. **Run the initialization command:**
Use the `make init` command to automate the setup of a virtual environment and the installation of dependencies.

This will:
- Create a Python virtual environment named `hackaton_venv`.
- Activate the virtual environment.
- Upgrade pip to its latest version.
- Install the required Python packages listed in `requirements/requirements.txt`.
4. **Download and prepare the data:**

Execute the `get_data.sh` script to download the necessary dataset and prepare it for use.

This script will:
- Download the dataset and save it under the `xls` directory.
- Convert specific sheets to CSV format and clean the data.


### Usage

1. **Ensure the virtual environment is activated:**
2. **Enter your question in the `main` function of `enhanced_query_response.py`.** This involves editing the file to include your specific query.
3. **Run the application:**
python -m enhanced_query_response

This will process your query through the `enhanced_query_response.py` module and display the results.

## Contributing 🤝

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature`)
3. Commit your Changes (`git commit -m 'Add feature'`)
4. Push to the Branch (`git push origin feature`)
5. Open a Pull Request

## License 📜

Distributed under the MIT License. See `LICENSE` for more information.


