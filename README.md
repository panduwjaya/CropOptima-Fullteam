<br/>
<p align="center">
  <a href="https://github.com/panduwjaya/CropOptima-Fullteam/">
    <img src="logo-transparent.png" alt="Logo">
  </a>

  <h3 align="center">Crop Optima</h3>

  <p align="center">
    An Awesome application taht can give you plant suggestion based on your location!
    <br/>
    <br/>
  </p>
</p>

![Downloads](https://img.shields.io/github/downloads/panduwjaya/CropOptima-Fullteam/total)![Contributors](https://img.shields.io/github/contributors/panduwjaya/CropOptima-Fullteam?color=dark-green) ![Issues](https://img.shields.io/github/issues/panduwjaya/CropOptima-Fullteam) ![License](https://img.shields.io/github/license/panduwjaya/CropOptima-Fullteam)

## Table Of Contents

* [About the Project](#about-the-project)
* [Authors](#authors)
* [Getting Started](#getting-started)
    * [Machine Learning](#machine-learning)
    * [Cloud Computing](#cloud-computing)
    * [Mobile Development](#mobile-development)
* [Usage](#usage)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Acknowledgements](#acknowledgements)

## About The Project

![Screen Shot](images/screenshot.png)

We make a mobile application that can give plant sugestion based on your location na dyour enviroment situation, such as
Nitrogen, Fosfor, an Kalium. With that data we send it to out Machine Learning model and the model will give us the
suggestion plant as result. The model itself created by using dataset. Our mobile application do communication with the
Machine Learning Model via API which created by our personil too.

## Authors

|            Nama            | Bangkit-ID  |        Path        |
|:--------------------------:|:-----------:|:------------------:|
|      Odista Dwi Putra      | M226BSY1570 |  Machine Learning  |
| Prayogo Makarya Alexandria | M001BSY0200 |  Machine Learning  |
|      Devano Danendra       | M226BSY0749 |  Machine Learning  |
|  Alvin Reihansyah Makarim  | C248BSY3644 |  Cloud Computing   |
|        Muhkito Afif        | C248BSY3747 |  Cloud Computing   |
|        Pandu Wijaya        | A248BSY1976 | Mobile Development |
|  Muammar Mufid Darmindra   | A548BKY4474 | Mobile Development |

## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Machine Learning

<details>
<summary> Library and Framework </summary>

* [Tensorflow](https://www.tensorflow.org/) :
* [Numpy](https://numpy.org/)
* [Keras](https://keras.io/)
* [Jupyter Notebook](https://jupyter.org/)

</details>

<details>
<summary>  How to run </summary> 

1. Clone [this](https://github.com/panduwjaya/CropOptima-Fullteam.git) repository and open the folder
2. Open file `/MachineLearning/File Py/Capstone_Project_Bangkit.ipynb` in your Jupyter Notebook or Google Collab
3. Build and run the `.ipynb` file
4. Use the generated model to predict with required data

</details>

### Cloud Computing

<details>
<summary> Library and Platform </summary>

* [Express Js](https://expressjs.com/)
* [Docker](https://docker.com/)
* [Cloudrun](https://cloud.google.com/run)
* [Flask](https://flask.palletsprojects.com/)
* [Python >= 3.8](https://www.python.org/)

</details>

<details>
<summary>  How to run </summary> 

1. Clone [this](https://github.com/panduwjaya/CropOptima-Fullteam.git) repository and open the folder
2. Open directory `/CloudComputing`
3. If you want use database to saving your history go to `/database-api` otherwise `/model-api`
4. Don't forget include the Machine Learning Model
3. Open your terminal and install all dependencies with

```sh
pip install -r requirements.txt
```

4. Run API

```sh
python3 main.py
```

5. Access API at `http://localhost:5000`

</details>

### Mobile Development

<details>
<summary> Library and Platform </summary>

* [Material 3](https://m3.material.io/) : Used as User Interface library that can help you make your design look more
  beautiful
* [Retrofit](https://square.github.io/retrofit/) : Retrofit is a library that can help application to make API call and
  handling API
* [Glide](https://github.com/bumptech/glide) : This library is useful for showing images from URL to ImageView
* [Firebase](https://github.com/bumptech/glide) : Firebase is one of most popular library to handling Authorization
* [Android Studio](https://developer.android.com/studio)

</details>
<details>
<summary>  How to run </summary> 

1. Clone [this](https://github.com/panduwjaya/CropOptima-Fullteam.git) repository
2. Open directory `/MobileDevelopment `in your Android Studio
3. Build and run your application

</details>
<br>
</br>
<br>
</br>
<br>
</br>
<br>
</br>
##############EXAMPLE

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.

* npm

```sh
npm install npm@latest -g
```

### Installation

1. Get a free API Key at [https://example.com](https://example.com)

2. Clone the repo

```sh
git clone https://github.com/your_username_/Project-Name.git
```

3. Install NPM packages

```sh
npm install
```

4. Enter your API in `config.js`

```JS
const API_KEY = 'ENTER YOUR API';
```

## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos
work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

## Roadmap

See the [open issues](https://github.com/ShaanCoding/ReadME-Generator/issues) for a list of proposed features (and known
issues).

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any
contributions you make are **greatly appreciated**.

* If you have suggestions for adding or removing projects, feel free
  to [open an issue](https://github.com/ShaanCoding/ReadME-Generator/issues/new) to discuss it, or directly create a
  pull request after you edit the *README.md* file with necessary changes.
* Please make sure you check your spelling and grammar.
* Create individual PR for each suggestion.
* Please also read through
  the [Code Of Conduct](https://github.com/ShaanCoding/ReadME-Generator/blob/main/CODE_OF_CONDUCT.md) before posting
  your first idea as well.

### Creating A Pull Request

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See [LICENSE](https://github.com/ShaanCoding/ReadME-Generator/blob/main/LICENSE.md)
for more information.

## Acknowledgements

* [ShaanCoding](https://github.com/ShaanCoding/)
* [Othneil Drew](https://github.com/othneildrew/Best-README-Template)
* [ImgShields](https://shields.io/)
