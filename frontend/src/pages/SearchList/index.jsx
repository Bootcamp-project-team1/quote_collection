import { Search } from "../../components/Search";
import { useLocation } from "react-router-dom";

export const SearchList =()=>{

    const location = useLocation();
    const prevInput=location.state?.key;

    return(
        <>
        <div className="flex justify-center">
        <Search prevInput={prevInput}/>
        </div>
         <div className="flex mt-10 justify-center">
            " {prevInput} " results
        </div>
        </>
    );
}