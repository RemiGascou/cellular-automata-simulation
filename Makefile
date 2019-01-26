BASEDIR=./Ceausi
TESTDIR=./Ceausi/tests

all : clean tests

clean :
	@rm -rf `find ./ -type d -name "*__pycache__"`
tests :
	@python3 ${BASEDIR}/main_tests.py `if [ ${DISPLAY} ]; then echo "1"; else echo "0"; fi;`
build :
	python3 setup.py sdist
upload :
	python3 setup.py sdist upload
