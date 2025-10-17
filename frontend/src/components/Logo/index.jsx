import { useNavigate } from "react-router-dom";

export const Logo=()=>{

    const navigator = useNavigate();

    return(
        <>
        <hr className="border-1"></hr>
        <div className="flex justify-center mt-5 mb-5 text-5xl cursor-pointer" onClick={()=>navigator('/')}>Momentary</div>
        <hr className="border-1"></hr>
        </>
    );
}