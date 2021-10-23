replicate.log: data
	python3 replicate.py

data:
	wget https://zenodo.org/record/3351648/files/kickscore-kdd-20190725.tar.gz?download=1 -O kickscore-kdd-20190725.tar.gz
	tar xvf kickscore-kdd-20190725.tar.gz

