# html 정리

### emmet로 html 태그 작성하기

1. !emmet으로 html snippet생성
2. div>ul>li : 자식 노드 형태로 생성된다.
3. div+p+bq : 형제 노드 형태로 생성된다.
4. ul*5>li*5 : list 5개에 list item 5개씩 생성된다.
5. ul>li.item*5 : li에 item이라는 클래스가 생성된다.
6. ul>li.items^span.title ^부모 태그로 이동한다.

추가적인 문법은 아래 사이트 참조하면 된다.
https://docs.emmet.io/abbreviations/syntax/

### vscode 단축키

1. cmd(Ctrl) + D : 같은 단어를 여러 개를 선택하여 편집하고 싶을 때
2. (dd)(Alt) + click : 여러 개의 위치에서 동시에 편집하고 싶을 때
3. (dd)(Alt) + Shift + Drag : Drag한 영역을 편집하고 싶을 때
4. (dd)(Alt) + 화살표(up/down) : 하나의 라인이나 여러 라인을 이동시키고 싶을 때
5. (dd)(Alt) + Shift + 화살표(up/down) : 하나의 라인이나 여러 라인을 아래에 복사하고 싶을 때
6. cmd(Ctrl) + B : 옆창 열기/닫기

### css flex

1. flex는 flex-container와 flex-items으로 구성된다. flex-items을 어떻게 배치할 지 결정한다.
2. display:flex;가 설정된 tag가 flex-container이며, 직계 자식에게만 영향을 준다. (tag or value)
3. flex-container properties: flex-direction, flex-wrap, justify-contents, align-items이 있다.
4. justify-contens(가로 정렬), align-items(세로 정렬)을 의미하며, flex-direction에 따라 main-axis와 cross axis가 정해진다.
5. flex-wrap:wrap를 하게 되면 flex item의 사이즈가 유지되면서 라인이 변경된다.

### css grid
1. flex의 경우 멀티 라인 블럭에 대해서 제대로 처리해 주지 못한다. 이를 위해 grid system이 등장하였다.
2. display:grid;가 설정된 tag가 grid-contatiner이고, grid-template-columns, grid-template-rows, 속성으로 grid 갯수를 설정할 수 있다. 자식 태그가 많아도, grid의 갯수만큼만 화면에 표현된다.
3. grid-auto-row: 100px; 을 하게 되면 api에서 호출된 알수 있는 갯수의 데이타를 표현할 수 있다. grid-auto-flow로 main axis를 변경할 수 있다.
4. grid-template-areas를 이용하면 사이트의 레이아웃을 잡을 수 있다.
- grid-auto-row:200px;로 가로 길이를 잡아줌.
- grid-template-areas:"header header header" "content content sidebar" "content content sidebar" "footer footer footer"; 로 사이트 레이아웃 템플릿을 잡아줌.
- grid-items에서 grid-area:header로 같이 내용을 담을 영역을 정해줌. 이때 이름이 일치하여야 함.
5. grid-template-columns: repeat(4, 1fr) : repeat함수를 이용하여 1fr 크기를 4개 생성하라는 의미
- 1fr이란 너비를 기준으로 얼마의 크기를 할당할 지를 결정하는 단위로 (1fr 2fr 2fr 1fr이면 너비를 1/6로 나누어 각 화면의 크기를 어느 비율로 할 지 정할 수 있다.)
6. grid-template-columns: minmax(400px, 2fr) repeat(3, 1fr); : 화면을 1/5로 나누고, 첫번째 화면의 경우 최소 사이즈가 400px이고, 2fr이 400px을 넘으면 2fr를 반영하고 작으면 400px을 적용한다.
7. grid-template-columns: max-content repeat(3, 1fr); : 내용물을 위해서 사용 가능한 최대 크기를 사용해라. 
8. grid-template-columns: min-content repeat(3, 1fr); : 내용물을 위해서 가장 적은 크기를 사용하라. 
9. grid-template-columns: repeat(auto-fit, minmax(50px, 1fr)); : 50px 크기로 자식 태그들을 채운다. 갯수가 적을 경우 1fr로 균등하게 할당된다.
10. grid-template-columns: repeat(auto-fill, minmax(50px, 1fr)); // 50px로 자식 태그들을 채운다. 갯수가 적어도 50px 사이즈를 유지한다.
- auto-fit은 content를 stretch해서 browser를 꽉 채우는 것
- auto-fill은 최대한 모으는 거 왜냐하면 더 많은 column를 넣어야 하니깐.
11. place-content: center center; -> height: 100vh 로 하여 높이 설정을 해 주어야 한다. (container에 설정한다)
- place-content: align-content justify-content : align grid cell (grid container를 정렬한다.)
12. place-items: align-items justify-items: align content inside grip cell (container에 설정한다)
13. grip-auto-rows와 grip-template-columns를 이용하여 grid cell을 생성한 후, grid-row, grid-column, gird-area등을 이용하여 grid의 배치나 영역을 조정할 수 있다.
- grip-row:start/end, grip-column:start/end은 자식 태그을 얼마나 할당할 지를 결정한다.
- grip-area: row-start / column-start / row-end / column-end
14. grid-items의 경우 container에서 content의 정렬을 조정하는데, place-self는 각 셀에서 자신의 정렬을 조정한다.
- place-self: align-self justify-self (각 항목에서 content 조절)

