# Run mongoDB in a docker container:
- `docker volume create mongodbdata`
- `docker run --name mongodb -d -p 27017:27017 -v mongodbdata:/data/db mongo`

# Convert jupyter notebook to pdf:
- `jupyter nbconvert .\main_report.ipynb --to webpdf --TagRemovePreprocessor.remove_input_tags='{"hide-input"}' --no-prompt`
