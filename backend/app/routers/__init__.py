from fastapi import APIRouter

from . import auth, book, bookmark, producer, publisher, quote, quote_tag, source, tag, user

router = APIRouter()

router.include_router(auth.router)
router.include_router(book.router)
router.include_router(bookmark.router)
router.include_router(producer.router)
router.include_router(publisher.router)
router.include_router(quote.router)
router.include_router(quote_tag.router)
router.include_router(source.router)
router.include_router(tag.router)
router.include_router(user.router)
