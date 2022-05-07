# import theater_module # theater_module 파일에서 가져옴
# theater_module.price(3)
# theater_module.price_moning(4)
# theater_module.price_soldier(5)

# import theater_module as mv
# mv.price(3)
# mv.price_moning(4)
# mv.price_soldier(5)

# from theater_module import *
# price(3)
# price_moning(4)
# price_soldier(5)

# from theater_module import price, price_moning
# price(5)
# price_moning(6)
# price_soldier(7) #import 에서 price_soldier를 쓰던가 *로 전체를 가져와야지 price_soldier를 쓸 수 있다.

from theater_module import price_soldier as price
price(5) # 이렇게 정의하면 솔져에 대한 별명을 price로 붙였기 때문에 기존에 있는 price가 아닌 솔져에 대한 price가 나온다