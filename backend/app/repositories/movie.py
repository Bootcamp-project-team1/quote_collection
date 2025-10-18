from sqlalchemy.orm import Session
from app.models import movie as movie_model
from app.models import quote as quote_model
from app.models import tag as tag_model
from app.schemas import movie as movie_schema

class MovieRepository:
    def create_movie(self, db: Session, movie_data: movie_schema.MovieCreate):
        # 1. 영화(Movie) 정보 생성
        new_movie = movie_model.Movie(
            title=movie_data.title,
            director=movie_data.director,
            release_date=movie_data.release_date
        )
        db.add(new_movie)
        db.flush() # new_movie의 id를 할당받기 위해 flush

        # 2. 명대사(Quote) 정보 생성 및 영화와 연결
        new_quote = quote_model.Quote(
            content=movie_data.quote_content,
            movie_id=new_movie.id,
            #  누락된 필수값 임시로 추가 (프론트랑 연결확인위해 임시로 넣은 값, 나중에 실제 값으로 변경 필요)
            user_id=1,      # 임시로 1번 유저가 작성했다고 가정 db에 맞게 수정 필요 나중에 실제 유저 아이디로 변경 필요
            source_id=1,    # 임시로 1번 출처라고 가정
            page="0"        # page 필드도 필수값이므로 임시값 추가
        )
        db.add(new_quote)

        # 3. 태그(Tag) 처리
        for tag_name in movie_data.tags:
            # 기존에 태그가 있는지 확인
            existing_tag = db.query(tag_model.Tag).filter(tag_model.Tag.name == tag_name).first()
            if existing_tag:
                # 있으면 기존 태그를 영화에 추가
                new_movie.tags.append(existing_tag)
            else:
                # 없으면 새로 태그를 만들어 영화에 추가
                new_tag = tag_model.Tag(name=tag_name)
                db.add(new_tag)
                new_movie.tags.append(new_tag)

        db.commit()
        db.refresh(new_movie)
        return new_movie

movie_repo = MovieRepository()