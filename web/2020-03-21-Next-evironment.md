# zeit now 설정

```bash
npm i -g now
```

## now.sh, .nowignore 설정

## now login

## now

## server.js

참조 : https://github.com/zeit/next.js/#custom-server-and-routing

```js
const { createServer } = require('http')
const { parse } = require('url')
const next = require('next')

const dev = process.env.NODE_ENV !== 'production'
const app = next({ dev })
const handle = app.getRequestHandler()

app.prepare().then(() => {
  createServer((req, res) => {
    // Be sure to pass `true` as the second argument to `url.parse`.
    // This tells it to parse the query portion of the URL.
    const parsedUrl = parse(req.url, true)
    const { pathname, query } = parsedUrl

    if (pathname === '/a') {
      app.render(req, res, '/b', query)
    } else if (pathname === '/b') {
      app.render(req, res, '/a', query)
    } else {
      handle(req, res, parsedUrl)
    }
  }).listen(3000, err => {
    if (err) throw err
    console.log('> Ready on http://localhost:3000')
  })
})
```

이후 `package.json`에서 script를 변경한다

```json
{
  "scripts": {
    "dev": "node server.js",
    "build": "next build",
    "start": "NODE_ENV=production node server.js"
  }
}
```

## koa.js

- express 다음 버전?
- ssr을 위한 server framework

## 설치

```
yarn add koa @koa/cors koa-router koa-body
```

## server.js

```js
const Koa = require('koa');
const cors = require('@koa/cors');
const next = require('next');
const Router = require('koa-router');

const port = parseInt(process.env.PORT, 10) || 3000;
const dev = process.env.NODE_ENV !== 'production';
const app = next({ dev });
const handle = app.getRequestHandler();
const koaBody = require('koa-body');

const api = new Router({ prefix: '/api' });

api.get('/', async context => {
  context.body = 'api';
});

api.get('/ping', async context => {
  context.body = 'pong';
});

app
  .prepare()
  .then(() => {
    const server = new Koa();
    const router = new Router();

    router.get('*', async context => {
      await handle(context.req, context.res);
      context.respond = false;
    });

    server.use(async (context, next) => {
      context.res.statusCode = 404;
      await next();
    });

    // 미들웨어
    server.use(koaBody({ multipart: true }));
    server.use(
      cors({
        origin: '*',
        allowMethods: ['GET', 'HEAD', 'PUT', 'POST', 'DELETE', 'PATCH'],
        allowHeaders: ['Content-Type', 'Authorization'],
        exposeHeaders: ['Content-Length', 'Date', 'X-Request-Id'],
      }),
    );

    // API
    server.use(api.routes());
    server.use(router.routes());
    // server.use(handle);
    server.listen(port, () => {
      console.log(`> Ready on http://localhost:${port}`);
    });
  })
  .catch(ex => {
    console.log(ex);
    process.exit(1);
  });

```

- file upload의 경우 koa framework에서 multipart upload를 어떻게 하는 지 찾으면 된다.
- server가 요청을 받을 때 get 주소 param에 대한 처리 및 복잡한 분기 처리를 목적으로 koa-body를 사용한다.

## 서버 자동 실행

- npm install -g nodemon (yarn add nodemon)

```bash
"scripts": {
    "dev": "nodemon server.js --exec",
    "build": "next build",
    "start": "NODE_ENV=production node server.js"
    },
```

## 환경변수 설정

- npm install dotenv (yarn add dotenv)

## firebase 설정

- yarn add firebase

- yarn add axios moment underscore