### postCSS, CSS4
1. parcel & postcss-preset-env 설치하기
- yarn global add parcel-bundler
- yarn init -y
- yarn add postcss-preset-env
- package.json
``` json
  "scripts": {
    "start": "parcel index.html"
  },
  "postcss": {
    "plugins": {
      "postcss-preset-env": {
        "stages": 0
      }
    }
  }
```
2. functional pseudo-classes
```
li:matches(:nth-child(odd), .target){

}
li:not(.target){

}

```3. css variables
```
:root{
  --awesomeColor:red;
}

a:hover{
  color:var(--awesomeColor);
}

```

### css 실전 예제
아래와 같이 html의 default속성을 정의한다. 아래 내용을 기반으로 수정을 가하면 좋을 듯...
```
:root {
  --borderRadius: 15px;
}

* {
  box-sizing: border-box;
}

h1,
h2,
h3,
h4,
h5 {
  margin: 0;
  padding: 0;
}

body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
    Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
  background-color: #fafafc;
  color: rgba(0, 0, 0, 0.8);
  padding: 0px 15px;
}

.header {
  margin-top: 50px;
  margin-bottom: 25px;
}
```

### 아이콘 꾸미기
- list
-- list item
--- list icon
--- list text

list item들은 5개가 50px사이즈로 옆으로 배열됨.
```
.navigaiton .navigation__list {
  list-style-type: none;
  padding: 0;
  margin: 0;
  display: grid;
  grid-template-columns: repeat(4, 50px);
  grid-gap: 40px;
}

```
item은 icon과 text가 3:1비율로 구성됨.
```
.navigation__list .navigation__item {
  display: grid;
  grid-template-rows: 3fr 1fr;
  grid-gap: 10px;
  text-align: center;
  transition: opacity 0.1s linear;
}

```
list icon class에 shadow를 주고, flex로 이미지 위치 조정함 height, width로 아이콘 사이즈 조정 transition으로 효과 적용.
```
.navigation__item .item__icon {
  background-color: white;
  border-radius: 50%;
  box-shadow: 0 10px 35px rgba(0, 0, 0, 0.05), 0 6px 6px rgba(0, 0, 0, 0.1);
  display: flex;
  justify-content: center;
  align-items: center;
  height: 50px;
  width: 50px;
  transition: box-shadow 0.2s linear;
  cursor: pointer;
}
```
list text는 아래과 같이 조정 weight는 텍스트의 밝기 조정을 표현함.
```
.navigation__item .item__text {
  font-size: 14px;
  font-weight: 600;
}
```
mouse hover에 따른 강조 효과 주기
1. mouse가 없을 때
2. mouse가 list위엔 있고, 해당 list item위에 대한 처리
3. moust가 list위엔 있고, 해당 list item위에 없는 경우에 대한 처리
```
.navigation__list:hover .navigation__item {
  opacity: 0.5;
}
.navigation__list .navigation__item:hover {
  opacity: 1;
}
.navigation__list .navigation__item:hover .item__icon {
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.05), 0 6px 10px rgba(0, 0, 0, 0.1);
}
```

