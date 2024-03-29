## 백엔드 어플리케이션 실행

```commandline
docker compose up
```

## 테스트 실행

```sh
# 도커 컴포즈 실행 후
docker exec -it backend /bin/bash
python manage.py test app.tests.test_auth app.tests.test_product
```

## API Endpoints

### 유저

- 회원가입 : /user/signup(POST)
- 로그인 : /user/login(POST)
- 로그아웃 : /user/logout(POST)

### 상품

- 상품 생성 : /products - POST
- 상품 상세 조회 : /products/pk - GET
- 상품 삭제 : /products/pk - DELETE
- 상품 리스트 조회 : /products - GET
  - param : `search`
- 상품 수정 : /products/pk - PATCH

### Swagger API Docs

- Swagger API Docs : /docs

![](https://github.com/kdh92417/user-product-api/assets/58774316/d3d49ccb-0338-4032-bac9-603527d3fae0)