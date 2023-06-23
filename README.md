# Machine Translation Model Hosting

This project provides a simple solution for hosting machine translation models locally. It allows you to generate a configuration based on a provided SQLite database and easily deploy the models on your machine. The project combines Python and bash scripts to automate the setup process and provide easy access to the models through HTTP requests.
This project is complementary to Voss, a web API built for communicating with machine translation models.

#### Credits
I would like to dedicate this project to the incredible team behind OpenNMT, whose exceptional work has made this project possible. OpenNMT is a powerful and versatile machine translation framework that has revolutionized the field of neural machine translation.

## Features
- Easy setup and deployment of machine translation models
- Utilizes a SQLite database for storing model configurations
- Host multiple models simultaneously
- Supports various translation frameworks
- Customizable configuration options
- Monitoring and logging capabilities

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/DanielGall500/OpenNMT-MT-Server.git
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Make sure you have SQLite installed on your machine. If not, follow the official SQLite documentation to install it.

## Usage

1. Prepare your SQLite database with the necessary model configurations. You can use the provided `database.db` file as a template and modify it according to your needs.

2. Start the model hosting server:

   ```bash
   bash run_model_hosting.sh
   ```

   This will launch the server and load the models according to the generated configuration.

3. Access the translation API through the following URL:

   ```
   http://localhost:[PORT]/translator/translate
   ```

4. Monitor the server logs and performance as needed.

## Configuration

The `config.json` file contains the configuration for your machine translation models. You can modify it to adjust various settings such as model paths, byte-pair encoding paths, GPU configuration, etc. However, you do not need to modify this yourself. Simply modify the SQLite database and on each startup a new configuration will be automatically generated.

## Contribution

Contributions are welcome! If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request on the GitHub repository.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute it according to the terms of the license.

## Acknowledgments

We would like to express our gratitude to the open-source community and the developers of the frameworks and libraries used in this project. Their contributions and hard work make projects like this possible.