### column으로 증가하는 이미지 표현하기
- featured
-- featured title
-- featured wrapper
--- featured meal
---- featured meal title
---- featured meal button
feature레이아웃을 아래와 같이 전역변수로 관리하는 것이 일관성 유지에 좋다. wrapper에 grid flow롤 column으로 1fr씩 증가하게하여 scroll를 구현하였다. 머리 짱 좋네 ㅡㅡ;;
```
.featured {
  padding: var(--padding);
  padding-top: 25px;
  border-top: var(--borderTop);
}

.featured .featured__title {
  margin: 0;
  font-size: 18px;
  margin-bottom: 20px;
}

.featured .featured__wrapper {
  overflow: scroll;
  display: grid;
  grid-auto-columns: minmax(200px, 1fr);
  grid-auto-flow: column;
  grid-gap: 30px;
  padding-bottom: 20px;
}
```
feature-meal자식에 대해서 flex를 적용하고, 
```
.featured-meal {
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
  height: 150px; /*이미지 사이즈 조정*/
  border-radius: 10px;
  padding: 20px; /* padding을 주어 자식들 위치 조정 */
  color: white;
  background-size: cover;
  background-position: center center;
}

.featured-meal__title {
  margin-right: 10px;
}
.featured-meal__button {
  background-color: white;

  font-size: 15px;
  text-align: center;
  display: flex;
  align-items: center;
  justify-content: center;
}
.featured-meal:first-child {
  background-image: linear-gradient(rgba(0, 0, 0, 0.2), rgba(0, 0, 0, 0.2)),
    url(https://i.pinimg.com/564x/d9/26/7e/d9267eb5f9756e0664191f0d148a11bd.jpg);
}

.featured-meal:last-child {
  background-image: linear-gradient(rgba(0, 0, 0, 0.2), rgba(0, 0, 0, 0.2)),
    url(https://i.pinimg.com/564x/2f/db/39/2fdb393218271fbf0464e8c0818a1a2b.jpg);
}

.featured-meal:nth-child(2) {
  background-image: linear-gradient(rgba(0, 0, 0, 0.2), rgba(0, 0, 0, 0.2)),
    url(https://i.pinimg.com/564x/b7/90/da/b790daca8c52b830b63c6d14d3f1cad7.jpg);
}

.featured-meal:nth-child(3) {
  background-image: linear-gradient(rgba(0, 0, 0, 0.2), rgba(0, 0, 0, 0.2)),
    url(https://i.pinimg.com/564x/7c/dc/81/7cdc811124f1e0bdce19712fec67c22c.jpg);
}
```

### grid 가로 정렬 예
- grid
-- grid item
--- grid photo
--- grid title
--- grid subtitle
```
.grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-gap: 20px;
}
.grid-item .grid-item__photo {
  max-width: 100%;
  border-radius: var(--borderRadius);
  margin-bottom: 10px;
}

.grid-item .grid-item__title {
  font-weight: 800;
  font-size: 16px;
}

.grid-item .grid-item__subtitle {
  color: rgba(0, 0, 0, 0.6);
}
```

### CSS Layout position property
1. position property는 element의 위치를 어떻게 처리할 때에 대한 타입을 정할 수 있다.
2. static, relative, fixed, absolute, sticy등이 있다.
4. fixed는 viewport기준으로 위치를 표시한다. 화면의 절대적인 위치를 정할 수 있다.
5. absolute는 positioned ancestor기준으로 상대 위치를 정할 수 있다. 그래서 ancestor position을 relative로 하고, 자식 element의 위치를 absolute로 정할 수 있다.
