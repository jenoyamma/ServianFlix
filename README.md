# servianflix-intro2sagemaker

This repository contains the workshop and website material for the AWS AI/ML SageMaker session delivered at Servian. 
The workshop consists of using SageMaker to train, build and deploy models. You can find the notebook material in scripts. Users will be able to build a movie recommendation system (using MovieLens ml-100k data) using Factorization Machines and deploy it as an endpoint. Servianflix was created to show the movie that was recommended to the user (Top 45 movies). Users will also be able to view the probability score of them liking that movie as well. You will need to set up lambda and dynamodb table, essentially just a table that has movie_id as the pk and attributes of the movies (description, genre, poster_url etc), the movie metadata can be found in script/notebook. 

# To Run Servianflix

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```
