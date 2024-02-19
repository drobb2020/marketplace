<div id="top"></div>
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
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/drobb2020/marketplace">
    <img src="static/assets/logo.png" alt="Logo" height="100">
  </a>

<h3 align="center">Marketplace</h3>

  <p align="center">
    This is a Django project presented on YouTube by FreeCodeCamp, and authored by Code with Stein. The project is a way for users to sell items to other people on the web.
    <br />
    <a href="https://github.com/drobb2020/marketplace"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/drobb2020/marketplace">View Demo</a>
    ·
    <a href="https://github.com/drobb2020/marketplace/issues">Report Bug</a>
    ·
    <a href="https://github.com/drobb2020/marketplace/issues">Request Feature</a>
  </p>
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
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

This is a fun project and includes some very useful apps especially conversation, and dashboard. Check out the entire project on [YouTube](https://www.youtube.com/watch?v=ZxMB6Njs3ck).

<p align="right">(<a href="#top">back to top</a>)</p>

### Built With

* [Django](https://www.djangoproject.com/)
* [Tailwindcss](https://tailwindcss.com/)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

You will need a recent version of Python installed on your OS (Windows/Mac/Linux), and the basic knowledge of how to setup and start a Django project. This was built with the most recent version of Django (5.0.2) to make it as current as possible. The only extra package that was installed is django-extensions.

See `PROJECT_SETUP.md` for more detailed instructions.

### Prerequisites

You should always create a virtual environment to keep you projects properly isolated from each other. To create a virtual environment you can install virtualenv globally or use venv.

```sh
python -m venv venv
```

This will create a virtual environment named venv. To activate this environment run:

```sh
venv/bin/activate (macos)
```

To deactivate the virtual environment run:

```sh
deactivate
```

### Installation

1. A way to quick start your development is to clone this repo.
2. Clone the repo from github

   ```sh
   git clone https://github.com/drobb2020/marketplace.git
   ```

3. Install the needed packages into the virtual environment (make sure it is active):

   ```sh
   pip install -r requirements.txt
   pip install -r requirements-dev.txt
   ```

4. Make migrations and a superuser for the database:

    ```sh
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
    ```

5. Run the django development server:

   ```sh
   python manage.py runserver
   ```

6. Have fun!

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

The idea is that people can setup their own account and add items they want to sell. The inbox/conversation system allows other users to contact the seller and make an offer for the item.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/drobb2020/marketplace/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>

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

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

David Robb - drobb2011@gmail.com

Project Link: [https://github.com/drobb2020/marketplace](https://github.com/drobb2020/marketplace)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [FreeCodeCamp](https://www.youtube.com/@freecodecamp)
* [Code with Stein](https://www.youtube.com/@CodeWithStein)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/drobb2020/marketplace.svg?style=for-the-badge
[contributors-url]: https://github.com/drobb2020/marketplace/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/drobb2020/marketplace.svg?style=for-the-badge
[forks-url]: https://github.com/drobb2020/marketplace/network/members
[stars-shield]: https://img.shields.io/github/stars/drobb2020/marketplace.svg?style=for-the-badge
[stars-url]: https://github.com/drobb2020/marketplace/stargazers
[issues-shield]: https://img.shields.io/github/issues/drobb2020/marketplace.svg?style=for-the-badge
[issues-url]: https://github.com/drobb2020/marketplace/issues
[license-shield]: https://img.shields.io/github/license/drobb2020/marketplace.svg?style=for-the-badge
[license-url]: https://github.com/drobb2020/marketplace/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: static/assets/screenshot.png
