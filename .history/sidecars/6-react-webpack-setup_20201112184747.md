# Create a rack of dirs
First of all, let’s create all of the directories we need:

    mkdir -p ./frontend/src/{components,actions,reducers}
    mkdir -p ./frontend/{static,templates}/frontend

The above command should create the directories as follows:
```py
frontend/
  src/
    actions/
    components/
    reducers/
  static/
    frontend/
  templates/
    frontend/
```

# install packages

# cd into react frontend fold
    cd frontend

We need to create a package.json file by running the following command before installing packages:

# npm init
    npm init -y

        response=>
    Wrote to /Users/LHD/Documents/django-react-pgsql-todo/frontend/package.json:
    {
    "name": "frontend",
    "version": "1.0.0",
    "description": "",
    "main": "index.js",
    "scripts": {
        "test": "echo \"Error: no test specified\" && exit 1"
    },
    "keywords": [],
    "author": "",
    "license": "ISC"
    }

# install npm packages

    npm i -D webpack webpack-cli
    npm i -D @babel/core babel-loader @babel/polyfill @babel/preset-env @babel/preset-react babel-plugin-transform-class-properties
    npm i react react-dom react-router-dom
    npm i redux react-redux redux-thunk redux-devtools-extension
    npm i redux-form
    npm i axios
    npm i lodash

 
# Creating config files

Add a file named [.babelrc] to the overall project root directory and configure Babel:
```js
// .babelrc

{
  "presets": [
    [
      "@babel/preset-env",
      {
        "targets": {
          "node": "current"
        }
      }
    ],
    "@babel/preset-react"
  ],
  "plugins": ["transform-class-properties"]
}
```

We can use Async/Await with Babel by installing @babel/polyfill and writing as above.

Secondary, add a file named [webpack.config.js] to the same directory and write a configuration for webpack:

```js
// webpack.config.js

module.exports = {
  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader'
        }
      }
    ]
  }
};
```