# 데이타 모델링

## 개념적 모델링

### Entity

- Primary Key
- Foregine key

### Attribute

### Relationship

#### Cardinality

- 1:1 관계: 각 아이템별로 관계를 설명하면 이해하는 데 도움이 된다.
예) kim 선생님은 1반 담임만 할 수 있다.
1반 담임은 kim 선생님 한 분밖에 없다.

- 1:N 관계: 각 아이템별로 관계를 설명하면 이해하는 데 도움이 된다
예) **kim 유저**는 **여러 개의 댓글**을 작성할 수 있다.
**댓글1**은 **kim 유저**가 쓴 것이다. (공동으로 쓸 수 없다.)

- M:N 관계: 각 아이템별로 관계를 설명하면 이해하는 데 도움이 된다
예) **kim 유저**는 **여러 개의 댓글**을 작성할 수 있다.
**글1**은 **공동 집필**이 가능하다.

#### Optionality

- Entity간의 필수인지 아닌지에 따라 결정된다.
예) 글은 댓글이 있을 **필요가 없다**.
댓글은 **반드시** 글이 있어야 한다.

## 논리적 모델링(정규화)

- 3정규화까지 많이 사용한다.
<https://docs.google.com/spreadsheets/d/1udvYV60wmX1oz2d7tNdaYBFf9Y6pXQtATNBUXQz2pak/edit#gid=0>
