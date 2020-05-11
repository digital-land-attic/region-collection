init: 
	pip3 install -r requirements.txt

collect/boundaries:
	python3 collect_boundaries.py
	python3 split_boundaries.py

collect/regions:
	python3 collect.py

clean:
	rm -r collection/*
	rm -r index/*
