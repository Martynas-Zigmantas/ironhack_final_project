<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/Martynas-Zigmantas/ironhack_final_project">
    <img src="AI Model/images/home_image.png" alt="Logo" width="1200" height="150">
  </a>

  <h3 align="center">Streamlit Travel Assistant</h3>

  <p align="center">
    An AI prediction model to predict departure lateness and a visual dashboard of destinations with direct flying airlines.
    <br />
  </p>
</div>

<div align="center">

[![LinkedIn][linkedin-shield]][linkedin-url]

</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project

<div align="center">
  <a href="https://github.com/Martynas-Zigmantas/ironhack_final_project">
    <img src="AI Model/images/screen_shot.png" alt="Screen shot" width="650" height="350">
  </a>
</div>


I wanted to create tool that would allow the user to organise their travel plan. With a visual dashboard that gives direct insight to the available destinations from a selected airport and the airlines that can take you there. Along with that a machine learning model that can give the user a prediction of the chance of tardiness and an estimation of it.

Here's how:
* Created and maintained a complete pipeline from extraction to transformation, storage and automated appending of new data
* Scraped roughly 40,000 flight records from 3 different airports in Europe
* Transformed the data to make tables
* Create interactive visual dashboard
* Extract and engineer features for training the predictive models
* Deploy the model and dashboard to a web application


<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With


* [![Pandas][Pandas.js]][Pandas-url]
* [![Numpy][Numpy.js]][Numpy-url]
* [![Scikit Learn][Scikit.js]][Scikit-url]
* [![Selenium][Selenium.js]][Selenium-url]
* [![MySQL][MySQL.js]][MySQL-url]
* [![Tableau][Tableau.js]][Tableau-url]
* [![Streamlit][Streamlit.js]][Streamlit-url]
* [![Python][Python.js]][Python-url]


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To run this project locally, clone this repository to your device and run the "app.py" file.


### Installation

_Follow the step by step instructions below._

1. Clone the repo
   ```sh
   git clone https://github.com/Martynas-Zigmantas/ironhack_final_project.git
   ```

2. Set the directory to `ironhack_final_project/AI Model`
   ```sh
   cd ironhack_final_project/AI Model
   ```

3. Create a new virtual environment in your IDE
   ```sh
   python3 -m venv env
   ```

4. Activate the virtual environment

    *	On Mac:
		   ```sh
		   source venv/bin/activate
		   ```
    *	On Windows:
		   ```sh
		   .\venv\Scripts\activate
		   ```

5. Install `requirements.txt`
   ```sh
   pip install -r requirements.txt
   ```
6. In the terminal, run the Streamlit app
   ```sh
   streamlit run app.py
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Scrape raw data
- [x] Transform data into tables
- [x] Create and update database
- [x] Create visual dashboard
- [x] Extract and engineer features
- [x] Train predictive models
- [x] Deploy Streamlit app with predictive models
- [ ] Embed interactive dashboard into Streamlit app
- [ ] Display bulk predictions in app
- [ ] Multi-language Support
    - [x] English
    - [ ] Chinese
    - [ ] Spanish

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Top contributors:

<a href="https://github.com/Martynas-Zigmantas/ironhack_final_project/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=Martynas-Zigmantas/ironhack_final_project" alt="contribution.rocks image" />
</a>

<p align="right">(<a href="#readme-top">back to top</a>)</p>




<!-- CONTACT -->
## Contact

Martynas Zigmantas - [My LinkedIn](https://www.linkedin.com/in/martynas-zigmantas) - mz124512@gmail.com

Project Link: [https://github.com/Martynas-Zigmantas/ironhack_final_project](https://github.com/Martynas-Zigmantas/ironhack_final_project)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/Martynas-Zigmantas/ironhack_final_project.svg?style=for-the-badge
[contributors-url]: https://github.com/Martynas-Zigmantas/ironhack_final_project/graphs/contributors
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/martynas-zigmantas/
[product-screenshot]: images/screenshot.png
[Python.js]: https://img.shields.io/badge/python%203-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/
[Pandas.js]: https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white
[Pandas-url]: https://pandas.pydata.org/
[Numpy.js]: https://img.shields.io/badge/numpy-013243?style=for-the-badge&logo=numpy&logoColor=white
[Numpy-url]: https://numpy.org/
[Scikit.js]: https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white
[Scikit-url]: https://scikit-learn.org/stable/
[Selenium.js]: https://img.shields.io/badge/selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white
[Selenium-url]: https://www.selenium.dev/
[MySQL.js]: https://img.shields.io/badge/mysql%20workbench-4479A1?style=for-the-badge&logo=mysql&logoColor=white
[MySQL-url]: https://www.mysql.com/
[Tableau.js]: https://img.shields.io/badge/tableau-E97627?style=for-the-badge&logo=tableau&logoColor=white
[Tableau-url]: https://public.tableau.com/app/discover
[Streamlit.js]: https://img.shields.io/badge/streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white
[Streamlit-url]: https://streamlit.io/