﻿# 튜플은 리스트랑 비슷하긴 한데 값을 변화시킬 수가 없다
t = (1,)
# 일단 소괄호로 감싼다. 요소가 하나면 마지막에 콤마를 추가해 줘야 한다

t = (1, 2, 3)
# 여러개 선언하는 건 열거해 주면 된다

t = 1, 2, 3
# 괄호 생략해도 튜플 처리 된다
print(type(t))

# 얘도 인덱싱, 슬라이싱, 더하기, 곱하기 된다
# 값 변화가 불가능하기 때문에 빌트인 메소드가 몇 개 없다(count, index 있음)
# 리스트가 가지고 있는 메소드 중 값 변화와 수정에 관한 메소드 외의 메소드를 사용할 수 있다.
