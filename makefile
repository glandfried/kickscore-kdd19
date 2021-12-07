replicate.log: data
	make -C lib

data:
	wget https://zenodo.org/record/3351648/files/kickscore-kdd-20190725.tar.gz?download=1 -O kickscore-kdd-20190725.tar.gz
	tar xvf kickscore-kdd-20190725.tar.gz
	rm kickscore-kdd-20190725.tar.gz

path:
	if grep -Fxq "export KSEVAL_DATASETS=/home/landfried/meta/fork/kickscore-kdd19/data/" ~/.bashrc; then echo "True"; else cat "export KSEVAL_DATASETS=/home/landfried/meta/fork/kickscore-kdd19/data/" ~/.bashrc >>  ; fi

