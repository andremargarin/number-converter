# number-converter
Converts numbers to words. (sample project, for study purposes only)

[![CircleCI - Dev](https://circleci.com/gh/andremargarin/number-converter/tree/dev.svg?style=svg)
[![CircleCI - Master](https://circleci.com/gh/andremargarin/number-converter/tree/master.svg?style=svg)

## Build and run using docker

### Build
docker build -t number-converter .

### Run
docker run -d -p 5000:5000 --name=number-converter-webserver number-converter
