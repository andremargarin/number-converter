# number-converter
Converts numbers to words. (sample project, for study purposes only)

## Build and run using docker

### Build
docker build -t number-converter .

### Run
docker run -d -p 5000:5000 --name=number-converter-webserver number-converter
