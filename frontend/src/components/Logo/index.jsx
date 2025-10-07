import { useNavigate } from "react-router-dom";

export const Logo=()=>{

    const navigator = useNavigate();

    return(
        <>
        {/* 클릭 시 root page 로 이동 */}
        <div className="flex justify-center mt-4 pb-4 text-5xl border-b-2 " >
            <div className="cursor-pointer"
                onClick={()=>{navigator('/')}}>WEB NAME</div>
        </div>
        </>
    );
}