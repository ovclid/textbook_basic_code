#CH09-04. 딕셔너리 수정과 삭제

##################################################################
##딕셔너리의 항목을 모두 삭제하려면 clear( )를 사용

phone_book = {'홍길동':'010-1234-5678',
	      '강감찬':'010-1111-2222',
	      '이순신':'010-3333-4444'}
phone_book.clear( )	  #모든 항목 삭제
print(phone_book)