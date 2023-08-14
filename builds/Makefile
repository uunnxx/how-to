.PHONY dc run test clean

dc:
	docker-compose up --remove-orphans --build

run:
	python3 pre_run.py && TOKEN=token python3 run.py

test:
	test_it

clean:
	rm -rf some_cached_files
