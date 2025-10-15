import { useNavigate } from "react-router-dom";

export const Logo=()=>{

    const navigator = useNavigate();

    return(
        <>
        <hr className="border-1"></hr>
        <div className="flex justify-center mt-4 mb-4 text-5xl cursor-pointer" onClick={()=>navigator('/')}>WEB NAME</div>
        <hr className="border-1"></hr>
        </>
    );
}