# HackerRank Test Case Generator

[<img src="https://image.flaticon.com/icons/svg/180/180867.svg" align="right" width="100">](#)
[<img src="https://brandfolder.com/hackerrank/logo/hackerrank-primary-logo.png" align="right" width="100">](https://www.hackerrank.com/)

[![](https://img.shields.io/travis/aashutoshrathi/HackerRank-Test-Case-Generator/master.svg?style=for-the-badge)](https://travis-ci.org/aashutoshrathi/HackerRank-Test-Case-Generator)

One Click Test Case Generation for HackerRank Problems.

Are you a Problem Author?

The toughest part of creating a problem is creating tricky, correct and constrained Test Cases.

Well, Here is one Click **Python** Code, for your respective logic(solution).

### Mentions

- [Blog post](https://medium.com/@agarwalrounak/my-nwoc-njack-winter-of-code-2018-experience-badf30b9c02d) on experince in NWoC 2018 by Rounak Agarwal.
- Selected as project in [GSSoC 2019](https://www.gssoc.tech/projects.html)
- Selected as project in [NJACKWinterOfCode 2018]([https://github.com/NJACKWinterOfCode/HackerRank-Test-Case-Generator](https://njackwinterofcode.github.io/))

### Python Codes and Examples

Logic File | TC Generator File |
------------------ | ------------- |
C / C++ / Java / Python | [TC Generator](/tc_generator/tc_gen.py) |

## Install

### How to Use ? 😃

* Clone the repository `$ git clone https://github.com/aashutoshrathi/HackerRank-Test-Case-Generator.git `

* Create a virtual environment `$ virtualenv venv `, 
[click here](https://stackoverflow.com/questions/14604699/how-to-activate-virtualenv) to read about activating virtualenv.

* #### Activate virtualenv (Linux)
```sh
   $ source ./venv/bin/activate
```
* #### Activate virtualenv (Windows)
```sh
   $ cd venv/Scripts/
   $ activate
   $ pip install -r requirements.txt
```   
* Go to ```sh tc_generator ``` and run the project.
```sh
   $ cd tc_generator/
   $ python tc_gen.py
```
### How it Works ? 🤔

![Demo](demo2.gif)

### Setup using Docker

```sh
  docker build . --tag=tcgen
  docker run -p 4000:80 tcgen
```   

## Stargazers over time 📈

[![Stargazers over time](https://starcharts.herokuapp.com/aashutoshrathi/HackerRank-Test-Case-Generator.svg)](https://starcharts.herokuapp.com/aashutoshrathi/HackerRank-Test-Case-Generator)


<p align="center"> Made with ❤ by <a href="https://github.com/aashutoshrathi">Aashutosh Rathi</a></p>
