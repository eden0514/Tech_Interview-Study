## Express란?
Express 홈페이지를 보면, Express는 웹 및 모바일 애플리케이션을 위한 강력한 기능 세트를 제공하는 최소의 유연한 Node.js 웹 애플리케이션 프레임워크라고 설명한다. 즉, Express는 Node.js 환경에서 웹 서버, 또는 API 서버를 제작하기 위해 사용되는 인기있는 프레임워크이다.

[프레임워크와 라이브러리의 개념](https://github.com/eden0514/Tech_Interview-Study/blob/main/Back-end/%ED%94%84%EB%A0%88%EC%9E%84%EC%9B%8C%ED%81%AC%EC%99%80%20%EB%9D%BC%EC%9D%B4%EB%B8%8C%EB%9F%AC%EB%A6%AC.md)

### Node.js란?
Node.js란 Chrome V8 JavaScript 엔진으로 빌드된 JavaScript 런타임(어떤 프로그래밍 언어가 동작할 수 있는 프로그램)이다. Node.js는 이벤트 기반, 논 블로킹 I/O모델을 사용해 가볍고 효율적이다. Node.js의 패키지 생태계인 npm은 세계에서 가장 큰 오픈 소스 라이브러리 생태계이기도 하다.  
예전에는 JavaScript 런타임이 브라우저밖에 존재하지 않았는데, 이러한 한계를 극복하고자 나온 것이 Node.js이다.

---
### 라우팅?
라우팅은 애플리케이션 엔드 포인트(URI)의 정의, 그리고 URI가 클라이언트 요청에 응답하는 방식을 말함.
```js
const express = require('express');
const app = express();

app.get('/',function(req,res){
  res.send('Hello World');
});
```
#### 기본 라우팅
라우팅은 URI 및 특정한 HTTP 요청 메소드(GET, POST 등)인 특정 엔드포인트에 대한 클라이언트 요청에 애플리케이션이 응답하는 방법을 결정하는 것을 말한다. 각 라우트는 하나 이상의 핸들러 함수를 가질 수 있으며, 이러한 함수는 라우트가 일치할 때 실행된다.
라우트 정의에는 다음과 같은 구조가 필요함.
```js
app.METHOD(PATH,HANDLER)
/*
* app => express의 인스턴스
* METHOD => HTTP 요청 메소드
* PATH => 서버에서의 경로
* HANDLER => 라우트가 일치할 때 실행되는 함수
*/

//예제)
app.get('/',function(req,res){
  res.send('Hello World');
});
```
#### 라우트 핸들러
위에서 언급했듯이 라우트가 일치할 때 실행되는 함수를 말하는데, 미들웨어와 비슷하게 작동하는 여러 콜백 함수를 제공하여 요청을 처리할 수 있다. 유일한 차이점은 이러한 콜백은 *next('route')*를 호출하여 나머지 라우트 콜백을 우회할 수 있다는 점이다.
```js
//하나의 콜백함수의 경우
app.get('/',function(req, res){
  res.send('Hello World');
});

//두 개 이상의 콜백함수의 경우
app.get('/', function(req, res){
  console.log('HELLO WORLD');
  next() // next 오브젝트를 반드시 지정해야 함
}, function(req, res){
  res.send('BYE BYE');
})
```
#### 응답 메소드
응답 객체에 대한 메소드(res)는 응답을 클라이언트로 전송하고 요청-응답 주기를 종료할 수 있다. 만약 응답 메소드를 호출하지 않는 경우, 클라이언트 요청은 정지된 상태로 방치가 된다.
|메소드|설명|
|---|------|
|res.download()|파일이 다운로드되도록 프롬프트한다.|
|res.end()|응답 프로세스를 종료함.|
|res.json()|JSON 응답을 전송함.|
|res.jsonp()|JSONP 지원을 통해 JSON 응답을 전송.|
|res.redirect()|요청의 경로를 재지정함.|
|res.render()|보기 템플릿을 렌더링함.|
|res.send()|다양한 유형의 응답을 전송.|
|res.sendFile()|파일을 옷텟 스트림의 형태로 전송.|
|res.sendStatus()|응답 상태코드를 설정한 수 해당 코드를 문자열로 표현한 내용을 응답 본문으로서 전송함.|

#### app.route()
app.route()를 이용하면 라우트 경로에 대해 체인 가능한 라우터 핸들러를 작성할 수 있다. 경로는 한곳에 지정되어 있으므로, 모듈식 라우트를 작성하면 중복성과 오타가 감소하여 도움이 된다.
```js
app.route('/book')
  .get(function(req,res){
    res.send('get a book');
  })
  .post(function(req,res){
    res.send('add a book');
  })
  .put(function(req,res){
    res.send('update the book')
  })
```
#### express.Router
express.Router 클래스를 사용하면 모듈식 마운팅 가능한 핸들러를 작성할 수 있다. Router 인스턴스는 완전한 미들웨어이자 라우팅 시스템이며, 따라서 미니앱이라고 불리는 경우가 많다.
```js
//birds.js
const express = require('express');
const router = express.Router();

router.use(funtion timeLog(req,res,next){
  console.log('Time : ', Date.now());
  next();
})

router.get('/',funtion(req,res){
  res.send('bird homePage');
});

router.get('/about',funtion(req,res){
  res.send('About bird');
});

module.exports = router;
```
이후 앱 내에서 다음과 같이 라우터 모듈을 로드하십시오.
```js
const birds = require('./birds')// 위에 작성한 birds.js 가져옴.

app.use('/birds', birds);
//이제 앱은 /birds 와 /birds/about에 대한 요청을 처리할 수 있게 된다.
```
---
### 미들웨어(Middleware)
미들웨어는 컨베이어 벨트처럼 각 공정마다 부품을 추가하듯, request에 피요한 기능을 더하거나, 문제가 발견된 불량품을 밖으로 걷어내는 역할을 한다. 미들웨어는 express의 가장 큰 장점이다.  
미들웨어 함수는 요청 객체(req)와 응답 객체(res), 그리고 애플리케이션의 요청-응답 주기 중 그 다음의 미들웨어 함수에 대한 액세스 권한르 갖는 함수이다. 그 다음의 미들웨어함수는 일반적으로 next라는 이름의 변수로 표시된다.

#### 자주 사용하는 미들웨어
먼저, 미들웨어를 사용하는 상황은 다음과 같다.
1. 모든 요청에 대해 url이나 메소드를 확인할 때
2. POST 요청등에 포함된 body(payload)를 구조화할 때(쉽게 얻어내고자 할 때)
3. 모든 요청/응답에 CORS 헤더를 붙여야할 때
4. 요청 헤더에 사용자 인증 정보가 담겨 있는지 확인 할 때

미들웨어를 이용하면 node.js만으로 구현한 서버에서는 다소 번거로울 수 있는 작업을 보다 쉽게 적용 가능하다.


