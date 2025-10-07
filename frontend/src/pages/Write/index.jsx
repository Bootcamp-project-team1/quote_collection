import { useState } from "react";
import { BookWrite } from "./layout/bookwrite";
import { MovieWrite } from "./layout/MovieWrite";
import { DramaWrite } from "./layout/DramaWrite";

export const Write = () =>{

    const [mode, setMode]=useState("book");

    const onBook =()=>{
        setMode('book');
    }

     const onMovie =()=>{
        setMode('movie');
    }

     const onDrama =()=>{
        setMode('drama');
    }

    return(
        <>
        <ul className="flex flex-row justify-center mt-3">
            <li className={mode=='book'?"ml-6 mr-6 cursor-pointer border-b-4 border-main-green pb-2 w-2/12":"w-2/12 ml-6 mr-6 cursor-pointer"} onClick={onBook}> book </li>
            <li className={mode=='movie'?"ml-6 mr-6 cursor-pointer border-b-4 border-main-green pb-2 w-2/12":"w-2/12 ml-6 mr-6 cursor-pointer"} onClick={onMovie}> movie </li>
            <li className={mode=='drama'?"ml-6 mr-6 cursor-pointer border-b-4 border-main-green pb-2 w-2/12":"w-2/12 ml-6 mr-6 cursor-pointer"} onClick={onDrama}> drama </li>
        </ul>

        {mode == 'book'&& <BookWrite/>}
        {mode == 'movie'&& <MovieWrite/>}
        {mode == 'drama'&& <DramaWrite/>}
        </>
    );
}