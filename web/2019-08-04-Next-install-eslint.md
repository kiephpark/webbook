## 설치하기
---
아래와 같이 npm으로 next및 react를 설치해 주고, eslint 및 webpack도 설치하자
```
npm i --save react react-dom next antd prop-types axios
npm i -D nodemon webpack
npm i -D eslint eslint-plugin-import eslint-plugin-react eslint-plugin-react-hooks babel-eslint eslint-config-airbnb eslint-plugin-jsx-a11y
```

아래와 같이 package.json을 next로 변경하자. next는 라우팅 시스템 및 여러 기능을 지원해 주므로 next를 실행주여야 한다. `npm run dev` 를 하면 서버가 실행된다. 기본 페이지가 없어서 404 에러가 발생한다.
```
  "scripts": {
    "dev": "next",
    "build": "next build",
    "start": "next start"
  },
```
express와 함께 서버를 동작시키려면, server.js 생성, package.json 수정, nodemon.json파일을 생성해야 한다.

```
npm i --save cookie-parser dotenv express express-session morgan

```
package.json
```
  "scripts": {
    "dev": "nodemon",
    "build": "next build",
    "start": "next start"
  },
```
nodemon.json
```
{
  "watch": [
    "server.js",
    "nodemon.json"
  ],
  "exec": "node server.js",
  "ext": "js json jsx"
}

```
server.js
```
const express = require('express');
const next = require('next');
const morgan = require('morgan');
const cookieParser = require('cookie-parser');
const expressSession = require('express-session');
const dotenv = require('dotenv');

const dev = process.env.NODE_ENV !== 'production';
const prod = process.env.NODE_ENV === 'production';

const app = next({ dev });
const handle = app.getRequestHandler();
dotenv.config();

app.prepare().then(() => {
  const server = express();

  server.use(morgan('dev'));
  server.use(express.json());
  server.use(express.urlencoded({ extended: true }));
  server.use(cookieParser(process.env.COOKIE_SECRET));
  server.use(expressSession({
    resave: false,
    saveUninitialized: false,
    secret: process.env.COOKIE_SECRET,
    cookie: {
      httpOnly: true,
      secure: false,
    },
  }));

  server.get('/hashtag/:tag', (req, res) => {
    return app.render(req, res, '/hashtag', { tag: req.params.tag });
  });

  server.get('/user/:id', (req, res) => {
    return app.render(req, res, '/user', { id: req.params.id });
  });

  server.get('*', (req, res) => {
    return handle(req, res);
  });

  server.listen(3060, () => {
    console.log('next+express running on port 3060');
  });
});

```

## eslint 설정
---
vscode에서 prettier 및 eslint를 설치해 준 후,.eslintrc파일을 루트 폴더에 설치해 주고, 아래 내용을 입력해 주면 되는데, airbnb 코드 형식은 제약이 심하므로 아래 rules에 형식을 맞추기 싫은 것은 추가해 주면 에러 표시가 없어진다.
```
{
  "parser": "babel-eslint",
  "parserOptions": {
    "ecmaVersion": 2018,
    "sourceType": "module",
    "ecmaFeatures": {
      "jsx": true
    }
  },
  "env": {
    "browser": true,
    "node": true,
    "es6": true
  },
  "extends": [
    "airbnb"
  ],
  "plugins": [
    "import",
    "react-hooks"
  ],
  "rules": {
    "no-underscore-dangle": "off",
    "react/forbid-prop-types": 0,
    "object-curly-newline": 0,
    "jsx-a11y/anchor-is-valid": 0,
    "arrow-body-style": 0,
    "react/prefer-stateless-function":0,
    "react/jsx-filename-extension": 0,
    "react/jsx-one-expression-per-line": 0
  }
}
```
자세한 설정은 아래 velog 페이지 참조
* https://velog.io/@velopert/eslint-and-prettier-in-react

