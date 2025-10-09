import { useEffect, useState } from "react";
import { useLocation } from "react-router-dom";
import { BookDetail } from "./layout/BookDetail";
import { MovieDetail } from "./layout/MovieDetail";
import { DramaDetail } from "./layout/DramaDetail";

export const Detail=()=>{
    const location = useLocation();
    /** id로 해당 data 불러오기  */
    const id = location.state?.key;
    const [mode, setMode]=useState('');

    const [quote,setQuote]=useState('');

    /** dummy data */
    useEffect(()=>{
        const q = {'id':0,'category':0,
            'title':'title','creater':'author book','subData':'',
            'content':'content contentcontentcontentcontentcontent',
            'tags':['warm','hope'],
            'writer':'hana', 'createdAt':'2013-10-23'
        }
        setQuote(q);
        setMode('movie');
    },[]);

    return(
        <>
        {mode=='book'&& <BookDetail quote={quote}/>}
        {mode=='movie'&& <MovieDetail quote={quote}/>}
        {mode=='drama'&& <DramaDetail quote={quote}/>}
        </>
    );
}