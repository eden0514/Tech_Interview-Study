## Callback 함수란?
Node.js는 비동기식 플랫폼으로 파일 I/O가 끝날 때까지 기다리지 않는다. Node.js는 콜백을 사용한다. 콜백은 주어진 작업이 완료될 때 호출되는 함수이다. 이렇게 작성을 하면 차단이 방지되고, 그 동안에는
다른 코드가 실행될 수 있다. 콜백은 "당신이 그 일을 마치면 이 모든 것을 하라"고 말할 수 있는 인터페이스를 제공한다. 이를 통해 OS가 동시에 처리할 수 있는 만큼의 IO작업을 수행할 수 있다.
즉, 콜백은 async를 핸들링할 수 있는 방법입니다.

```js
const plus = (a,b,callback) => {
  let sum = a + b;
  callback(sum);
}

plus(1,2,function(res){
  console.log(res);  
})

// callback error handling
const someFunc = callback => {
  somethingFunctionHappen()
  if(Good){
    callback(null,something)
  }
  if(Bad){
    callback(something,null)
  }
}

someFunc((err,data)=>{
  if(err){
    console.log('oops...Error');
    return;
  }
  return data;
})
```
### callback hell
callback함수를 이용해서 비동기이지만 순서를 보장받을 수 있다는 장점이 있지만, callback 함수의 문제점으로 callback hell이라는 것이 있다. 이는 순차적으로 계속해서 콜백을 넣어 작성을 하는 경우,
가독성 측면과 코드를 관리하기 상당히 어려워진다는 단점이 존재한다.
```js
const print = () => {
  somePrintFunc("a",()=>{
    somePrintFunc("b",()=>{
      somePrintFunc("c",()=>{
      })
    })
  })
}
```
 
