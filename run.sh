pip3 install virtualenv --force-reinstall
python3 -m venv .env
source .env/bin/activate
python3 -m pip install -r requirements.txt
python3 main.py
