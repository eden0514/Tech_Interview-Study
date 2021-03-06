## Selection Sort(선택 정렬)란?
> **시간복잡도 O(n<sup>2</sup>)**  
선택 정렬은 일단 자리가 정해져 있고, 그 위치에 어떤 원소를 넣을지 선택하는 알고리즘을 말한다. 선택 정렬은 제자리 정렬 알고리즘 중 하나이다.  
선택 정렬은 알고리즘이 단순하며, 사용할 수 있는 메모리가 제한적인 경우 사용 시 성능 상의 이점이 있다.

## 선택 정렬이 정렬되는 순서
1. 주어진 리스트 중 최소값을 찾는다.
2. 그 값을 맨 앞에 위치하는 값과 교체한다.
3. 맨 처음을 뺀 위치에서 나머지 리스트를 위와 같은 방법으로 교체한다.
4. 리스트 끝까지 위 과정을 반복한다.

### Javascript로 선택 정렬 작성
```js
function selectionSort (arr) {
  for(let i = 0; i < arr.length; i++){
    let minIdx = i;
    for(let j = i +1 ; j < arr.length; j++){
      if(arr[minIdx] > arr[j]){
        minIdx = j;
      }
    }
    if(minIdx !== i){
      [arr[i],arr[minIdx]] = [arr[minIdx],arr[i]]
    }
  }
  return arr;
}
```
