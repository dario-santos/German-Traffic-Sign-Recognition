<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Stars][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![GNU GPLv3 License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <h3 align="center">A Machine Learning model that classifies german traffic signs</h3>

  <p align="center">
    A CNN based model constructed using tensorflow 2.0 and Keras that can detect german traffic signs. 
    <br />
    ·
    <a href="https://github.com/dario-santos/CNN-Machine-Learning-Model/issues">Report a Bug</a>
    ·
    <a href="https://github.com/dario-santos/CNN-Machine-Learning-Model/issues">Request a Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Roadmap](#roadmap)
* [License](#license)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)



<!-- ABOUT THE PROJECT -->
## About The Project

This is one of my personal projects, used so I can learn more about a particular subject.

This is my take on a competition long ago closed, but that is still relevant as a beginners project of machine learning and multiclass classification.

My project was built using Tensorflow 2.0 with the built-in Keras framework. The architecture of my network is a simple CNN with multiple groups of two convolutional layers and one max pooling, I used intercalated dropout layers to dimish the overfitting of the model. It as a 97% accuracy in the test group.

As a necessity, I coded two scripts to create three groups from the main data set (training, validation, and test) their use is explained below.



### Built With

* [Tensorflow](https://www.tensorflow.org)
* [Keras](https://keras.io)


<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

You will need the GTSRB dataset and Tensorflow 2.0 to execute all of the scripts.
If you only want the model simple copy the gtsrb_model.h5 file.

### Installation

1. Clone the repo
```sh
git clone https:://github.com/dario-santos/CNN-Machine-Learning-Model.git
```
2. Download the GTSRB dataset (link in the end)
3. Run the prepare_data.py script

<!-- USAGE EXAMPLES -->
## Usage

1. Run the model.py to train the model **It's recommended to use a GPU as it's fastest**
2. If you want to test your model in the test dataset you can do it by running the model_predict.py script.

**If you only want the model it's the .h5 file.**


<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/dario-santos/CNN-Machine-Learning-Model/issues) for a list of proposed features (and known issues).

<!-- LICENSE -->
## License

Distributed under the GNU GPLv3 License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Dário Santos - [LinkedIn](https://www.linkedin.com/in/dariovfsantos) - dariovfsantos@gmail.com

Project Link: [https://github.com/dario-santos/CNN-Machine-Learning-Model](https://github.com/dario-santos/CNN-Machine-Learning-Model)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [Img Shields](https://shields.io)
* [Choose an Open Source License](https://choosealicense.com)
* [GTSRB](http://benchmark.ini.rub.de/?section=gtsrb&subsection=news)


<!-- MARKDOWN LINKS & IMAGES -->
[stars-shield]: https://img.shields.io/github/stars/dario-santos/CNN-Machine-Learning-Model
[stars-url]: https://github.com/dario-santos/CNN-Machine-Learning-Model/stargazers
[issues-shield]: https://img.shields.io/github/issues/dario-santos/CNN-Machine-Learning-Model
[issues-url]: https://github.com/dario-santos/CNN-Machine-Learning-Model/issues
[license-shield]: https://img.shields.io/github/license/dario-santos/CNN-Machine-Learning-Model
[license-url]: https://github.com/dario-santos/CNN-Machine-Learning-Model/blob/master/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/dariovfsantos/
