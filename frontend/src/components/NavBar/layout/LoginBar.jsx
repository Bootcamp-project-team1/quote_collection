import { NavLink } from "react-router-dom";

export const LoginBar=()=>{
    return(
        <>
        <nav className="float-right mr-3 mt-3 text-sm">
           <NavLink className="mr-3" to='/BookMark'>Bookmark</NavLink>
           <NavLink className="mr-3" to='/Upload'>upload</NavLink>
           <NavLink className="mr-3" to='/Mypage'>mypage</NavLink>
        </nav>
        </>
    );
}