# 파일 구조
Book: 예산안 파일. 수입과 지출로 나뉨. 예산안은 하나 이상의 Item으로 구성됨.
Item: 예산안을 이루는 하나의 항목. 수입과 지출로 나뉨. 이름, 카테고리, 비용(또는 수입)으로 구성됨

```json: Book.json
{
	"exe_date":"YYYY/MM"
	"incomes":{"item1":{category:"항목 종류", "budget":항목 예산},"item2":{},...}
	"expenses":{{},{},...}
}
```

# 클래스, 기능 구현
Book: 예산안 파일을 구현한 클래스. 새로운 예산안 파일 생성, 기존의 예산안 파일 수정, 삭제
BookManage: Book 클래스의 인스턴스들을 관리하고 접근을 돕는 클래스. 
Book 클래스의 인스턴스 생성을 한다. 
Book 클래스의 경우 파일 중복 검사, 잘못된 값 검출 등을 하지 않기 때문에 BookManage 클래스에서 도맡는다. 

파라미터로 사용되는 Item 딕셔너리 
```
{"kind":"종류", "name":"item1", "category":"항목", "budget":항목 예산}
```