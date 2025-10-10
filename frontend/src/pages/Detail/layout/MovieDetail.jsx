import { useNavigate } from 'react-router-dom';
import mark from '../../../assets/bookmark.png';
import marked from '../../../assets/bookmark_marked.png';
import { useEffect, useState } from 'react';

export const MovieDetail =({quote})=>{

 const navigation = useNavigate();
 const [isLogin, setIsLogin] = useState(true);
 const [bookmark, setBookMarked] = useState(true);

 useEffect(()=>{
    if(isLogin){
        /**로그인한 사용자가 이 글에 북마크를 했는지 데이터 불러오기 */
        setBookMarked(true);
    }
    
 },[isLogin]);

 const onIsLogin =()=>{
    if(!isLogin){
        alert('로그인이 필요한 기능입니다.');
        return;
    }
    /** DB 사용자 북마트 데이터 업데이트 필요 */
    setBookMarked(!bookmark);
 }

  const onSearchList =(input)=>{
    navigation('/searchlist/'+input);
  }

    return(
        <>
         <div className="flex flex-col mt-10">
                  <div className="text-3xl mb-5">MOVIE MARKY</div>
                    <div className="flex items-end mt-3">
                        <label className="w-1/12 text-sm text-end pb-3">영화 제목 </label>
                        <div className="w-4/6 text-xl text-start rounded-lg p-2 pl-4 ml-3 cursor-pointer" onClick={()=>onSearchList(quote.title)}>{quote.title}</div>
                     </div>
                     <div className="flex justify-center mt-3">  
                        <div className="w-4/5 text-main-white pt-12 pb-12 bg-main-green rounded-lg p-2 pl-4 ml-3 shadow-lg shadow-gray-400">{quote.content}</div>
                     </div>
                    <div className="flex justify-end mt-3">  
                        <div className=" flex border-2 border-sub-darkgreen w-1/12 items-end rounded-lg p-3 mr-14">
                            <img className="size-5 cursor-pointer" onClick={onIsLogin} src={(isLogin&&bookmark)?marked:mark}/>
                        </div>
                     </div>
                     <div className="flex items-end mt-3">
                        <label className="w-1/12 text-sm text-end pb-3">감독 </label>
                        <div className="w-4/6 text-start rounded-lg p-2 pl-4 ml-3 text-sm pb-3 cursor-pointer" onClick={()=>onSearchList(quote.creater)}>{quote.creater}</div>
                    </div>
        
                    {quote.subData && (<>
                    <div className="flex items-end mt-3">
                        <label className="w-1/12 text-end pb-3 text-sm">개봉일 </label>
                        <div className="w-4/6 text-start rounded-lg p-2 pl-4 ml-3 text-sm pb-3">{quote.subData}</div>
                        </div></>)} 
        
                    {quote.tags && (
                    <div className="flex items-end mt-3">
                         <label className="w-1/12 text-end pb-3 text-sm">TAGS </label>
                        <div className="w-4/6 text-start rounded-lg p-2 pl-4 ">
                        {quote.tags.map(
                            (t)=>(
                                <span key={t.id} onClick={()=>onSearchList(t)} className="rounded-xl p-2 cursor-pointer bg-main-beige text-xs ml-1 mr-1 mb-1 border-sub-darkbeidge border">{t}</span>
                            )
                        )}</div>
                    </div>
                    )}
                    
                </div>
        
        </>
    );
}