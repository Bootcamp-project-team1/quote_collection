from fastapi import APIRouter

from . import auth, book, bookmark, producer, publisher, quote, source, tag, user , movie ### Movie추가 ### quote_tag 임시 비활성화

router = APIRouter()

# router.include_router(auth.router)
# router.include_router(book.router)
# router.include_router(bookmark.router)
# router.include_router(producer.router)
# router.include_router(publisher.router)
# router.include_router(quote.router)
# # router.include_router(quote_tag.router) 임시 비활성화
# router.include_router(source.router)
# router.include_router(tag.router)
# router.include_router(user.router)
# router.include_router(movie.router) ### Movie추가 ###


# 각 라우터를 포함시킬 때, 해당 기능의 API 경로(prefix)를 명확하게 지정해줍니다.
router.include_router(auth.router, prefix="/auth", tags=["auth"])
router.include_router(book.router, prefix="/book", tags=["book"])
router.include_router(bookmark.router, prefix="/bookmark", tags=["bookmark"])
router.include_router(producer.router, prefix="/producer", tags=["producer"])
router.include_router(publisher.router, prefix="/publisher", tags=["publisher"])
router.include_router(quote.router, prefix="/quote", tags=["quote"])
# router.include_router(quote_tag.router) # 임시 비활성화
router.include_router(source.router, prefix="/source", tags=["source"])
router.include_router(tag.router, prefix="/tag", tags=["tag"])
router.include_router(user.router, prefix="/users", tags=["users"])

# ▼ Movie 라우터 추가 ▼
# /movies 라는 경로를 명확하게 지정해줍니다.
router.include_router(movie.router, prefix="/movies", tags=["movies"])