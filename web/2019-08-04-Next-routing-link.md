# root 페이지 생성하기

next는 폴더 구조로 라우팅을 결정한다. 아래와 같이 폴더를 설정하면, `index.js`, `prfile.js`, `signup.js`가 각각 `localhost:3000`, `localhost:3000/profile`, `localhost:3000/signup` 주소가 된다.

```
└──components
├   ├── AppLayout.js
└── pages
    ├── _app.js
    ├── index.js
    ├── profile.js
    └── signup.js
```
아래는 indxe.js를 아래와 같이 작성하면 된다.
```
const Index = () => (
  <div><p>Hello</p></div>
)
export default Index;
```

아래는 next/link의 특성이다.
* Link는 href 태그를 이용하여 라우팅 주소를 설정한다. 이 때 js 파일 이름이 라우팅 주소가 된다.
* Link는 wrapper Componet이름도 herf, as 등의 자체 props를 빼곤 내부 component에 props설정을 해야한다. style이 대표적인 예이다.
* Link 내의 component는 onClick props를 가지고 있어야 한다.
* Link는 location.history를 알아서 처리해 주므로 추가적인 코드가 필요 없다.

```
import Link from 'next/link';
const AppLayout = ({ children }) => (
  <>
    <header>
      <Link href="/"><a>홈</a></Link>
      <Link href="/profile"><a>프로파일</a></Link>
      <Link href="/sginup"><a>회원가입</a></Link>
    </header>
    <section>{children}</section>
  </>
)
```

# Layout 생성하기
_app.js는 root component역할을 하는데, 여기에 layout관련 내용을 설정해주고, {children}를 설정해 주면 하위 component들은 children에 rendering된다. 아래는 antd를 이용한 레이아웃 예제이다. (https://nextjs.org/docs#custom-app 참조) Head는 htmldml `<head>`를 설정할 수 있게 해 준다.
```
import React from 'react';
import Head from 'next/head';
import PropTypes from 'prop-types';
import AppLayout from '../components/AppLayout';

const MyApp = ({ Component, pageProps }) => {
  return (
    <>
      <Head>
        <title>xxxxx</title>
      </Head>
      <AppLayout>
        <Component {...pageProps} />
      </AppLayout>
    </>
  );
};

MyApp.protoTypes = {
  Component: PropTypes.elementType,
  pageProps: PropTypes.object.isRequired,
};
export default MyApp;

```

# 동적 페이지 라우팅



```
{ Component: [Function: Post],
  AppTree: [Function: AppTree],
  router:
   ServerRouter {
     route: '/post',
     pathname: '/post',
     query:
      [Object: null prototype] { title: 'Next js', content: "it's is good to die" },
     asPath:
      '/post?title=Next%20js&content=it%27s%20is%20good%20to%20die' },
  ctx:
   { err: undefined,
     req:
      IncomingMessage {
        _readableState: [ReadableState],
        readable: true,
        _events: [Object],
        _eventsCount: 1,
        _maxListeners: undefined,
        socket: [Socket],
        connection: [Socket],
        httpVersionMajor: 1,
        httpVersionMinor: 1,
        httpVersion: '1.1',
        complete: true,
        headers: [Object],
        rawHeaders: [Array],
        trailers: {},
        rawTrailers: [],
        aborted: false,
        upgrade: false,
        url:
         '/post?title=Next%20js&content=it%27s%20is%20good%20to%20die',
        method: 'GET',
        statusCode: null,
        statusMessage: null,
        client: [Socket],
        _consuming: false,
        _dumped: false },
     res:
      ServerResponse {
        _events: [Object],
        _eventsCount: 1,
        _maxListeners: undefined,
        outputData: [],
        outputSize: 0,
        writable: true,
        _last: false,
        chunkedEncoding: false,
        shouldKeepAlive: true,
        useChunkedEncodingByDefault: true,
        sendDate: true,
        _removedConnection: false,
        _removedContLen: false,
        _removedTE: false,
        _contentLength: null,
        _hasBody: true,
        _trailer: '',
        finished: false,
        _headerSent: false,
        socket: [Socket],
        connection: [Socket],
        _header: null,
        _onPendingData: [Function: bound updateOutgoingData],
        _sent100: false,
        _expect_continue: false,
        statusCode: 200,
        locals: {},
        flush: [Function: flush],
        write: [Function: write],
        end: [Function: end],
        on: [Function: on],
        writeHead: [Function: writeHead],
        [Symbol(isCorked)]: false,
        [Symbol(outHeadersKey)]: null },
     pathname: '/post',
     query:
      [Object: null prototype] { title: 'Next js', content: "it's is good to die" },
     asPath:
      '/post?title=Next%20js&content=it%27s%20is%20good%20to%20die' } }
```