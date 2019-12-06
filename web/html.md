# html 정리

### emmet로 html 태그 작성하기

1. !emmet으로 html snippet생성
2. div>ul>li : 자식 노드 형태로 생성된다.
3. div+p+bq : 형제 노드 형태로 생성된다.
4. ul*5>li*5 : list 5개에 list item 5개씩 생성된다.
5. ul>li.item*5 : li에 item이라는 클래스가 생성된다.

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

### css gird
1. flex의 경우 멀티 라인 블럭에 대해서 제대로 처리해 주지 못한다. 이를 위해 grid system이 등장하였다.
2. display:grid;가 설정된 tag가 grid-contatiner이고, grid-template-columns, grid-template-rows, 속성으로 grid 갯수를 설정할 수 있다. 자식 태그가 많아도, grid의 갯수만큼만 화면에 표현된다.
3. grid-auto-row: 100px; 을 하게 되면 api에서 호출된 알수 있는 갯수의 데이타를 표현할 수 있다. grid-auto-flow로 main axis를 변경할 수 있다.
4. grid-template-areas를 이용하면 사이트의 레이아웃을 잡을 수 있다.
- grid-auto-row:200px;로 가로 길이를 잡아줌.
- grid-template-areas:"header header header" "content content sidebar" "content content sidebar" "footer footer footer"; 로 사이트 레이아웃 템플릿을 잡아줌.
- grid-items에서 grid-area:header로 같이 내용을 담을 영역을 정해줌. 이때 이름이 일치하여야 함.

