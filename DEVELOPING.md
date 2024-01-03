# 구조
Book: 예산안. 수입과 지출로 나뉨. 예산안은 하나 이상의 Item으로 구성됨. [클래스, json으로 구현]
Item: 예산안을 이루는 하나의 항목. 수입과 지출로 나뉨. 이름, 카테고리, 비용(또는 수입)으로 구성됨 [딕셔너리로 구현]

```json: Book.json
{
	"exe_date":"YYYY/MM"
	"incomes":{"item1":{category:"항목 종류", "budget":항목 예산},"item2":{},...}
	"expenses":{{},{},...}
}
```

Item 딕셔너리
```
{"kind":"종류", "name":"item1", "category":"항목", "budget":항목 예산}
```