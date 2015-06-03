all:
	python manage.py loaddata microcontroller.json
	python manage.py loaddata processor.json
	python manage.py loaddata operatingSystem.json
	python manage.py loaddata gpu.json
	python manage.py loaddata microComputer.json
	python manage.py loaddata physicalCharacteristic.json
	python manage.py loaddata voltage.json
	python manage.py loaddata memory.json
	python manage.py loaddata interface.json
	python manage.py loaddata template.json
	
	
	