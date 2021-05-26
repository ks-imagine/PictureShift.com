# PictureShift

Extract text from images using Tesseract OCR.


## Getting Started

### Prerequisites

Kindly ensure you have the following installed:
- [ ] [Python 3.6](https://www.python.org/downloads/release/python-365/)
- [ ] [Pip](https://pip.pypa.io/en/stable/installing/)
- [ ] [Virtualenv](https://virtualenv.pypa.io/en/stable/installation/)

### Setting up + Running

1. Clone the repo:

    ```
    $ git clone https://github.com/ks-imagine/PictureShift.com.git
    ```

2. With Python 3.6 and Pip installed:

    ```
    $ virtualenv --python=python3 env --no-site-packages
    $ source env/bin/activate
    $ pip install -r requirements.txt
    ```

3. Export the required environment variables:

    ```
    $ export FLASK_APP=app/app.py
    ```

4. Run the Flask API:

    ```
    $ flask run
    ```

5. Navigate to `http://localhost:5000/` to view the application.